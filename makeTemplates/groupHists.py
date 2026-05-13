#!/usr/bin/python
# python3 groupHists.py $iPlot $region $isCategorized $pfix
# python3 groupHists.py VLQBMass all False _Dec2025
# python3 groupHists.py VLQBMass all False kinematicsall_Dec2025_RJR
import os,sys,time,math,datetime,itertools,ctypes
from ROOT import gROOT,TFile,TH1F,TH2D
parent = os.path.dirname(os.getcwd())
sys.path.append(parent)
from samples import targetlumi, lumiStr, systListShort, systListFull, samples_data, samples_signal, samples_electroweak, samples_electroweak3, samples_electroweak4, samples_wjets, samples_singletop, samples_ttbarx, samples_ttbarx3, samples_ttbarx4, samples_qcd, uncorrList_sf, yearList, samples_nonprompt, samples_conversion, samples_higgs
from utils import *

gROOT.SetBatch(1)
start_time = time.time()

if len(sys.argv)>1:
	iPlot = str(sys.argv[1])
else:   
        iPlot = 'Nleps'
if len(sys.argv)>2:
        region = str(sys.argv[2])
else:
        region='3lep' # BAX, DCY, individuals, or all
if len(sys.argv)>3:
        isCategorized = bool(eval(sys.argv[3]))
else:
        isCategorized=False

if isCategorized:
        pfix='templates'+region
else:
        #pfix='kinematicsTEST'+region    #'TEST' is TEMP
        pfix = 'kinematics'+region
if len(sys.argv)>4:
        pfix+=str(sys.argv[4])
else:
        #pfix+='_Oct2025_NoSys'
        pfix+=''                        # TEMP
outDir=f'{os.getcwd()}/{pfix}/'

print('Grouping hists for iPlot',iPlot,', region',region,', isCategorized',isCategorized,', and folder',pfix)


## Override yearList for a year-specific plot
#yearList=['2018']

removeThreshold = 0.0005 # TODO: add if necessary

scaleSignalXsecTo1pb = False # Set to True if analyze.py ever uses a non-1 cross section
doAllSys = False
doPDF = False
if isCategorized: doPDF=False # FIXME later

from samples import samples_ttbar

bkgProcs = {'ewk':samples_electroweak,'ttbar':samples_ttbar,'ttx':samples_ttbarx}
if region == '3lep':
        bkgProcs = {'ewk':samples_electroweak3,'np':samples_nonprompt,'ttx':samples_ttbarx3,'conv':samples_conversion,'higgs':samples_higgs}
elif region == '4lep':
        bkgProcs = {'ewk':samples_electroweak4,'np':samples_nonprompt,'ttx':samples_ttbarx4,'conv':samples_conversion,'higgs':samples_higgs}
massList = [400,700,1000,1300,1600]
sigList = ['BpM'+str(mass) for mass in massList]

isEMlist = ['L'] #['E','M'], 'L' #
if '2D' in outDir: 
        isEMlist =['L']
taglist = ['all']
if isCategorized: 
        #taglist=['tagTjet','tagWjet','untagTlep','untagWlep','allWlep','allTlep']
        #taglist=['allWlep','allTlep'] # TEMP: for code developing only
        taglist=['tagTjet','tagWjet','untagTlep','untagWlep']

catList = ['is'+item[0]+'_'+item[1] for item in list(itertools.product(isEMlist,taglist))]

lumiSys = 0.018 #lumi uncertainty

groupHists = True # TEMP: turn this on to group histograms
getYields = False # TEMP: turn this on to get yield tables
if len(yearList) == 1:
        getYields = False

corrList_sf = systListFull.copy()
mySystList = systListFull
if not isCategorized:
        corrList_sf = systListShort.copy()
        mySystList = systListShort
else:
        for i in range(101):
                mySystList.append('pdf'+str(i))
                corrList_sf.append('pdf'+str(i))
for syst in uncorrList_sf:
        corrList_sf.remove(syst)        
        
### Group histograms
if groupHists:
        if len(yearList) == 1:
                outHistFile = TFile.Open(f'{outDir}templates_{iPlot}_{lumiStr}_{yearList[0]}.root', "RECREATE")
        else:
                outHistFile = TFile.Open(f'{outDir}templates_{iPlot}_{lumiStr}.root', "RECREATE")
        for cat in catList:
                print("PROGRESS: "+cat)
                if region=="all" or isCategorized == False:
                        histoPrefix = f'{iPlot}_{lumiStr}_{cat}'
                else:
                        histoPrefix = f'{iPlot}_{lumiStr}_{cat}_{region}'

                dataHistFile = TFile.Open(f'{outDir}{cat[2:]}/datahists_{iPlot}.root', "READ")
                print(f'this is the file! HERE ----> {dataHistFile}')
                isFirstHist = True
                for dat in samples_data:
                        if samples_data[dat].year not in yearList:
                                continue
                        if isFirstHist:
                                print(histoPrefix+'_'+samples_data[dat].prefix)
                                hists = dataHistFile.Get(histoPrefix+'_'+samples_data[dat].prefix).Clone(f'{histoPrefix}__data_obs')
                                isFirstHist = False
                        else:
                                hists.Add(dataHistFile.Get(histoPrefix+'_'+samples_data[dat].prefix))
                outHistFile.cd()
                hists.Write()
                dataHistFile.Close()

                for proc in bkgProcs:
                        # DID NOT IMPLEMENT REMOVETHRESHOLD
                        bkgHistFile = TFile.Open(f'{outDir}{cat[2:]}/bkghists_{proc}_{iPlot}.root', "READ")
                        bkgGrp = bkgProcs[proc]
                        nomHists = {}
                        systHists = {}
                        systHistsWrite = {}
                        isFirstHistDir = {"2022":True, "2022EE":True, "2023":True, "2023BPix":True}

                        systematicList = mySystList
                        corrList = corrList_sf
                        uncorrList = uncorrList_sf
                
                        for bkg in bkgGrp:
                                if bkgGrp[bkg].year not in yearList:
                                        continue
                                
                                year = bkgGrp[bkg].year
                                bkgPrefix = bkgGrp[bkg].prefix
                                doMuRF = True
                                if (bkgPrefix).find('WW') == 0 or (bkgPrefix).find('WZ') == 0 or (bkgPrefix).find('ZZ') == 0:
                                        doMuRF = False
                                
                                # Group nominal and correlated systs for each year
                                if isFirstHistDir[year]:
                                        nomHists[f'{histoPrefix}__{proc}{year}'] = bkgHistFile.Get(f'{histoPrefix}_{bkgPrefix}').Clone(f'{histoPrefix}__{proc}{year}')
                                        isFirstHistDir[year] = False
                                        if doAllSys:
                                                for syst in systematicList:
                                                        if 'pdf' in syst:
                                                                if doMuRF:
                                                                        systHists[f'{histoPrefix}__{proc}__{syst}{year}'] = bkgHistFile.Get(f'{histoPrefix}_{syst}_{bkgPrefix}').Clone(f'{histoPrefix}__{proc}__{syst}{year}')
                                                                else: # let's add nominal for WW, etc, rather than have nothing...
                                                                        systHists[f'{histoPrefix}__{proc}__{syst}{year}'] = bkgHistFile.Get(f'{histoPrefix}_{bkgPrefix}').Clone(f'{histoPrefix}__{proc}__{syst}{year}')
                                                        else:
                                                                try:
                                                                        systHists[f'{histoPrefix}__{proc}__{syst}{year}Up'] = bkgHistFile.Get(f'{histoPrefix}_{syst}Up_{bkgPrefix}').Clone(f'{histoPrefix}__{proc}__{syst}{year}Up')
                                                                        systHists[f'{histoPrefix}__{proc}__{syst}{year}Down'] = bkgHistFile.Get(f'{histoPrefix}_{syst}Dn_{bkgPrefix}').Clone(f'{histoPrefix}__{proc}__{syst}{year}Down')
                                                                except:                                                                
                                                                        if ('pNet' in syst and ('untag' in cat or ('Wtag' in syst and 'Tjet' in cat) or ('Ttag' in syst and 'Wjet' in cat))):
                                                                                pass
                                                                        else:
                                                                                print('could not process '+syst+' for '+bkg)
                                else:
                                        nomHists[f'{histoPrefix}__{proc}{year}'].Add(bkgHistFile.Get(f'{histoPrefix}_{bkgPrefix}'))
                                        if doAllSys:
                                                for syst in systematicList:
                                                        if 'pdf' in syst:
                                                                if doMuRF:
                                                                        systHists[f'{histoPrefix}__{proc}__{syst}{year}'].Add(bkgHistFile.Get(f'{histoPrefix}_{syst}_{bkgPrefix}'))
                                                                else:
                                                                        systHists[f'{histoPrefix}__{proc}__{syst}{year}'].Add(bkgHistFile.Get(f'{histoPrefix}_{bkgPrefix}'))
                                                        else:
                                                                try:
                                                                        systHists[f'{histoPrefix}__{proc}__{syst}{year}Up'].Add(bkgHistFile.Get(f'{histoPrefix}_{syst}Up_{bkgPrefix}'))
                                                                        systHists[f'{histoPrefix}__{proc}__{syst}{year}Down'].Add(bkgHistFile.Get(f'{histoPrefix}_{syst}Dn_{bkgPrefix}'))
                                                                except:
                                                                        if ('pNet' in syst and ('untag' in cat or ('Wtag' in syst and 'Tjet' in cat) or ('Ttag' in syst and 'Wjet' in cat))):
                                                                                pass
                                                                        else:
                                                                                print('could not process '+syst+' for '+bkg)

                        # add years for corr uncertainties
                        nomHistAllYears = nomHists[f'{histoPrefix}__{proc}{yearList[0]}'].Clone(f'{histoPrefix}__{proc}')
                        if doAllSys:
                                for syst in corrList:
                                        if 'pdf' in syst: # now even VV will have pdf hists in the list (even though fake)
                                                systHistsWrite[f'{histoPrefix}__{proc}__{syst}'] = systHists[f'{histoPrefix}__{proc}__{syst}{yearList[0]}'].Clone(f'{histoPrefix}__{proc}__{syst}')
                                        else:
                                                try:
                                                        systHistsWrite[f'{histoPrefix}__{proc}__{syst}Up'] = systHists[f'{histoPrefix}__{proc}__{syst}{yearList[0]}Up'].Clone(f'{histoPrefix}__{proc}__{syst}Up')
                                                        systHistsWrite[f'{histoPrefix}__{proc}__{syst}Down'] = systHists[f'{histoPrefix}__{proc}__{syst}{yearList[0]}Down'].Clone(f'{histoPrefix}__{proc}__{syst}Down')
                                                except:
                                                        if ('pNet' in syst and ('untag' in cat or ('Wtag' in syst and 'Tjet' in cat) or ('Ttag' in syst and 'Wjet' in cat))):
                                                                pass
                                                        else:
                                                                print('could not process '+syst+' for '+bkg)
                        
                        for year in yearList:
                                if year!=yearList[0]:
                                        nomHistAllYears.Add(nomHists[f'{histoPrefix}__{proc}{year}'])
                                        if doAllSys:
                                                for syst in corrList:
                                                        if 'pdf' in syst:
                                                                systHistsWrite[f'{histoPrefix}__{proc}__{syst}'].Add(systHists[f'{histoPrefix}__{proc}__{syst}{year}'])
                                                        else:
                                                                try:
                                                                        systHistsWrite[f'{histoPrefix}__{proc}__{syst}Up'].Add(systHists[f'{histoPrefix}__{proc}__{syst}{year}Up'])
                                                                        systHistsWrite[f'{histoPrefix}__{proc}__{syst}Down'].Add(systHists[f'{histoPrefix}__{proc}__{syst}{year}Down'])
                                                                except:
                                                                        if ('pNet' in syst and ('untag' in cat or ('Wtag' in syst and 'Tjet' in cat) or ('Ttag' in syst and 'Wjet' in cat))):
                                                                                pass
                                                                        else:
                                                                                print('could not process '+syst+' for '+bkg)

                        # uncorr years
                        if doAllSys:
                                for syst in uncorrList:
                                        for shiftyear in yearList:
                                                systHistsWrite[f'{histoPrefix}__{proc}__{syst}{shiftyear}Up'] = systHists[f'{histoPrefix}__{proc}__{syst}{shiftyear}Up'].Clone()
                                                systHistsWrite[f'{histoPrefix}__{proc}__{syst}{shiftyear}Down'] = systHists[f'{histoPrefix}__{proc}__{syst}{shiftyear}Down'].Clone()
                                                for nomyear in yearList:
                                                        if nomyear!=shiftyear:
                                                                systHistsWrite[f'{histoPrefix}__{proc}__{syst}{shiftyear}Up'].Add(nomHists[f'{histoPrefix}__{proc}{nomyear}'])
                                                                systHistsWrite[f'{histoPrefix}__{proc}__{syst}{shiftyear}Down'].Add(nomHists[f'{histoPrefix}__{proc}{nomyear}'])

                        outHistFile.cd()
                        nomHistAllYears.Write()
                        for systHist in systHistsWrite:
                                systHistsWrite[systHist].Write()
                        bkgHistFile.Close()

                sigHistFile = TFile.Open(f'{outDir}{cat[2:]}/sighists_{iPlot}.root', "READ")
                systematicList = mySystList
                for mass in massList:
                        systHists = {}
                        # add nominal and correlated systs
                        nomHistsAllYears = sigHistFile.Get(f'{histoPrefix}_Bprime_M{mass}_{yearList[0]}').Clone(histoPrefix+'__BpM'+str(mass))
                        if doAllSys:
                                for syst in corrList_sf:
                                        if 'pdf' in syst:
                                                systHists[f'{histoPrefix}__BpM{mass}__{syst}'] = sigHistFile.Get(f'{histoPrefix}_{syst}_Bprime_M{mass}_{yearList[0]}').Clone(f'{histoPrefix}__BpM{mass}__{syst}')
                                        else:
                                                try:
                                                        systHists[f'{histoPrefix}__BpM{mass}__{syst}Up'] = sigHistFile.Get(f'{histoPrefix}_{syst}Up_Bprime_M{mass}_{yearList[0]}').Clone(f'{histoPrefix}__BpM{mass}__{syst}Up')
                                                        systHists[f'{histoPrefix}__BpM{mass}__{syst}Down'] = sigHistFile.Get(f'{histoPrefix}_{syst}Dn_Bprime_M{mass}_{yearList[0]}').Clone(f'{histoPrefix}__BpM{mass}__{syst}Down')
                                                except:
                                                        if ('pNet' in syst and ('untag' in cat or ('Wtag' in syst and 'Tjet' in cat) or ('Ttag' in syst and 'Wjet' in cat))):
                                                                pass
                                                        else:
                                                                print('could not process '+syst+' for '+bkg)

                        for year in yearList:
                                if year == yearList[0]: continue
                                print('Trying to add',f'{histoPrefix}_Bprime_M{mass}_{year}')
                                nomHistsAllYears.Add(sigHistFile.Get(f'{histoPrefix}_Bprime_M{mass}_{year}'))
                                if doAllSys:
                                        for syst in corrList_sf:
                                                if 'pdf' in syst:
                                                        systHists[f'{histoPrefix}__BpM{mass}__{syst}'].Add(sigHistFile.Get(f'{histoPrefix}_{syst}_Bprime_M{mass}_{year}'))
                                                else:
                                                        try:
                                                                systHists[f'{histoPrefix}__BpM{mass}__{syst}Up'].Add(sigHistFile.Get(f'{histoPrefix}_{syst}Up_Bprime_M{mass}_{year}'))
                                                                systHists[f'{histoPrefix}__BpM{mass}__{syst}Down'].Add(sigHistFile.Get(f'{histoPrefix}_{syst}Dn_Bprime_M{mass}_{year}'))
                                                        except:
                                                                if ('pNet' in syst and ('untag' in cat or ('Wtag' in syst and 'Tjet' in cat) or ('Ttag' in syst and 'Wjet' in cat))):
                                                                        pass
                                                                else:
                                                                        print('could not process '+syst+' for '+bkg)

                        # make hists for uncorrleated systs
                        if doAllSys:
                                for syst in uncorrList_sf:
                                        for shiftyear in yearList:
                                                systHists[f'{histoPrefix}__BpM{mass}__{syst}{shiftyear}Up'] = sigHistFile.Get(f'{histoPrefix}_{syst}Up_Bprime_M{mass}_{shiftyear}').Clone(f'{histoPrefix}__BpM{mass}__{syst}{shiftyear}Up')
                                                systHists[f'{histoPrefix}__BpM{mass}__{syst}{shiftyear}Down'] = sigHistFile.Get(f'{histoPrefix}_{syst}Dn_Bprime_M{mass}_{shiftyear}').Clone(f'{histoPrefix}__BpM{mass}__{syst}{shiftyear}Down')
                                                for year in yearList:
                                                        if year!=shiftyear:
                                                                systHists[f'{histoPrefix}__BpM{mass}__{syst}{shiftyear}Up'].Add(sigHistFile.Get(f'{histoPrefix}_Bprime_M{mass}_{year}'))
                                                                systHists[f'{histoPrefix}__BpM{mass}__{syst}{shiftyear}Down'].Add(sigHistFile.Get(f'{histoPrefix}_Bprime_M{mass}_{year}'))

                        outHistFile.cd()
                        nomHistsAllYears.Write()
                        for systHist in systHists:
                                systHists[systHist].Write()
                sigHistFile.Close()
        outHistFile.Close()

# ###################
# ### Yield Table ###
# ###################
# # Does not record data yield. Update if needed. Sample code in doTemplates_RDF.py

if not getYields:
        exit()
        
yieldTable = {}
yieldStatErrTable = {}

systListFullUCOC = corrList_sf.copy()
for syst in uncorrList_sf:
        for year in yearList:
                systListFullUCOC.append(f'{syst}{year}')

combinedHistFile = TFile.Open(f'{outDir}templates_{iPlot}_{lumiStr}.root', "READ")

# Initialize empty yields dictionaries for table printing
for cat in catList:
        if region=="all":
                histoPrefix = f'{iPlot}_{lumiStr}_{cat}'
        else:
                histoPrefix = f'{iPlot}_{lumiStr}_{cat}_{region}'        
        yieldTable[histoPrefix]={}
        yieldStatErrTable[histoPrefix]={}

        lastBin = combinedHistFile.Get(f'{histoPrefix}__ewk').GetXaxis().GetNbins()+1
        binerr = ctypes.c_double()
        
        yieldTable[histoPrefix]['data'] = combinedHistFile.Get(f'{histoPrefix}__data_obs').IntegralAndError(1,lastBin,binerr,"")
        yieldStatErrTable[histoPrefix]['data'] = binerr.value
        
        for sig in sigList:
                yieldTable[histoPrefix][sig] = combinedHistFile.Get(f'{histoPrefix}__{sig}').IntegralAndError(1,lastBin,binerr,"")
                yieldStatErrTable[histoPrefix][sig] = binerr.value
        
        yieldTable[histoPrefix]['totBkg'] = 0.
        yieldStatErrTable[histoPrefix]['totBkg'] = 0.
        for proc in bkgProcs:
                yieldTable[histoPrefix][proc] = combinedHistFile.Get(f'{histoPrefix}__{proc}').IntegralAndError(1,lastBin,binerr,"")
                yieldStatErrTable[histoPrefix][proc] = binerr.value
                yieldTable[histoPrefix]['totBkg'] += yieldTable[histoPrefix][proc]
                yieldStatErrTable[histoPrefix]['totBkg'] += binerr.value**2
        yieldStatErrTable[histoPrefix]['totBkg'] = math.sqrt(yieldStatErrTable[histoPrefix]['totBkg'])

        yieldTable[histoPrefix]['dataOverBkg'] = yieldTable[histoPrefix]['data']/yieldTable[histoPrefix]['totBkg']
        yieldStatErrTable[histoPrefix]['dataOverBkg'] = yieldStatErrTable[histoPrefix]['data']/yieldStatErrTable[histoPrefix]['totBkg']

        if doAllSys:
                for syst in systListFullUCOC:
                        if 'pdf' in syst or syst == 'muR' or syst == 'muF': continue
                        for ud in ['Up', 'Down']:
                                yieldTable[f'{histoPrefix}{syst}{ud}']={}
                for proc in list(bkgProcs.keys())+sigList:
                        systematicList = systListFullUCOC
                                
                        for syst in systematicList:
                                if 'pdf' in syst or syst == 'muR' or syst == 'muF': continue
                                for ud in ['Up', 'Down']:
                                        try:
                                                yieldTable[f'{histoPrefix}{syst}{ud}'][proc]=combinedHistFile.Get(f'{histoPrefix}__{proc}__{syst}{ud}').Integral()
                                        except:
                                                if ('pNet' in syst and ('untag' in cat or ('Wtag' in syst and 'Tjet' in cat) or ('Ttag' in syst and 'Wjet' in cat))):
                                                        yieldTable[f'{histoPrefix}{syst}{ud}'][proc] = 0
                                                else:
                                                        print('could not store integral of '+syst+' for '+proc)


table = []
table.append(['break'])
table.append(['break'])
table.append(['YIELDS']+[proc for proc in list(bkgProcs.keys())+['data']])

# yields for bkg and data
for cat in catList:
        row = [cat]
        if region=="all":
                histoPrefix = f'{iPlot}_{lumiStr}_{cat}'
        else:
                histoPrefix = f'{iPlot}_{lumiStr}_{cat}_{region}'
        for proc in list(bkgProcs.keys())+['data']:
                row.append(str(round(yieldTable[histoPrefix][proc],3))+' $\pm$ '+str(round(yieldStatErrTable[histoPrefix][proc],3)))
        table.append(row)
table.append(['break'])
table.append(['break'])

table.append(['YIELDS']+sigList)
# yields for signals
for cat in catList:
        row = [cat]
        if region == "all":
                histoPrefix = f'{iPlot}_{lumiStr}_{cat}'
        else:
                histoPrefix = f'{iPlot}_{lumiStr}_{cat}_{region}'
        for proc in sigList:
                row.append(str(round(yieldTable[histoPrefix][proc],3))+' $\pm$ '+str(round(yieldStatErrTable[histoPrefix][proc],3)))
        table.append(row)

# yields for AN tables
for isEM in isEMlist:
        corrdSys = lumiSys  # maybe additional later?
        table.append(['break'])
        table.append(['','is'+isEM+'_yields'])
        table.append(['break'])
        #table.append(['YIELDS']+[cat for cat in catList if 'is'+isEM in cat]+['\\\\'])
        table.append(['YIELDS']+catList+['\\\\'])
        for proc in list(bkgProcs.keys())+['totBkg','data','dataOverBkg']+sigList:
                row = [proc]
                for cat in catList:
                        if not ('is'+isEM in cat): continue
                        if region=="all":
                                histoPrefix = f'{iPlot}_{lumiStr}_{cat}'
                        else:
                                histoPrefix = f'{iPlot}_{lumiStr}_{cat}_{region}'
                        if proc=='data': 
                                row.append(' & '+str(int(yieldTable[histoPrefix][proc])))
                        else:
                                #row.append(' & '+str(round_sig(yieldTable[histoPrefix][proc],5))+' $\pm$ '+str(round_sig(yieldStatErrTable[histoPrefix][proc],2)))
                                row.append(' & '+str(round(yieldTable[histoPrefix][proc],2))+' $\pm$ '+str(round(yieldStatErrTable[histoPrefix][proc],2)))
                row.append('\\\\')
                table.append(row)

# TODO: yields for PAS tables (yields in e/m channels combined)
# skip for now

# systematics
if doAllSys:
        table.append(['break'])
        table.append(['','Systematics'])
        table.append(['break'])
        for proc in list(bkgProcs.keys())+sigList:
                table.append([proc]+[cat for cat in catList]+['\\\\'])
                for syst in systListFullUCOC:
                        if 'pdf' in syst or syst == 'muR' or syst == 'muF': continue
                        for ud in ['Up', 'Down']:
                                row = [syst+ud]
                                for cat in catList:
                                        if region=="all":
                                                histoPrefix = f'{iPlot}_{lumiStr}_{cat}'
                                        else:
                                                histoPrefix = f'{iPlot}_{lumiStr}_{cat}_{region}'
                                        nomHist = histoPrefix
                                        shpHist = f'{histoPrefix}{syst}{ud}'
                                        try:
                                                row.append(' & '+str(round(yieldTable[shpHist][proc]/(yieldTable[nomHist][proc]+1e-20),2)))
                                        except:
                                                pass
                                row.append('\\\\')
                                table.append(row)
                table.append(['break'])
#print(table)
#exit()       

tabFile = f'{outDir}yields_{iPlot}_{lumiStr}.txt'
#if year != 'all': tabFile = outDir+'/yields_'+discriminant+'_'+year+'.txt'
out=open(tabFile,'w')
printTable(table,out)
