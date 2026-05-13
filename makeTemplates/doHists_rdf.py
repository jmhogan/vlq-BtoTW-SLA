#!/usr/bin/python

# python3 -u doHists_rdf.py test BpMassAve 4lep 0 L
# python3 -u doHists_rdf.py testtest VLQCosDecayAngleAve all 0 L
# python3 -u doHists_rdf.py
# optional arguments:
#    argv1: outDir (default cwd)
#    argv2: iPlot (discriminant from plotList. default 'HT')
#    argv3: region (divide into ABCDnn regions. takes 'A', 'B', ..., 'all'. default 'all')
#    argv4: isCategorized (divide into decay modes. takes integer values 0 or 1 (True). default '0' (False))
#    argv5: isEMlist (default 'E')
#    argv6: taglist (default 'all')

# Outputs .p files containing a dictionary of histograms

import os,sys,time,math,datetime,pickle,itertools,getopt
from ROOT import TH1D,gROOT,TFile,TTree,gDirectory
parent = os.path.dirname(os.getcwd())
sys.path.append(parent)
from numpy import linspace

from analyze_RDF import *
from samples import samples_electroweak, samples_electroweak3, samples_electroweak4, samples_wjets, samples_singletop, samples_ttbarx, samples_ttbarx3, samples_ttbarx4, samples_qcd, samples_data, samples_signal, samples_ttbar, samples_nonprompt
from utils import *

gROOT.SetBatch(1)
start_time = time.time()

# ------------- File location and total lumi ---------------
step1Dir = 'root://cmseos.fnal.gov//store/user/lpchtop/BBto2b4tau_Feb2026_Run3/'

# ------------- Arguments and default values ------------
iPlot = 'BpMassAve' #choose a discriminant from plotList below!
if len(sys.argv)>2: iPlot=sys.argv[2]

region = '3lep'
if len(sys.argv)>3: region=sys.argv[3]

isCategorized = False
if len(sys.argv)>4: isCategorized=int(sys.argv[4])

doABCDnn = False
doJetRwt= 0
doAllSys= False
cTime=datetime.datetime.now()
datestr='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
timestr='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)
pfix='templatesTest'+region
if not isCategorized: pfix='kinematics'+region
print('Set pfix to '+pfix)

# -------------- Groups of background samples to use --------------

doData = True
doSigs = True
doBkgs = True

# this is a list of group dictionaries. "wjets" has entries like "WJetsHT2002018":WJetsHT2002018, where the 2nd is the class
bkgList = {"ewk"      : samples_electroweak,           
           "ttx"      : samples_ttbarx,
           "wjets"    : samples_wjets,
           "ttbar"    : samples_ttbar,
           "singletop": samples_singletop,
}
if region == '3lep':
        bkgList = {"ewk"      : samples_electroweak3,           
                   "ttx"      : samples_ttbarx3,
                   "np"       : samples_nonprompt,
                   }
elif region == '4lep':
        bkgList = {"ewk"      : samples_electroweak4,           
                   "ttx"      : samples_ttbarx4,
                   "np"       : samples_nonprompt,
                   }

### TO-DO: in samples.py, make up an entry for each year for ABCDnn with dummy information where needed.
### When iPlot == a transform variable, bkgList = [samples_electroweak,samples_ttbarx,samples_abcdnn] (singletop?)

# use "samples_data" and "samples_signal" below for the dictionaries of data and signals

# ------------- Parameters to divide up the histograms --------------

if len(sys.argv)>5: isEMlist=[str(sys.argv[5])]
else:
        isEMlist = ['L']
if len(sys.argv)>6: taglist=[str(sys.argv[6])]
else: 
	taglist = ['all']
	if isCategorized: 
                #taglist=['tagTjet','tagWjet','untagTlep','untagWlep']
                #taglist=['tagTjet','tagWjet','untagTlep','untagWlep','allWlep','allTlep']
                taglist=['all'] # TEMP

# ------------- Definition of plots to make ------------------
### TO-DO: add ABCDnn branches
plotList = {#discriminantName:(discriminantLJMETName, binning, xAxisLabel)
        'NPV'   :('PV_npvs',linspace(0,80,81).tolist(),';N PVs'),
        'Nleps' :('NgoodLeptons',linspace(0,5,5).tolist(),';N good leptons'),
        'lepPt' :('Good4Lepton_pt',linspace(0, 300, 51).tolist(),';lepton p_{T} [GeV]'),
        'lepEta':('Good4Lepton_eta',linspace(-2.5, 2.5, 51).tolist(),';lepton #eta'),
        'lepPhi':('Good4Lepton_phi',linspace(-3.2,3.2,65).tolist(),';lepton #phi'),
        'lepID':('Good4Lepton_ID',linspace(10,16,7).tolist(),';lepton flavor'),
        'lepCharge':('Good4Lepton_charge',linspace(-2,2,5).tolist(),';lepton charge'),
        'lepChargeSum':('Sum(Good4Lepton_charge)',linspace(-5,5,11).tolist(),';lepton charge sum'),
        'MET'   :('corrMET_pt',linspace(0, 1000, 51).tolist(),';PUPPI #slash{E}_{T} [GeV]'),
        'METphi':('corrMET_phi',linspace(-3.2,3.2, 65).tolist(),';PUPPI #slash{E}_{T} phi'),
        'HT':('gcJet_ht',linspace(0, 2500, 51).tolist(),';H_{T} (GeV)'),
        'ST':('gcJet_ST',linspace(0, 5000, 51).tolist(),';S_{T} (GeV)'),
        'JetEta':('gcJet_eta',linspace(-3, 3, 41).tolist(),';central AK4 jet #eta'),
        'JetPt' :('gcJet_pt',linspace(0, 400, 51).tolist(),';central AK4 jet p_{T} [GeV]'),
        'JetPhi':('gcJet_phi',linspace(-3.2,3.2, 65).tolist(),';central AK4 jet phi'),
        'JetBtag':('gcJet_PNet',linspace(0,1,51).tolist(),';central AK4 jet DeepJet disc'),
        'NJets' :('NgoodcleanJets',linspace(0, 10, 11).tolist(),';central AK4 jet multiplicity'),
        'NBJets':('NJets_PNetL',linspace(0, 10, 11).tolist(),';ParticleNet b-tag loose multiplicity'),
        'BpMassAve':('0.5*(B1finalM+B2finalM)',linspace(0,1000,51).tolist(),';Average B quark mass (manual) [GeV]'),
        'BpMassDiff':('abs(B1finalM-B2finalM)',linspace(0,1800,31).tolist(),';Difference in B quark masses [GeV]'),
        'BpMass1':('B1finalM',linspace(0,1800,31).tolist(),';B quark 1 mass [GeV]'),
        'BpMass2':('B2finalM',linspace(0,1800,31).tolist(),';B quark 2 mass [GeV]'),
        'VLQBBbarMass':('VLQ_BBbar_mass',linspace(0,10000,51).tolist(),';B#bar{B} mass [GeV]'),
        'VLQBBbarCosDecayAngle':('VLQ_BBbar_cosDecayAngle',linspace(-1.6,1.6,65).tolist(),';B#bar{B} Cos Decay Angle'),
        'VLQBBbarDeltaPhiDecayAngle':('VLQ_BBbar_deltaPhiDecayAngle',linspace(0,3.2,65).tolist(),';B#bar{B} Delta Decay #phi'),
        'VLQBbarMass':('VLQ_Bbar_mass',linspace(0,5000,51).tolist(),';#bar{B} quark mass [GeV]'),
        'VLQBbarCosDecayAngle':('VLQ_Bbar_cosDecayAngle',linspace(-1.6,1.6,65).tolist(),';#bar{B} Cos Decay Angle'),
        'VLQBbarDeltaPhiDecayAngle':('VLQ_Bbar_deltaPhiDecayAngle',linspace(0,3.2,65).tolist(),';#bar{B} Delta #phi'),
        'VLQBMass':('VLQ_B_mass',linspace(0,5000,51).tolist(),';B quark mass [GeV]'),
        'VLQBCosDecayAngle':('VLQ_B_cosDecayAngle',linspace(-1.6,1.6,65).tolist(),';B Cos#theta'),
        'VLQBDeltaPhiDecayAngle':('VLQ_B_deltaPhiDecayAngle',linspace(0,3.2,65).tolist(),';B Delta #phi'),
        'VLQtau11Mass':('VLQ_tau11_mass',linspace(0,700,51).tolist(),';#tau_{11} mass [GeV]'),
        'VLQtau12Mass':('VLQ_tau12_mass',linspace(0,700,51).tolist(),';#tau_{12} mass [GeV]'),
        'VLQtau21Mass':('VLQ_tau21_mass',linspace(0,700,51).tolist(),';#tau_{21} mass [GeV]'),
        'VLQtau22Mass':('VLQ_tau22_mass',linspace(0,700,51).tolist(),';#tau_{22} mass [GeV]'),
        'VLQBBbarDeltaPhiVisible':('VLQ_BBbar_DeltaPhiVisible',linspace(0,3.2,65).tolist(),';B#bar{B} Delta #phi Visible'),
        'VLQBBbarDeltaPhiDecayVisible':('VLQ_BBbar_DeltaPhiDecayVisible',linspace(0,3.2,65).tolist(),';B#bar{B} Delta #phi Decay Visible'),
        'VLQBBbarDeltaPhiBoostVisible':('VLQ_BBbar_DeltaPhiBoostVisible',linspace(0,3.2,65).tolist(),';B#bar{B} Delta #phi Boost Visible'),
        'VLQBBbarVisibleShape':('VLQ_BBbar_VisibleShape',linspace(0,1,51).tolist(),';B#bar{B} Visible Shape'),
        'VLQMassAve':('0.5*(VLQ_B_mass+VLQ_Bbar_mass)',linspace(0,2000,51).tolist(),';Ave(B,#bar{B}) quark mass (RJR) [GeV]'),
        'VLQCosDecayAngleAve':('0.5*(VLQ_B_cosDecayAngle+VLQ_Bbar_cosDecayAngle)',linspace(-1,1,51).tolist(),';Avg(B,#bar{B}) cos#theta'),
        'VLQDeltaPhiDecayAngleAve':('0.5*(VLQ_B_deltaPhiDecayAngle+VLQ_Bbar_deltaPhiDecayAngle)',linspace(0,3.2,65).tolist(),';Avg(B,#bar{B}) Delta #phi'),
}

print( "PLOTTING: "+iPlot)
print( "         LJMET Variable: "+plotList[iPlot][0])
print( "         X-AXIS TITLE  : "+plotList[iPlot][2])
print( "         BINNING USED  : "+str(plotList[iPlot][1]))

shapesFiles = []#'JEC','JER']
tTreeData = {}
tTreeSig = {}
tTreeBkg = {}

catList = list(itertools.product(isEMlist,taglist))
print('Cat list: '+str(catList))
nCats  = len(catList)
catInd = 1

for cat in catList:
        print('==================== Category: '+str(cat)+' ======================')
        catDir = cat[0]+'_'+cat[1]

        if len(sys.argv)>1:
                outDir=sys.argv[1]
                sys.path.append(outDir)
        else:
                outDir = os.getcwd()+'/'+pfix+'/'+catDir
        if not os.path.exists(outDir): os.system('mkdir -p '+outDir)

        category = {'isEM':cat[0],'tag':cat[1]} # THINK: is this necessary?

        print(f'Running analyze! Storing in outDir = {outDir}')

        if doData:
                dataHistFile = TFile.Open(f'{outDir}/datahists_{iPlot}.root', "RECREATE")
                #for i in samples_data.keys():
                #    print(f'Samples_data: {samples_data[i].samplename}')

                for data in samples_data.keys(): # "data" is the class 
                        print('------------ '+data+' -------------')
                        #SingleMuonRun2022EEF  = sample("SingleMuonRun2022EEF", 1.0, "2022EE", "SingleMuonRun2022EEF2022EENanoList.txt", "/Muon/Run2022F-22Sep2023-v2/NANOAOD")
                        #SingleElecRun2023C13  = sample("SingleElecRun2023C13", 1.0, "2023", "SingleElecRun2023C132023NanoList.txt", "/EGamma1/Run2023C-22Sep2023_v3-v1/NANOAOD")
                        
                        #print('START FP\n\tBuilding File Prefix')
                        #print(f'\tData: {data}')
                        #print(f'\tSample Name: {samples_data[data].samplename}')
                        fileprefix = (samples_data[data].samplename).split('/')[1]+((samples_data[data].samplename).split('/')[2])[7]
                        if (((samples_data[data].samplename).split('/')[2]).split('-')[1])[-2] == 'v':
                                fileprefix += (((samples_data[data].samplename).split('/')[2]).split('-')[1])[-2:]
                        else:
                                fileprefix += '22'
                        #print('DONE FP')

                        #print("START TD\n\tBuilding Tree Data")
                        #print(f'\tFile Prefix: {fileprefix}')
                        #print(f'\tSampels Data: {samples_data[data].year}')
                        #print(f'\tStep 1 Dir: {step1Dir}')
                        tTreeData[data]=readTreeNominal(fileprefix,samples_data[data].year,step1Dir) ## located in utils.py
                        #print("DONE TD")
                        ### For analyze_RDF make the switch here (and similar regions below)
                        #dataHistFile.cd()
                        analyze(tTreeData,samples_data[data],False,iPlot,plotList[iPlot],category,region,isCategorized,dataHistFile, False)
                        if catInd==nCats: 
                                print('deleting '+data)
                                del tTreeData[data]
                dataHistFile.Close()

        if doBkgs:
                ### Now we begin the same general process but for simulated backgrounds
                for proc in bkgList:
                        bkgHistFile = TFile.Open(f'{outDir}/bkghists_{proc}_{iPlot}.root', "RECREATE")
                        bkgGrp = bkgList[proc]

                        if proc == "np":
                                for bkg in bkgGrp:
                                        print('------------ '+bkg+' -------------')
                                        fileprefix = 'Nonprompt'+(bkgGrp[bkg].samplename).split('/')[1]+((bkgGrp[bkg].samplename).split('/')[2])[7]
                                        if (((bkgGrp[bkg].samplename).split('/')[2]).split('-')[1])[-2] == 'v':
                                                fileprefix += (((bkgGrp[bkg].samplename).split('/')[2]).split('-')[1])[-2:]
                                        else:
                                                fileprefix += '22'
                                        tTreeBkg[bkg]=readTreeNominal(fileprefix,bkgGrp[bkg].year,step1Dir) ## located in utils.py
                                        analyze(tTreeBkg,bkgGrp[bkg],False,iPlot,plotList[iPlot],category,region,isCategorized,bkgHistFile, False)
                                        if catInd==nCats: 
                                                print('deleting '+bkg)
                                                del tTreeBkg[bkg]
                                
                        else:
                                for bkg in bkgGrp:
                                        print('------------ '+bkg+' -------------')
                                        fileprefix = (bkgGrp[bkg].samplename).split('/')[1]
                                        tTreeBkg[bkg]=readTreeNominal(fileprefix,bkgGrp[bkg].year,step1Dir)
                                        if doAllSys and not doABCDnn:
                                                for syst in shapesFiles:
                                                        for ud in ['up','dn']: # TODO: can be optimized
                                                                print(f'        {syst}{ud}')
                                                                tTreeBkg[bkg+syst+ud]=readTreeShift(fileprefix,bkgGrp[bkg].year,f'{syst}{ud}',step1Dir) ## located in utils.py
                                        analyze(tTreeBkg,bkgGrp[bkg],doAllSys,iPlot,plotList[iPlot],category,region,isCategorized, bkgHistFile, doABCDnn)
                                        if catInd==nCats:
                                                print('deleting '+bkg)
                                                del tTreeBkg[bkg]
                                                if doAllSys and not doABCDnn:
                                                        for syst in shapesFiles:
                                                                for ud in ['up','dn']: del tTreeBkg[bkg+syst+ud]
                        bkgHistFile.Close()
        
        if doSigs:
                sigHistFile = TFile.Open(f'{outDir}/sighists_{iPlot}.root', "RECREATE")
                for sig in samples_signal.keys(): 
                        print('------------- '+sig+' ------------')
                        fileprefix = (samples_signal[sig].samplename).split('/')[1]
                        tTreeSig[sig]=readTreeNominal(fileprefix,samples_signal[sig].year,step1Dir)
                        if doAllSys:
                                for syst in shapesFiles:
                                        for ud in ['up','dn']:
                                                print(f'        {syst}{ud}')
                                                tTreeSig[sig+syst+ud]=readTreeShift(fileprefix,samples_signal[sig].year,f'{syst}{ud}',step1Dir)
                        #sigHistFile.cd()
                        analyze(tTreeSig,samples_signal[sig],doAllSys,iPlot,plotList[iPlot],category,region,isCategorized, sigHistFile, False)
                        if catInd==nCats: 
                                print('deleting '+sig)
                                del tTreeSig[sig]
                                if doAllSys:
                                        for syst in shapesFiles:
                                                for ud in ['up','dn']: del tTreeSig[sig+syst+ud]
                sigHistFile.Close()

        catInd+=1

### Deals with overflow and negBinCorrection
for cat in catList:
        catDir = cat[0]+'_'+cat[1]
        if len(sys.argv)>1:
                outDir=sys.argv[1]
                sys.path.append(outDir)
        else:   
                outDir = os.getcwd()+'/'+pfix+'/'+catDir
        print(f'Formatting histograms in {outDir}')

        if doData:
                dataHistFile = TFile.Open(f'{outDir}/datahists_{iPlot}.root', "UPDATE")
                for key in gDirectory.GetListOfKeys():
                        hist = key.ReadObj()
                        try:
                                overflow(hist) # this function puts overflow into the last column
                                hist.Write()
                        except:
                                hist.Print()
                dataHistFile.Close()

        if doBkgs:
                for bkgGrp in bkgList:
                        bkgHistFile = TFile.Open(f'{outDir}/bkghists_{bkgGrp}_{iPlot}.root', "UPDATE")
                        for key in gDirectory.GetListOfKeys():
                                hist = key.ReadObj()
                                negBinCorrection(hist)
                                overflow(hist)
                                hist.Write()
                        bkgHistFile.Close()

        if doSigs:
                sigHistFile = TFile.Open(f'{outDir}/sighists_{iPlot}.root', "UPDATE")
                for key in gDirectory.GetListOfKeys():
                        hist = key.ReadObj()
                        negBinCorrection(hist)
                        overflow(hist)
                        hist.Write()
                sigHistFile.Close()
        

print("--- %s minutes ---" % (round((time.time() - start_time)/60,2)))
