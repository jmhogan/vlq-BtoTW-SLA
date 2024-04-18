#!/usr/bin/python

import os,sys,time,math,datetime,itertools
from ROOT import gROOT,TFile,TH1F, TH2D
parent = os.path.dirname(os.getcwd())
sys.path.append(parent)
from samples import targetlumi, lumiStr, systListFull, samples_data, samples_signal, samples_electroweak, samples_wjets, samples_singletop, samples_ttbarx, samples_qcd, samples_ttbar, samples_ttbar_abcdnn
from utils import *

gROOT.SetBatch(1)
start_time = time.time()

region='all' # BAX, DCY, individuals, or all
if len(sys.argv)>1: region = str(sys.argv[1])

isCategorized=False
year='all' # all

pfix='templates'+region
if not isCategorized: pfix='kinematics'+region
pfix+='_Oct2023SysAll'
#pfix = 'templatesTestA' # TEMP
outDir = os.getcwd()+'/'+pfix+'/'

removeThreshold = 0.0005 # TODO: add if necessary

scaleSignalXsecTo1pb = False # Set to True if analyze.py ever uses a non-1 cross section
doAllSys = True # TEMP
doPDF = False
if isCategorized: doPDF=False # FIXME later

bkgProcs = {'ewk':samples_electroweak,'wjets':samples_wjets,'ttbar':samples_ttbar,'singletop':samples_singletop,'ttx':samples_ttbarx,'qcd':samples_qcd}
massList = [800,1000,1200,1300,1400,1500,1600,1700,1800,2000,2200]
sigList = ['BpM'+str(mass) for mass in massList]

isEMlist = ['L'] #['E','M'], 'L' #
if '2D' in outDir: 
        isEMlist =['L']
taglist = ['all']
if isCategorized: 
        #taglist=['tagTjet','tagWjet','untagTlep','untagWlep','allWlep','allTlep']
        #taglist=['allWlep','allTlep']
        taglist=['allWlep']
        #taglist=['tagTjet','tagWjet','untagTlep','untagWlep']
        
catList = ['is'+item[0]+'_'+item[1] for item in list(itertools.product(isEMlist,taglist))]

lumiSys = 0.018 #lumi uncertainty

groupHists = True

plotList = ['ST',
            'BpMass',
            'HT',
            'lepPt',
            'lepEta',
            'lepPhi',
            'lepIso',
            'MET',
            'METphi',
            'JetEta',
            'JetPt'
            'JetPhi',
            'JetBtag',
            'ForwJetEta',
            'ForwJetPt' ,
            'ForwJetPhi',
            'FatJetEta',
            'FatJetPt' ,
            'FatJetPhi',
            'FatJetSD' ,
            'FatJetMatch',
            'OS1FatJetEta',
            'OS1FatJetPt' ,
            'OS1FatJetPhi',
            'OS1FatJetSD' ,
            'NJetsCentral' ,
            'NJetsForward' ,
            'NBJets',
            'NOSJets',
            'NSSJets',
            'NOSBJets',
            'NSSBJets',
            'NFatJets',
            'NOSFatJets',
            'NSSFatJets',
            'minDR_twoAK8s',
            'minDR_twoAK4s',
            'PtRel',
            'PtRelAK8',
            'minDR',
            'minDRAK8',
            'FatJetTau21'  ,
            'FatJetTau32'  ,
            'OS1FatJetTau21'  ,
            'OS1FatJetTau32'  ,
            'FatJetProbJ',
            'FatJetProbT',
            'FatJetProbW',
            'FatJetProbTvJ',
            'FatJetProbWvJ',
            'FatJetTag',
            'OS1FatJetProbJ',
            'OS1FatJetProbT',
            'OS1FatJetProbW',
            'OS1FatJetProbTvJ',
            'OS1FatJetProbWvJ',
            'OS1FatJetTag',
            'nT',
            'nW',
            'Wmass',
            'Wpt',
            'Weta',
            'Wphi',
            'WMt',
            'Wdrlep',
            'minMlj',
            'tmassMLJ',
            'tptMLJ',
            'tetaMLJ',
            'tphiMLJ',
            'tmassSSB',
            'tptSSB',
            'tetaSSB',
            'tphiSSB',
            'tdrWbMLJ',
            'tdrWbSSB',
            'BpPt',
            'BpEta',
            'BpPhi',
            'BpDeltaR',
            'BpPtBal',
            'BpChi2',
            'BpDecay',
            # 'BpMass_ABCDnn',
            # 'ST_ABCDnn'
]

#iPlot = "BpMass"
iPlot = "OS1FatJetProbJ"

doABCDnn = False
if "ABCDnn" in iPlot:
        doABCDnn = True

### Group histograms
### TODO: add Up and Dn
### TODO: ABCDnn
if groupHists:
        outHistFile = TFile.Open(f'{outDir}templates_{iPlot}_{lumiStr}.root', "RECREATE")
        for cat in catList:
                histoPrefix = f'{iPlot}_{lumiStr}_{cat}'

                dataHistFile = TFile.Open(f'{outDir}{cat[2:]}/datahists_{iPlot}.root', "READ")
                isFirstHist = True
                for dat in samples_data:
                        if isFirstHist:
                                hists = dataHistFile.Get(histoPrefix+'_'+samples_data[dat].prefix).Clone(histoPrefix+'__data_obs')
                                isFirstHist = False
                        else:
                                hists.Add(dataHistFile.Get(histoPrefix+'_'+samples_data[dat].prefix))
                outHistFile.cd()
                hists.Write()
                dataHistFile.Close()

                #systHists = {}
                for proc in bkgProcs:
                        # DID NOT IMPLEMENT REMOVETHRESHOLD
                        bkgHistFile = TFile.Open(f'{outDir}{cat[2:]}/bkghists_{proc}_{iPlot}.root', "READ")
                        print(f'{outDir}{cat[2:]}/bkghists_{proc}_{iPlot}.root')
                        bkgGrp = bkgProcs[proc]
                        systHists = {}
                        isFirstHist = True
                        for bkg in bkgGrp:
                                if 'QCDHT300' in bkg:
                                        print("Plotting without QCDHT300.")
                                        continue
                                if isFirstHist:
                                        hists = bkgHistFile.Get(histoPrefix+'_'+bkgGrp[bkg].prefix).Clone(histoPrefix+'__'+proc)
                                        isFirstHist = False
                                        if doAllSys:
                                                if doABCDnn: #TEMP #TODO
                                                        pass
                                                else:
                                                        for syst in systListFull:
                                                                print(f'{histoPrefix}_{syst}Up_{bkgGrp[bkg].prefix}')
                                                                systHists[f'{histoPrefix}__{proc}__{syst}__Up'] = bkgHistFile.Get(f'{histoPrefix}_{syst}Up_{bkgGrp[bkg].prefix}').Clone(f'{histoPrefix}__{proc}__{syst}__Up')
                                                                systHists[f'{histoPrefix}__{proc}__{syst}__Dn'] = bkgHistFile.Get(f'{histoPrefix}_{syst}Dn_{bkgGrp[bkg].prefix}').Clone(f'{histoPrefix}__{proc}__{syst}__Dn')
                                else:
                                        #print(bkgHistFile.Get(histoPrefix+'_'+bkgGrp[bkg].prefix))
                                        hists.Add(bkgHistFile.Get(histoPrefix+'_'+bkgGrp[bkg].prefix))
                                        if doAllSys:
                                                if doABCDnn:
                                                        pass
                                                else:
                                                        for syst in systListFull:
                                                                print(f'{histoPrefix}_{syst}Up_{bkgGrp[bkg].prefix}')
                                                                systHists[f'{histoPrefix}__{proc}__{syst}__Up'].Add(bkgHistFile.Get(f'{histoPrefix}_{syst}Up_{bkgGrp[bkg].prefix}').Clone(f'{histoPrefix}__{proc}__{syst}__Up'))
                                                                systHists[f'{histoPrefix}__{proc}__{syst}__Dn'].Add(bkgHistFile.Get(f'{histoPrefix}_{syst}Dn_{bkgGrp[bkg].prefix}').Clone(f'{histoPrefix}__{proc}__{syst}__Dn'))

                        outHistFile.cd()
                        hists.Write()
                        for systHist in systHists:
                                systHists[systHist].Write()
                        bkgHistFile.Close()

                sigHistFile = TFile.Open(f'{outDir}{cat[2:]}/sighists_{iPlot}.root', "READ")
                for mass in massList:
                        isFirstHist = True
                        for signal in samples_signal:
                                if f'Bprime_M{mass}' in signal:
                                        if isFirstHist:
                                                hists = sigHistFile.Get(histoPrefix+'_'+signal).Clone(histoPrefix+'__BpM'+str(mass))
                                                isFirstHist = False
                                        else:
                                                hists.Add(sigHistFile.Get(histoPrefix+'_'+signal))
                        outHistFile.cd()
                        hists.Write()
                sigHistFile.Close()

# ### Get yields
# Yieldtable = {}
# yieldStatErrTable = {}

# # Initialize empty yields dictionaries for table printing
# for cat in catList:
#         histoPrefix=discriminant+'_'+lumiStr+'_'+cat
#         yieldTable[histoPrefix]={}
#         yieldStatErrTable[histoPrefix]={}
#         if doAllSys:
#                 for syst in systematicList:
#                         for ud in ['Up','Dn']:
#                                 yieldTable[histoPrefix+syst+ud]={}

