#!/usr/bin/python
from ROOT import TH1D,TTree,TFile,RDataFrame,TH1,EnableImplicitMT,DisableImplicitMT
from array import array
from numpy import linspace
from samples import targetlumi, lumiStr
import math,time

TH1.SetDefaultSumw2(True)
EnableImplicitMT()

"""
--This function will make kinematic plots for a given distribution for electron, muon channels and their combination
--Check the cuts below to make sure those are the desired full set of cuts!
--The applied weights are defined in "weights.py". Also, the additional weights (SFs, 
negative MC weights, ets) applied below should be checked!
"""

def analyze(tTree,sample,doAllSys,iPlot,plotDetails,category,region,isCategorized, outHistFile, doABCDnn):
        start_time = time.time()
        plotTreeName=plotDetails[0]
        plotTreeNameTemp = plotDetails[0] #TEMP
        xbins=array('d', plotDetails[1])
        xAxisLabel=plotDetails[2]

        if iPlot == 'NPV' and 'Single' in sample.prefix:
                plotTreeName = 'PV_npvs'
        
        # Define categories
        isEM  = category['isEM']
        tag   = category['tag']
        catStr = 'is'+isEM+'_'+tag

        if isCategorized: catStr += '_'+region
        
	# Define weights
        topCorr     = '1'
        topCorrUp   = '1'
        topCorrDn   = '1'
        jetSFstr    = '1'
        jetSFstrUp  = '1'
        jetSFstrDn  = '1'
        if ('WJetsHT' in sample.prefix):
                jetSFstr   = 'gcHTCorr_WjetLHE[0]' # 
                jetSFstrUp = 'gcHTCorr_WjetLHE[1]' #
                jetSFstrDn = 'gcHTCorr_WjetLHE[2]' #
        if 'TTTo' in sample.prefix or 'TTMT' in sample.prefix:
                topCorr   = 'gcHTCorr_top[0]'
                topCorrUp = 'gcHTCorr_top[1]'
                topCorrDn = 'gcHTCorr_top[2]'

        weightStr = '1'
        doMuRF = True
        #if (sample.prefix).find('WW') == 0 or (sample.prefix).find('WZ') == 0 or (sample.prefix).find('ZZ') == 0:
        #        doMuRF = False
        
        if ('Single' not in sample.prefix and 'MuonEG' not in sample.prefix and 'Tau' not in sample.prefix): 
			# '+jetSFstr+' * '+topCorr+' * leptonIDSF[0] * leptonIsoSF[0] * leptonHLTSF[0] * puJetSF[0] * 
            weightStr += ' * PileupWeights[0] * elrecoSF[0] * elidSF[0] * muonidSF[0] * muonisoSF[0] * tauidVSeSF[0] * tauidVSmuSF[0] * tauidVSjetSF[0] * btagWeights[0] *'+str(targetlumi[sample.year]*sample.xsec/sample.nrun)+' * (genWeight/abs(genWeight))'
                        
            #if isCategorized:
            #        if tag=="tagTjet" or tag=="allWlep":
            #                weightStr += f' * gcFatJet_pnetweights[6]'
            #                weightpNetTtagUpStr = weightStr.replace('gcFatJet_pnetweights[6]', 'gcFatJet_pnetweights[7]')
            #                weightpNetTtagDnStr = weightStr.replace('gcFatJet_pnetweights[6]', 'gcFatJet_pnetweights[8]')
            #        elif tag=="tagWjet" or tag=="allTlep":                        
            #                weightStr += f' * gcFatJet_pnetweights[9]'
            #                weightpNetWtagUpStr = weightStr.replace('gcFatJet_pnetweights[9]', 'gcFatJet_pnetweights[10]')
            #                weightpNetWtagDnStr = weightStr.replace('gcFatJet_pnetweights[9]', 'gcFatJet_pnetweights[11]')

            #weightPrefireUpStr = weightStr.replace('PreFiringWeight_Nom','PreFiringWeight_Up')
            #weightPrefireDnStr = weightStr.replace('PreFiringWeight_Nom','PreFiringWeight_Dn')                        
                        
            # Reco has the main value in [0], up in [1], down in [2]. Up/Down are not additive on [0]

            weightPileupUpStr   = weightStr.replace('PileupWeights[0]','PileupWeights[1]')
            weightPileupDnStr   = weightStr.replace('PileupWeights[0]','PileupWeights[2]')
            #weightPuJetSFUpStr    = weightStr.replace('puJetSF[0]','puJetSF[1]')
            #weightPuJetSFDnStr    = weightStr.replace('puJetSF[0]','puJetSF[2]')
            
            weightBtagHFCOUpStr   = weightStr.replace('btagWeights[0]','btagWeights[1]')
            weightBtagHFCODnStr   = weightStr.replace('btagWeights[0]','btagWeights[2]')
            weightBtagHFUCUpStr   = weightStr.replace('btagWeights[0]','btagWeights[3]')
            weightBtagHFUCDnStr   = weightStr.replace('btagWeights[0]','btagWeights[4]')
            weightBtagLFCOUpStr   = weightStr.replace('btagWeights[0]','btagWeights[5]')
            weightBtagLFCODnStr   = weightStr.replace('btagWeights[0]','btagWeights[6]')
            weightBtagLFUCUpStr   = weightStr.replace('btagWeights[0]','btagWeights[7]')
            weightBtagLFUCDnStr   = weightStr.replace('btagWeights[0]','btagWeights[8]')
            
            weightelIDSFUpStr = weightStr.replace('elidSF[0]','elidSF[1]')
            weightelIDSFDnStr = weightStr.replace('elidSF[0]','elidSF[2]')
            weightelRecoSFUpStr = weightStr.replace('elrecoSF[0]','elrecoSF[1]')
            weightelRecoSFDnStr = weightStr.replace('elrecoSF[0]','elrecoSF[2]')
            
            weightmuIDSFUpStr = weightStr.replace('muonidSF[0]','muonidSF[0] + muonidSF[1]')
            weightmuIDSFDnStr = weightStr.replace('muonidSF[0]','muonidSF[0] + muonidSF[2]')
            weightmuIsoSFUpStr = weightStr.replace('muonisoSF[0]','muonidSF[0] + muonisoSF[1]')
            weightmuIsoSFDnStr = weightStr.replace('muonisoSF[0]','muonidSF[0] + muonisoSF[2]')
                        
            weighttauIDVSeSFUpStr = weightStr.replace('tauidVSeSF[0]','tauidVSeSF[1]')
            weighttauIDVSeSFDnStr = weightStr.replace('tauidVSeSF[0]','tauidVSeSF[2]')
            weighttauIDVSmuSFUpStr = weightStr.replace('tauidVSmuSF[0]','tauidVSmuSF[1]')
            weighttauIDVSmuSFDnStr = weightStr.replace('tauidVSmuSF[0]','tauidVSmuSF[2]')
            weighttauIDVSjetSFUpStr = weightStr.replace('tauidVSjetSF[0]','tauidVSjetSF[1]')
            weighttauIDVSjetSFDnStr = weightStr.replace('tauidVSjetSF[0]','tauidVSjetSF[2]')

            if doMuRF:
                weightmuRFcorrdUpStr = 'LHEScaleWeight[8] * '+weightStr
                weightmuRFcorrdDnStr = 'LHEScaleWeight[0] * '+weightStr
                weightmuRUpStr       = 'LHEScaleWeight[7] * '+weightStr
                weightmuRDnStr       = 'LHEScaleWeight[1] * '+weightStr
                weightmuFUpStr       = 'LHEScaleWeight[5] * '+weightStr
                weightmuFDnStr       = 'LHEScaleWeight[3] * '+weightStr

                #if 'Bprime' in sample.prefix: # signals don't have [4] being the 1,1 shift! [8] undefined
                #    weightmuRFcorrdUpStr = 'LHEScaleWeight[7] * '+weightStr
                #    weightmuRUpStr       = 'LHEScaleWeight[6] * '+weightStr
                #    weightmuFUpStr       = 'LHEScaleWeight[4] * '+weightStr
                                        
            else:
                weightmuRFcorrdUpStr = '1.15 * '+weightStr
                weightmuRFcorrdDnStr = '0.85 * '+weightStr
                weightmuRUpStr       = weightStr
                weightmuRDnStr       = weightStr
                weightmuFUpStr       = weightStr
                weightmuFDnStr       = weightStr
                #weighttopptUpStr     = weightStr.replace(topCorr,topCorrUp)
                #weighttopptDnStr     = weightStr.replace(topCorr,topCorrDn)
                #weightjsfUpStr       = weightStr.replace(jetSFstr,jetSFstrUp)
                #weightjsfDnStr       = weightStr.replace(jetSFstr,jetSFstrDn)
                                
                        
        print("*****"*20)
        print("PROCESSING:  "+sample.prefix)

        # Design the EM cuts for categories -- THIS WILL BE THE FIRST CUT
        isEMCut=''
        if isEM == 'L': 
                isEMCut += '(passesMuPD || passesMuEGPD || passesEGPD || passesTauPD)'#(isMu==1 || isEl==1)'
        elif isEM == 'E': 
                isEMCut += 'Good4Lepton_ID[0] == 11'    # Lead Electron
        elif isEM == 'M': 
                isEMCut += 'Good4Lepton_ID[0] == 13'    # Lead Muon
        elif isEM == 'T':
                isEMCut += 'Good4Lepton_ID[0] == 15'    # Lead Tau

        elif isEM == 'EEE':
                isEMCut += 'NgoodLeptons == 3 && ROOT::VecOps::Sum(Good4Lepton_ID) == 33'
        elif isEM == 'EEM':
                isEMCut += 'NgoodLeptons == 3 && ROOT::VecOps::Sum(Good4Lepton_ID) == 35'
        elif isEM == 'EMM':
                isEMCut += 'NgoodLeptons == 3 && ROOT::VecOps::Sum(Good4Lepton_ID) == 37 && ROOT::VecOps::Max(Good4Lepton_ID) == 13'
        elif isEM == 'EET':
                isEMCut += 'NgoodLeptons == 3 && ROOT::VecOps::Sum(Good4Lepton_ID) == 37 && ROOT::VecOps::Max(Good4Lepton_ID) == 15'
        elif isEM == 'ETT':
                isEMCut += 'NgoodLeptons == 3 && ROOT::VecOps::Sum(Good4Lepton_ID) == 41 && ROOT::VecOps::Sort(Good4Lepton_ID)[1] == 15'
        elif isEM == 'EMT':
                isEMCut += 'NgoodLeptons == 3 && ROOT::VecOps::Sum(Good4Lepton_ID) == 39 && ROOT::VecOps::Max(Good4Lepton_ID) == 15'
        elif isEM == 'MMM':
                isEMCut += 'NgoodLeptons == 3 && ROOT::VecOps::Sum(Good4Lepton_ID) == 39 && ROOT::VecOps::Max(Good4Lepton_ID) == 13'
        elif isEM == 'MMT':
                isEMCut += 'NgoodLeptons == 3 && ROOT::VecOps::Sum(Good4Lepton_ID) == 41 && ROOT::VecOps::Sort(Good4Lepton_ID)[1] == 13'
        elif isEM == 'MTT':
                isEMCut += 'NgoodLeptons == 3 && ROOT::VecOps::Sum(Good4Lepton_ID) == 43'
        elif isEM == 'TTT':
                isEMCut += 'NgoodLeptons == 3 && ROOT::VecOps::Sum(Good4Lepton_ID) == 45'

        elif isEM == 'EEEE':
                isEMCut += 'NgoodLeptons == 4 && ROOT::VecOps::Sum(Good4Lepton_ID) == 44'
        elif isEM == 'EEEM':
                isEMCut += 'NgoodLeptons == 4 && ROOT::VecOps::Sum(Good4Lepton_ID) == 46 && ROOT::VecOps::Max(Good4Lepton_ID) == 13'
        elif isEM == 'EEMM':
                isEMCut += 'NgoodLeptons == 4 && ROOT::VecOps::Sum(Good4Lepton_ID) == 48'
        elif isEM == 'EMMM':
                isEMCut += 'NgoodLeptons == 4 && ROOT::VecOps::Sum(Good4Lepton_ID) == 50 && ROOT::VecOps::Max(Good4Lepton_ID) == 13'
        elif isEM == 'EEET':
                isEMCut += 'NgoodLeptons == 4 && ROOT::VecOps::Sum(Good4Lepton_ID) == 46 && ROOT::VecOps::Max(Good4Lepton_ID) == 15'
        elif isEM == 'EETT':
                isEMCut += 'NgoodLeptons == 4 && ROOT::VecOps::Sum(Good4Lepton_ID) == 50 && ROOT::VecOps::Max(Good4Lepton_ID) == 15 && (ROOT::VecOps::Sort(Good4Lepton_ID)[1] + ROOT::VecOps::Sort(Good4Lepton_ID)[2])/2 == 13'
        elif isEM == 'ETTT':
                isEMCut += 'NgoodLeptons == 4 && ROOT::VecOps::Sum(Good4Lepton_ID) == 54 && ROOT::VecOps::Max(Good4Lepton_ID) == 15 && (ROOT::VecOps::Sort(Good4Lepton_ID)[1] + ROOT::VecOps::Sort(Good4Lepton_ID)[2])/2 == 15'
        elif isEM == 'EEMT':
                isEMCut += 'NgoodLeptons == 4 && ROOT::VecOps::Sum(Good4Lepton_ID) == 50 && ROOT::VecOps::Max(Good4Lepton_ID) == 15 && (ROOT::VecOps::Sort(Good4Lepton_ID)[1] + ROOT::VecOps::Sort(Good4Lepton_ID)[2])/2 == 12'
        elif isEM == 'EMMT':
                isEMCut += 'NgoodLeptons == 4 && ROOT::VecOps::Sum(Good4Lepton_ID) == 52 && ROOT::VecOps::Max(Good4Lepton_ID) == 15'
        elif isEM == 'EMTT':
                isEMCut += 'NgoodLeptons == 4 && ROOT::VecOps::Sum(Good4Lepton_ID) == 54 && ROOT::VecOps::Max(Good4Lepton_ID) == 15 && (ROOT::VecOps::Sort(Good4Lepton_ID)[1] + ROOT::VecOps::Sort(Good4Lepton_ID)[2])/2 == 14'
        elif isEM == 'MMMM':
                isEMCut += 'NgoodLeptons == 4 && ROOT::VecOps::Sum(Good4Lepton_ID) == 52 && ROOT::VecOps::Max(Good4Lepton_ID) == 13'
        elif isEM == 'MMMT':
                isEMCut += 'NgoodLeptons == 4 && ROOT::VecOps::Sum(Good4Lepton_ID) == 54 && ROOT::VecOps::Max(Good4Lepton_ID) == 15 && (ROOT::VecOps::Sort(Good4Lepton_ID)[1] + ROOT::VecOps::Sort(Good4Lepton_ID)[2])/2 == 13'
        elif isEM == 'MMTT':
                isEMCut += 'NgoodLeptons == 4 && ROOT::VecOps::Sum(Good4Lepton_ID) == 56'
        elif isEM == 'MTTT':
                isEMCut += 'NgoodLeptons == 4 && ROOT::VecOps::Sum(Good4Lepton_ID) == 58'
        elif isEM == 'TTTT':
                isEMCut += 'NgoodLeptons == 4 && ROOT::VecOps::Sum(Good4Lepton_ID) == 60'
        # if 'SingleMuon' in sample.prefix: # don't let data double count
        #         isEMCut+=' && isMu==1'
        # elif 'SingleElec' in sample.prefix:
        #         isEMCut+=' && isEl==1'

	# Define cuts by region. Use region "all" for all selected events
        cut  = ''# && W_MT < 200' #TEMP. TODO: Comment out once it got implemented in the analyer
                
        #if 'lowMT' in region:
        #        cut += ' && W_MT < 160'
        
        if region == '3lep':
                cut += ' && NgoodLeptons == 3'
        if region == '4lep': 
                cut += ' && NgoodLeptons == 4'
        if '2pb' in region: 
                cut += ' && NJets_PNetL > 1'
        elif '0b' in region: 
                cut += ' && NJets_PNetL == 0'
        if region == 'BAX': 
                cut += ' && NJets_forward == 0'                
        elif region == 'DCY': 
                cut += ' && NJets_forward > 0'
        elif region == 'B': 
                cut += ' && NJets_forward == 0 && NJets_PNetL < 3'
        elif region == 'A': 
                cut += ' && NJets_forward == 0 && NJets_PNetL == 3'
        elif region == 'X': 
                cut += ' && NJets_forward == 0 && NJets_PNetL > 3'
        elif region == 'D': 
                cut += ' && NJets_forward > 0 && NJets_PNetL < 3'
        elif region == 'C': 
                cut += ' && NJets_forward > 0 && NJets_PNetL == 3'
        elif region == 'Y': 
                cut += ' && NJets_forward > 0 && NJets_PNetL > 3'
        elif region == 'V':
                cut  += ' && NJets_forward > 0 && NJets_PNetL < 3 && gcJet_ST < 850'

        # Separate ttbar into mass bins for proper normalization 
        if 'TTTo' in sample.prefix:
            if sample.prefix[-4:] == "1000": 
                cut += ' && genttbarMass > 1000'
            elif sample.prefix[-3:] == "700": 
                cut += ' && genttbarMass > 700 && genttbarMass <= 1000'
            elif sample.prefix[-1] == "0": 
                cut += ' && genttbarMass <= 700'
              
        # Design the tagging cuts for categories
        tagCut = ''
        if isCategorized:
                if tag == 'tagTjet': 
                        tagCut += ' && Bdecay_obs == 1'
                elif tag == 'tagWjet': 
                        tagCut += ' && Bdecay_obs == 2'
                elif tag == 'untagTlep': 
                        tagCut += ' && Bdecay_obs == 3'
                elif tag == 'untagWlep': 
                        tagCut += ' && Bdecay_obs == 4'
                elif tag == 'allWlep': 
                        tagCut += ' && (Bdecay_obs == 4 || Bdecay_obs == 1)'
                elif tag == 'allTlep': 
                        tagCut += ' && (Bdecay_obs == 2 || Bdecay_obs == 3)'

              # signal categories for basic tag counts
                if '2pW' in tag: 
                        tagCut += ' && gcFatJet_nW >= 2'
                elif '2W' in tag: 
                        tagCut += ' && gcFatJet_nW == 2'
                elif '1pW' in tag: 
                        tagCut += ' && gcFatJet_nW >= 1'
                elif '1W' in tag: 
                        tagCut += ' && gcFatJet_nW == 1'
                elif '01W' in tag: 
                        tagCut += ' && gcFatJet_nW <= 1'
                elif '0W' in tag: 
                        tagCut += ' && gcFatJet_nW == 0'  
                if '0T' in tag: 
                        tagCut += ' && gcFatJet_nT == 0'
                elif '01T' in tag: 
                        tagCut += ' && gcFatJet_nT <= 1'
                elif '1T' in tag: 
                        tagCut += ' && gcFatJet_nT == 1'
                elif '1pT' in tag: 
                        tagCut += ' && gcFatJet_nT >= 1'
                elif '2T' in tag: 
                        tagCut += ' && gcFatJet_nT == 2'
                elif '2pT' in tag: 
                        tagCut += ' && gcFatJet_nT >= 2'

        fullcut = isEMCut+cut+tagCut

        print('plotTreeName: '+plotTreeName)
        print('Flavour: '+isEM+', tag: '+tag)
        print("Weights: "+weightStr)
        print('Cuts: '+fullcut)

        # Declare histograms --- COMMENTS FOR UNCERTAINTIES NOT BEING RUN YET
        process = sample.prefix

        # TODO: Switch back to this piece of code once jet veto got implemented in the analyzer
        # If making a root function for additional filtering, define the result before the filter
        if '[0]' in plotTreeName or 'Sum(' in plotTreeName or 'abs(' in plotTreeName or '0.5*(' in plotTreeName:
                df = RDataFrame(tTree[process]).Filter(fullcut)\
                                               .Define('weight',weightStr)\
                                               .Define(iPlot, plotTreeName)
                plotTreeName = iPlot
        else:
                df = RDataFrame(tTree[process]).Filter(fullcut)\
                                               .Define('weight',weightStr)
                                           

        hist = df.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_{process}',xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weight')             

        if ('Single' not in process and 'MuonEG' not in process and 'Tau' not in process) and doAllSys:
            sel = df.Define('weightelRecoSFUp' ,weightelRecoSFUpStr)\
                    .Define('weightelRecoSFDn' ,weightelRecoSFDnStr)\
                    .Define('weightmuRecoSFUp' ,weightmuRecoSFUpStr)\
                    .Define('weightmuRecoSFDn' ,weightmuRecoSFDnStr)\
                    .Define('weightPileupUp'   ,weightPileupUpStr)\
                    .Define('weightPileupDn'   ,weightPileupDnStr)\
                    .Define('weightmuRFcorrdUp',weightmuRFcorrdUpStr)\
                    .Define('weightmuRFcorrdDn',weightmuRFcorrdDnStr)\
                    .Define('weightmuRUp'      ,weightmuRUpStr)\
                    .Define('weightmuRDn'      ,weightmuRDnStr)\
                    .Define('weightmuFUp'      ,weightmuFUpStr)\
                    .Define('weightmuFDn'      ,weightmuFDnStr)\
                    .Define('weightbtagHFCOUp' ,weightBtagHFCOUpStr)\
                    .Define('weightbtagHFCODn' ,weightBtagHFCODnStr)\
                    .Define('weightbtagHFUCUp' ,weightBtagHFUCUpStr)\
                    .Define('weightbtagHFUCDn' ,weightBtagHFUCDnStr)\
                    .Define('weightbtagLFCOUp' ,weightBtagLFCOUpStr)\
                    .Define('weightbtagLFCODn' ,weightBtagLFCODnStr)\
                    .Define('weightbtagLFUCUp' ,weightBtagLFUCUpStr)\
                    .Define('weightbtagLFUCDn' ,weightBtagLFUCDnStr)\
                    .Define('weightelIdSFUp' ,weightelIdSFUpStr)\
                    .Define('weightelIdSFDn' ,weightelIdSFDnStr)\
                    .Define('weightelRecoSFUp' ,weightelRecoSFUpStr)\
                    .Define('weightelRecoSFDn' ,weightelRecoSFDnStr)\
                    .Define('weightmuIdSFUp' ,weightmuIdSFUpStr)\
                    .Define('weightmuIdSFDn' ,weightmuIdSFDnStr)\
                    .Define('weightmuIsoSFUp' ,weightmuIsoSFUpStr)\
                    .Define('weightmuIsoSFDn' ,weightmuIsoSFDnStr)\
                    .Define('weighttauIdVSeSFUp' ,weighttauIdVSeSFUpStr)\
                    .Define('weighttauIdVSeSFDn' ,weighttauIdVSeSFDnStr)\
                    .Define('weighttauIdVSmuSFUp' ,weighttauIdVSmuSFUpStr)\
                    .Define('weighttauIdVSmuSFDn' ,weighttauIdVSmuSFDnStr)\
                    .Define('weighttauIdVSjetSFUp' ,weighttauIdVSjetSFUpStr)\
                    .Define('weighttauIdVSjetSFDn' ,weighttauIdVSjetSFDnStr)\
                    #.Define('weightTrigEffElUp',weightTrigEffElUpStr)\
                    #.Define('weightTrigEffElDn',weightTrigEffElDnStr)\
                    #.Define('weightTrigEffMuUp',weightTrigEffMuUpStr)\
                    #.Define('weightTrigEffMuDn',weightTrigEffMuDnStr)\
                    #.Define('weightPuJetSFUp'  ,weightPuJetSFUpStr)\
                    #.Define('weightPuJetSFDn'  ,weightPuJetSFDnStr)\
                    #.Define('weightjsfUp'      ,weightjsfUpStr)\
                    #.Define('weightjsfDn'      ,weightjsfDnStr)\
                    #.Define('weighttopptUp'    ,weighttopptUpStr)\
                    #.Define('weighttopptDn'    ,weighttopptDnStr)\
                        
            hist_elRecoSFUp  = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_elRecoSFUp_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightelRecoSFUp' )
            hist_elRecoSFDn  = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_elRecoSFDn_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightelRecoSFDn' )
            hist_elIdSFUp    = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_elIdSFUp_{process}'   ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightelIdSFUp'   )
            hist_elIdSFDn    = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_elIdSFDn_{process}'   ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightelIdSFDn'   )
            #hist_elRecoSFUp   = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_elRecoSFUp_{process}'  ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightelRecoSFUp'  )
            #hist_elRecoSFDn   = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_elRecoSFDn_{process}'  ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightelRecoSFDn'  )
            #hist_TrigEffElUp = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_TrigEffElUp_{process}',xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightTrigEffElUp')
            #hist_TrigEffElDn = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_TrigEffElDn_{process}',xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightTrigEffElDn')
            #hist_muRecoSFUp  = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muRecoSFUp_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuRecoSFUp' )
            #hist_muRecoSFDn  = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muRecoSFDn_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuRecoSFDn' )
            hist_muIdSFUp    = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muIdSFUp_{process}'   ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuIdSFUp'   )
            hist_muIdSFDn    = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muIdSFDn_{process}'   ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuIdSFDn'   )
            hist_muIsoSFUp   = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muIsoSFUp_{process}'  ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuIsoSFUp'  )
            hist_muIsoSFDn   = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muIsoSFDn_{process}'  ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuIsoSFDn'  )
            
            hist_tauIdVSeSFUp   = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_tauIdVSeSFUp_{process}'  ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weighttauIdVSeSFUp'  )
            hist_tauIdVSeSFDn   = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_tauIdVSeSFDn_{process}'  ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weighttauIdVSeSFDn'  )
            hist_tauIdVSmuSFUp   = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_tauIdVSmuSFUp_{process}'  ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weighttauIdVSmuSFUp'  )
            hist_tauIdVSmuSFDn   = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_tauIdVSmuSFDn_{process}'  ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weighttauIdVSmuSFDn'  )
            hist_tauIdVSjetSFUp   = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_tauIdVSjetSFUp_{process}'  ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weighttauIdVSjetSFUp'  )
            hist_tauIdVSjetSFDn   = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_tauIdVSjetSFDn_{process}'  ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weighttauIdVSjetSFDn'  )
            #hist_TrigEffMuUp = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_TrigEffMuUp_{process}',xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightTrigEffMuUp')
            #hist_TrigEffMuDn = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_TrigEffMuDn_{process}',xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightTrigEffMuDn')
            hist_PileupUp    = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_PileupUp_{process}'   ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightPileupUp'   )
            hist_PileupDn    = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_PileupDn_{process}'   ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightPileupDn'   )
            #hist_PuJetSFUp   = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_PuJetSFUp_{process}'  ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightPuJetSFUp'  )
            #hist_PuJetSFDn   = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_PuJetSFDn_{process}'  ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightPuJetSFDn'  )
            #hist_jsfUp       = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_jsfUp_{process}'      ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightjsfUp'      )
            #hist_jsfDn       = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_jsfDn_{process}'      ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightjsfDn'      )
            #hist_topptUp     = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_topptUp_{process}'    ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weighttopptUp'    )
            #hist_topptDn     = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_topptDn_{process}'    ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weighttopptDn'    )
            hist_muRFcorrdUp = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muRFcorrdUp_{process}',xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuRFcorrdUp')
            hist_muRFcorrdDn = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muRFcorrdDn_{process}',xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuRFcorrdDn')
            hist_btagHFCOUp  = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_btagHFCOUp_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightbtagHFCOUp' )
            hist_btagHFCODn  = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_btagHFCODn_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightbtagHFCODn' )
            hist_btagHFUCUp  = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_btagHFUCUp_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightbtagHFUCUp' )
            hist_btagHFUCDn  = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_btagHFUCDn_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightbtagHFUCDn' )
            hist_btagLFCOUp  = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_btagLFCOUp_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightbtagLFCOUp' )
            hist_btagLFCODn  = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_btagLFCODn_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightbtagLFCODn' )
            hist_btagLFUCUp  = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_btagLFUCUp_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightbtagLFUCUp' )
            hist_btagLFUCDn  = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_btagLFUCDn_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightbtagLFUCDn' )

            if isCategorized:
                    hist_muRUp       = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muRUp_{process}'      ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuRUp'      )
                    hist_muRDn       = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muRDn_{process}'      ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuRDn'      )
                    hist_muFUp       = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muFUp_{process}'      ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuFUp'      )
                    hist_muFDn       = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muFDn_{process}'      ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuFDn'      )

                    #if tag=='allWlep' or tag=="tagTjet":
                    #        hist_pNetTtagUp = sel.Define('weightpNetTtagUp', weightpNetTtagUpStr)\
                    #                             .Histo1D((f'{iPlot}_{lumiStr}_{catStr}_pNetTtagUp_{process}',xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightpNetTtagUp' )
                    #        hist_pNetTtagDn = sel.Define('weightpNetTtagDn', weightpNetTtagDnStr)\
                    #                             .Histo1D((f'{iPlot}_{lumiStr}_{catStr}_pNetTtagDn_{process}',xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightpNetTtagDn' )
                    #elif tag=='allTlep' or tag=="tagWjet":
                    #        hist_pNetWtagUp = sel.Define('weightpNetWtagUp', weightpNetWtagUpStr)\
                    #                             .Histo1D((f'{iPlot}_{lumiStr}_{catStr}_pNetWtagUp_{process}',xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightpNetWtagUp' )
                    #        hist_pNetWtagDn = sel.Define('weightpNetWtagDn', weightpNetWtagDnStr)\
        #                             .Histo1D((f'{iPlot}_{lumiStr}_{catStr}_pNetWtagDn_{process}',xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightpNetWtagDn' )

                    if doMuRF: # doMuRF happens to be False only for WW, WZ, ZZ, which do not have pdf branches
                            if 'Bprime' in sample.prefix or 'STs' in sample.prefix:
                                    pdfVariations = 101
                            else:
                                    pdfVariations =	103
                            hist_pdf = []
                            for i in range(pdfVariations):
                                    hist_pdf.append(sel.Define(f'weightpdf{i}',f'{weightStr}*LHEPdfWeight[{i}]')\
                                                  .Histo1D((f'{iPlot}_{lumiStr}_{catStr}_pdf{i}_{process}',xAxisLabel,len(xbins)-1,xbins),plotTreeName,f'weightpdf{i}'))
                    else:
                            print(f'{process} does not have pdf branches.')

            if process+'JERup' in tTree:
                    dfjerUp    = RDataFrame(tTree[process+'JERup'])
                    dfjerDn    = RDataFrame(tTree[process+'JERdn'])
                    if '[0]' in plotTreeNameTemp: #TEMP
                            seljerUp   = dfjerUp.Filter(fullcut).Define('weight',weightStr).Define(iPlot,plotTreeNameTemp)
                            seljerDn   = dfjerDn.Filter(fullcut).Define('weight',weightStr).Define(iPlot,plotTreeNameTemp)
                    else:
                            seljerUp   = dfjerUp.Filter(fullcut).Define('weight',weightStr)
                            seljerDn   = dfjerDn.Filter(fullcut).Define('weight',weightStr)
                    hist_jerUp = seljerUp.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_jerUp_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weight')
                    hist_jerDn = seljerDn.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_jerDn_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weight')

            if process+'JECup' in tTree:
                    dfjecUp    = RDataFrame(tTree[process+'JECup'])
                    dfjecDn    = RDataFrame(tTree[process+'JECdn'])
                    if '[0]' in plotTreeNameTemp: #TEMP
                            seljecUp   = dfjecUp.Filter(fullcut).Define('weight',weightStr).Define(iPlot,plotTreeNameTemp)
                            seljecDn   = dfjecDn.Filter(fullcut).Define('weight',weightStr).Define(iPlot,plotTreeNameTemp)
                    else:
                            seljecUp   = dfjecUp.Filter(fullcut).Define('weight',weightStr)
                            seljecDn   = dfjecDn.Filter(fullcut).Define('weight',weightStr)
                    hist_jecUp = seljecUp.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_jecUp_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weight')
                    hist_jecDn = seljecDn.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_jecDn_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weight')


        # WRITE all the histograms (hopefully no event loop gets triggered until here?)
        hist.Write()
        if ('Single' not in process and 'MuonEG' not in process and 'Tau' not in process) and doAllSys:
            hist_elRecoSFUp.Write()
            hist_elRecoSFDn.Write()
            hist_elIdSFUp.Write()
            hist_elIdSFDn.Write()
            #hist_elIsoSFUp.Write()
            #hist_elIsoSFDn.Write()
            #hist_TrigEffElUp.Write()
            #hist_TrigEffElDn.Write()
            #hist_muRecoSFUp.Write()
            #hist_muRecoSFDn.Write()
            hist_muIdSFUp.Write()
            hist_muIdSFDn.Write()
            hist_muIsoSFUp.Write()
            hist_muIsoSFDn.Write()
            hist_tauIdVSeSFUp.Write()
            hist_tauIdVSeSFDn.Write()
            hist_tauIdVSmuSFUp.Write()
            hist_tauIdVSmuSFDn.Write()
            hist_tauIdVSjetSFUp.Write()
            hist_tauIdVSjetSFDn.Write()
            #hist_TrigEffMuUp.Write()
            #hist_TrigEffMuDn.Write()
            hist_PileupUp.Write()
            hist_PileupDn.Write()
            #hist_PuJetSFUp.Write()
            #hist_PuJetSFDn.Write()
            #hist_jsfUp.Write()
            #hist_jsfDn.Write()
            #hist_topptUp.Write()
            #hist_topptDn.Write()
            hist_muRFcorrdUp.Write()
            hist_muRFcorrdDn.Write()
            hist_btagHFCOUp.Write()
            hist_btagHFCODn.Write()
            hist_btagHFUCUp.Write()
            hist_btagHFUCDn.Write()
            hist_btagLFCOUp.Write()
            hist_btagLFCODn.Write()
            hist_btagLFUCUp.Write()
            hist_btagLFUCDn.Write()

            if process+'JERup' in tTree:
                    hist_jerUp.Write()
                    hist_jerDn.Write()

            if process+'JECup' in tTree:
                    hist_jecUp.Write()
                    hist_jecDn.Write()

            if isCategorized:
                    hist_muRUp.Write()
                    hist_muRDn.Write()
                    hist_muFUp.Write()
                    hist_muFDn.Write()
                    #if tag=='allWlep' or tag=="tagTjet":
                    #        hist_pNetTtagUp.Write()
                    #        hist_pNetTtagDn.Write()
                    #elif tag=="allTlep" or tag=="tagWjet":
                    #        hist_pNetWtagUp.Write()
                    #        hist_pNetWtagDn.Write()
                    if doMuRF:
                            for ipdf in hist_pdf:
                                ipdf.Write()

        # del df
        # if 'Single' not in process and doAllSys and not doABCDnn:
        #         del sel
        # if process+'JERup' in tTree:
        #         del dfjerUp
        #         del dfjerDn
        #         if '[0]' in plotDetails[0]:
        #                 del seljerUp
        #                 del seljerDn
        # if process+'JECup' in tTree:
        #         del dfjecUp
        #         del dfjecDn
        #         if '[0]' in plotDetails[0]:
        #                 del seljecUp
        #                 del seljecDn

        print("--- Analyze: %s minutes ---" % (round((time.time() - start_time)/60,2)))
        #DisableImplicitMT()
