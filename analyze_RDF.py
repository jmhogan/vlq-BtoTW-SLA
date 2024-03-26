#!/usr/bin/python
from ROOT import TH1D,TTree,TFile,RDataFrame,TH1,EnableImplicitMT
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

def analyze(tTree,sample,doAllSys,iPlot,plotDetails,category,region,isCategorized, outHistFile):
        start_time = time.time()
        plotTreeName=plotDetails[0]
        xbins=array('d', plotDetails[1])
        xAxisLabel=plotDetails[2]
        
	# Define categories
        isEM  = category['isEM']
        tag   = category['tag']
        catStr = 'is'+isEM+'_'+tag

	# Define weights
        topCorr     = '1'
        topCorrUp   = '1'
        topCorrDn   = '1'
        jetSFstr    = '1'
        jetSFstrUp  = '1'
        jetSFstrDn  = '1'
        if ('WJetsHT' in sample.prefix):
                jetSFstr = 'gcHTCorr_WjetLHE[0]' # 
                jetSFstrUp = 'gcHTCorr_WjetLHE[1]' #
                jetSFstrDn = 'gcHTCorr_WjetLHE[2]' #
        if 'TTTo' in sample.prefix or 'TTMT' in sample.prefix:
                topCorr = 'gcHTCorr_top[0]'
                topCorrUp = 'gcHTCorr_top[1]'
                topCorrDn = 'gcHTCorr_top[2]'

        weightStr = '1'
        doMuRF = True
        if (sample.prefix).find('WW') == 0 or (sample.prefix).find('WZ') == 0 or (sample.prefix).find('ZZ') == 0:
                doMuRF = False

        doABCDnn = False
        if "ABCDnn" in iPlot:
                if (sample.prefix).find('QCD') == 0 or (sample.prefix).find('TTTo')==0 or (sample.prefix).find('TTMT')==0 or (sample.prefix).find('ST')==0 or (sample.prefix).find('WJets') == 0:
                        doABCDnn = True
                        plotTreeName = plotTreeName.split('_ABCDnn')[0] #TEMP
                else:
                        plotTreeName = plotTreeName.split('_ABCDnn')[0]

        if 'Single' not in sample.prefix: 
                if doABCDnn:
                        weightStr += ' * transfer_ABCDnn'
                else:
                        weightStr += ' * '+jetSFstr+' * '+topCorr+' * PileupWeights[0] * leptonIDSF[0] * leptonRecoSF[0] * leptonIsoSF[0] * leptonHLTSF[0] * btagWeights[17] *'+str(targetlumi[sample.year]*sample.xsec/sample.nrun)+' * (genWeight/abs(genWeight))'

                        weightelRecoSFUpStr  = weightStr.replace('leptonRecoSF[0]','(isMu*leptonRecoSF[0]+isEl*leptonRecoSF[1])')
                        weightelRecoSFDnStr= weightStr.replace('leptonRecoSF[0]','(isMu*leptonRecoSF[0]+isEl*leptonRecoSF[2])')
                        weightmuRecoSFUpStr  = weightStr.replace('leptonRecoSF[0]','(isMu*leptonRecoSF[1]+isEl*leptonRecoSF[0])')
                        weightmuRecoSFDnStr= weightStr.replace('leptonRecoSF[0]','(isMu*leptonRecoSF[2]+isEl*leptonRecoSF[0])')
                        weightelIdSFUpStr  = weightStr.replace('leptonIDSF[0]','(leptonHLTSF[0]+isEl*leptonHLTSF[1])')
                        weightelIdSFDnStr= weightStr.replace('leptonIDSF[0]','(leptonHLTSF[0]-isEl*leptonHLTSF[1])')
                        weightmuIdSFUpStr  = weightStr.replace('leptonIDSF[0]','(isEl*leptonHLTSF[0]+isMu*leptonHLTSF[1])')
                        weightmuIdSFDnStr= weightStr.replace('leptonIDSF[0]','(isEl*leptonHLTSF[0]+isMu*leptonHLTSF[2])')
                        weightelIsoSFUpStr  = weightStr.replace('leptonIsoSF[0]','(leptonIsoSF[0]+isEl*leptonIsoSF[1])')
                        weightelIsoSFDnStr= weightStr.replace('leptonIsoSF[0]','(leptonIsoSF[0]-isEl*leptonIsoSF[1])')
                        weightmuIsoSFUpStr  = weightStr.replace('leptonIsoSF[0]','(leptonIsoSF[0]+isMu*leptonIsoSF[1])')
                        weightmuIsoSFDnStr= weightStr.replace('leptonIsoSF[0]','(leptonIsoSF[0]-isMu*leptonIsoSF[1])')
                        weightTrigEffElUpStr  = weightStr.replace('leptonHLTSF[0]','(leptonIDSF[0]+isEl*leptonIDSF[1])')
                        weightTrigEffElDnStr= weightStr.replace('leptonHLTSF[0]','(leptonIDSF[0]-isEl*leptonIDSF[1])')
                        weightTrigEffMuUpStr  = weightStr.replace('leptonHLTSF[0]','(leptonIDSF[0]+isMu*leptonIDSF[1])')
                        weightTrigEffMuDnStr= weightStr.replace('leptonHLTSF[0]','(leptonIDSF[0]-isMu*leptonIDSF[1])')
                        weightPileupUpStr   = weightStr.replace('PileupWeights[0]','PileupWeights[1]')
                        weightPileupDnStr   = weightStr.replace('PileupWeights[0]','PileupWeights[2]')
                        weightBtagHFCOUpStr   = weightStr.replace('btagWeights[17]','btagWeights[18]')
                        weightBtagHFCODnStr   = weightStr.replace('btagWeights[17]','btagWeights[19]')
                        weightBtagHFUCUpStr   = weightStr.replace('btagWeights[17]','btagWeights[20]')
                        weightBtagHFUCDnStr   = weightStr.replace('btagWeights[17]','btagWeights[21]')
                        weightBtagLFCOUpStr   = weightStr.replace('btagWeights[17]','btagWeights[22]')
                        weightBtagLFCODnStr   = weightStr.replace('btagWeights[17]','btagWeights[23]')
                        weightBtagLFUCUpStr   = weightStr.replace('btagWeights[17]','btagWeights[24]')
                        weightBtagLFUCDnStr   = weightStr.replace('btagWeights[17]','btagWeights[25]')
                        ### These weights are here in case we ever switch back to btag shape-reweighting scale factors
                        # weightBtagHFUpStr   = weightStr.replace('btagWeights[0]','btagWeights[1]')
                        # weightBtagHFDnStr   = weightStr.replace('btagWeights[0]','btagWeights[2]')
                        # weightBtagLFUpStr   = weightStr.replace('btagWeights[0]','btagWeights[3]')
                        # weightBtagLFDnStr   = weightStr.replace('btagWeights[0]','btagWeights[4]')
                        # weightBtagHFS1UpStr   = weightStr.replace('btagWeights[0]','btagWeights[5]')
                        # weightBtagHFS1DnStr   = weightStr.replace('btagWeights[0]','btagWeights[6]')
                        # weightBtagHFS2UpStr   = weightStr.replace('btagWeights[0]','btagWeights[7]')
                        # weightBtagHFS2DnStr   = weightStr.replace('btagWeights[0]','btagWeights[8]')
                        # weightBtagLFS1UpStr   = weightStr.replace('btagWeights[0]','btagWeights[9]')
                        # weightBtagLFS1DnStr   = weightStr.replace('btagWeights[0]','btagWeights[10]')
                        # weightBtagLFS2UpStr   = weightStr.replace('btagWeights[0]','btagWeights[11]')
                        # weightBtagLFS2DnStr   = weightStr.replace('btagWeights[0]','btagWeights[12]')
                        # weightBtagCFE1UpStr   = weightStr.replace('btagWeights[0]','btagWeights[13]')
                        # weightBtagCFE1DnStr   = weightStr.replace('btagWeights[0]','btagWeights[14]')
                        # weightBtagCFE2UpStr   = weightStr.replace('btagWeights[0]','btagWeights[15]')
                        # weightBtagCFE2DnStr   = weightStr.replace('btagWeights[0]','btagWeights[16]')
                        if doMuRF:
                                weightmuRFcorrdUpStr = 'LHEScaleWeight[8] * '+weightStr
                                weightmuRFcorrdDnStr = 'LHEScaleWeight[0] * '+weightStr
                                weightmuRUpStr       = 'LHEScaleWeight[7] * '+weightStr
                                weightmuRDnStr       = 'LHEScaleWeight[1] * '+weightStr
                                weightmuFUpStr       = 'LHEScaleWeight[5] * '+weightStr
                                weightmuFDnStr       = 'LHEScaleWeight[3] * '+weightStr
                        else:
                                weightmuRFcorrdUpStr = '1.15 * '+weightStr
                                weightmuRFcorrdDnStr = '0.85 * '+weightStr
                                weightmuRUpStr       = weightStr
                                weightmuRDnStr       = weightStr
                                weightmuFUpStr       = weightStr
                                weightmuFDnStr       = weightStr
                                weighttopptUpStr     = weightStr.replace(topCorr,topCorrUp)
                                weighttopptDnStr     = weightStr.replace(topCorr,topCorrDn)
                                weightjsfUpStr       = weightStr.replace(jetSFstr,jetSFstrUp)
                                weightjsfDnStr       = weightStr.replace(jetSFstr,jetSFstrDn)
                                

        print("*****"*20)
        print("PROCESSING:  "+sample.prefix)

	# Design the EM cuts for categories -- THIS WILL BE THE FIRST CUT
        isEMCut=''
        if isEM=='E': 
                isEMCut+='isEl==1'
        elif isEM=='M': 
                isEMCut+='isMu==1'
        elif isEM=='L': 
                isEMCut+='(isMu==1 || isEl==1)'
        if 'SingleMuon' in sample.prefix: # don't let data double count
                isEMCut+=' && isMu==1'
        elif 'SingleElec' in sample.prefix:
                isEMCut+=' && isEl==1'
                        
	# Define cuts by region. Use region "all" for all selected events
        cut  = ' && W_MT < 200' # TODO: 160 or 200
        #if 'lowMT' in region:
        #        cut += ' && W_MT < 160'
        if region == 'isoVT':
                cut += ' && lepton_miniIso < 0.05'
        if '1pb' in region: 
                cut += ' && NJets_DeepFlavL > 0'
        elif '2pb' in region: 
                cut += ' && NJets_DeepFlavL > 1'
        elif '0b' in region: 
                cut += ' && NJets_DeepFlavL == 0'
        if region == 'BAX': 
                cut += ' && NJets_forward == 0'                
        elif region == 'DCY': 
                cut += ' && NJets_forward > 0'
        elif region == 'B': 
                cut += ' && NJets_forward == 0 && NJets_DeepFlavL < 3'
        elif region == 'A': 
                cut += ' && NJets_forward == 0 && NJets_DeepFlavL == 3'
        elif region == 'X': 
                cut += ' && NJets_forward == 0 && NJets_DeepFlavL > 3'
        elif region == 'D': 
                cut += ' && NJets_forward > 0 && NJets_DeepFlavL < 3'
        elif region == 'C': 
                cut += ' && NJets_forward > 0 && NJets_DeepFlavL == 3'
        elif region == 'Y': 
                cut += ' && NJets_forward > 0 && NJets_DeepFlavL > 3'

        # Separate ttbar into mass bins for proper normalization 
        if not doABCDnn:
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
        df = RDataFrame(tTree[process])

        try:
                sel = df.Filter(fullcut).Define('weight',weightStr)
        except:
                print("No dataframe built!!")

        if doAllSys and 'Single' not in process:
                try:
                        selMC = df.Filter(fullcut)\
                                  .Define('weight',weightStr)\
                                  .Define('weightelRecoSFUp' ,weightelRecoSFUpStr)\
                                  .Define('weightelRecoSFDn' ,weightelRecoSFDnStr)\
                                  .Define('weightelIdSFUp'   ,weightelIdSFUpStr)\
                                  .Define('weightelIdSFDn'   ,weightelIdSFDnStr)\
                                  .Define('weightelIsoSFUp'  ,weightelIsoSFUpStr)\
                                  .Define('weightelIsoSFDn'  ,weightelIsoSFDnStr)\
                                  .Define('weighttrigeffElUp',weightTrigEffElUpStr)\
                                  .Define('weighttrigeffElDn',weightTrigEffElDnStr)\
                                  .Define('weightmuRecoSFUp' ,weightmuRecoSFUpStr)\
                                  .Define('weightmuRecoSFDn' ,weightmuRecoSFDnStr)\
                                  .Define('weightmuIdSFUp'   ,weightmuIdSFUpStr)\
                                  .Define('weightmuIdSFDn'   ,weightmuIdSFDnStr)\
                                  .Define('weightmuIsoSFUp'  ,weightmuIsoSFUpStr)\
                                  .Define('weightmuIsoSFDn'  ,weightmuIsoSFDnStr)\
                                  .Define('weighttrigeffMuUp',weightTrigEffMuUpStr)\
                                  .Define('weighttrigeffMuDn',weightTrigEffMuDnStr)\
                                  .Define('weightpileupUp'   ,weightPileupUpStr)\
                                  .Define('weightpileupDn'   ,weightPileupDnStr)\
                                  .Define('weightjsfUp'      ,weightjsfUpStr)\
                                  .Define('weightjsfDn'      ,weightjsfDnStr)\
                                  .Define('weighttopptUp'    ,weighttopptUpStr)\
                                  .Define('weighttopptDn'    ,weighttopptDnStr)\
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
                
                except:
                        print('No dataframe built!!')
        
        hist = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_{process}',xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weight')
        hist.Write()
        del hist

        if doAllSys and 'Single' not in process:
                hist_elRecoSFUp  = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_elRecoSFUp_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightelRecoSFUp' )
                hist_elRecoSFDn  = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_elRecoSFDn_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightelRecoSFDn' )
                hist_elIdSFUp    = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_elIdSFUp_{process}'   ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightelIdSFUp'   )
                hist_elIdSFDn    = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_elIdSFDn_{process}'   ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightelIdSFDn'   )
                hist_elIsoSFUp   = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_elIsoSFUp_{process}'  ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightelIsoSFUp'  )
                hist_elIsoSFDn   = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_elIsoSFDn_{process}'  ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightelIsoSFDn'  )
                hist_TrigEffElUp = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_TrigEffElUp_{process}',xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightTrigEffElUp')
                hist_TrigEffElDn = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_TrigEffElDn_{process}',xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightTrigEffElDn')
                hist_muRecoSFUp  = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muRecoSFUp_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuRecoSFUp' )
                hist_muRecoSFDn  = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muRecoSFDn_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuRecoSFDn' )
                hist_muIdSFUp    = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muIdSFUp_{process}'   ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuIdSFUp'   )
                hist_muIdSFDn    = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muIdSFDn_{process}'   ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuIdSFDn'   )
                hist_muIsoSFUp   = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muIsoSFUp_{process}'  ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuIsoSFUp'  )
                hist_muIsoSFDn   = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muIsoSFDn_{process}'  ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuIsoSFDn'  )
                hist_TrigEffMuUp = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_TrigEffMuUp_{process}',xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightTrigEffMuUp')
                hist_TrigEffMuDn = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_TrigEffMuDn_{process}',xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightTrigEffMuDn')
                hist_PileupUp    = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_PileupUp_{process}'   ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightPileupUp'   )
                hist_PileupDn    = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_PileupDn_{process}'   ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightPileupDn'   )
                hist_jsfUp       = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_jsfUp_{process}'      ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightjsfUp'      )
                hist_jsfDn       = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_jsfDn_{process}'      ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightjsfDn'      )
                hist_topptUp     = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_topptUp_{process}'    ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weighttopptUp'    )
                hist_topptDn     = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_topptDn_{process}'    ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weighttopptDn'    )
                hist_muRFcorrdUp = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muRFcorrdUp_{process}',xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuRFcorrdUp')
                hist_muRFcorrdDn = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muRFcorrdDn_{process}',xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuRFcorrdDn')
                hist_muRUp       = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muRUp_{process}'      ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuRUp'      )
                hist_muRDn       = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muRDn_{process}'      ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuRDn'      )
                hist_muFUp       = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muFUp_{process}'      ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuFUp'      )
                hist_muFDn       = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_muFDn_{process}'      ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuFDn'      )
                hist_btagHFCOUp  = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_btagHFCOUp_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightbtagHFCOUp' )
                hist_btagHFCODn  = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_btagHFCODn_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightbtagHFCODn' )
                hist_btagHFUCUp  = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_btagHFUCUp_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightbtagHFUCUp' )
                hist_btagHFUCDn  = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_btagHFCODn_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightbtagHFUCDn' )
                hist_btagLFCOUp  = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_btagLFCOUp_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightbtagLFCOUp' )
                hist_btagLFCODn  = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_btagLFCODn_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightbtagLFCODn' )
                hist_btagLFUCUp  = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_btagLFUCUp_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightbtagLFUCUp' )
                hist_btagLFUCDn  = selMC.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_btagLFCODn_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightbtagLFUCDn' )
                
                hist_elRecoSFUp.Write()
                
                ## TO-DO: Add ABCDnn Uncertainties!

                ## TO-DO: check tree names for jer and jec!
		if process+'jerUp' in tTree: 
                        dfjerUp    = RDataFrame(tTree[process+'jerUp'])
                        seljerUp   = dfjerUp.Filter(fullcut).Define('weight',weightStr)
                        dfjerDn    = RDataFrame(tTree[process+'jerDn'])
                        seljerDn   = dfjerDn.Filter(fullcut).Define('weight',weightStr)
                        hist_jerUp = seljerUp.Histo1D((f'{iPlot}_jerUp_{lumiStr}_{catStr}_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weight')
                        hist_jerDn = seljerDn.Histo1D((f'{iPlot}_jerDn_{lumiStr}_{catStr}_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weight')
                        hist_jerUp.Write()
                        hist_jerDn.Write()
		if process+'jecUp' in tTree:                                                                                                                            
                        dfjecUp  = RDataFrame(tTree[process+'jecUp'])
                        seljecUp = dfjecUp.Filter(fullcut).Define('weight',weightStr)
                        dfjecDn  = RDataFrame(tTree[process+'jecDn'])
                        seljecDn = dfjecDn.Filter(fullcut).Define('weight',weightStr)
                        hist_jecUp = seljecUp.Histo1D((f'{iPlot}_jecUp_{lumiStr}_{catStr}_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weight')
                        hist_jecDn = seljecDn.Histo1D((f'{iPlot}_jecDn_{lumiStr}_{catStr}_{process}' ,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weight')
                        hist_jecUp.Write()
                        hist_jecDn.Write()

		# if isCategorized:
		# 	histptrs[iPlot+'muRUp_'   +lumicatproc] = selMC.Histo1D((iPlot+'muRUp_'  +lumicatproc,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuRUp')
		# 	histptrs[iPlot+'muRDown_' +lumicatproc] = selMC.Histo1D((iPlot+'muRDown_'+lumicatproc,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightmuRDown')
		# 	histptrs[iPlot+'muFUp_'   +lumicatproc] = selMC.Histo1D((iPlot+'muFUp_'  +lumicatproc,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightFUp')
		# 	histptrs[iPlot+'muFDown_' +lumicatproc] = selMC.Histo1D((iPlot+'muFDown_'+lumicatproc,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightFDown')

                        ### TO-DO: check how many PDF variations live in NanoAOD, find branch names and get this segment set up correctly
                        # for i in range(100): histptrs[iPlot+'pdf'+str(i)+'_'+lumicatproc] = selMC.Define('weightpdf'+str(i),weightStr+'*pdfWeights['+str(i)+']').Histo1D((iPlot+'pdf'+str(i)+'_'+lumicatproc,xAxisLabel,len(xbins)-1,xbins),plotTreeName,'weightpdf'+str(i))

        print("--- Analyze: %s minutes ---" % (round((time.time() - start_time)/60,2)))
