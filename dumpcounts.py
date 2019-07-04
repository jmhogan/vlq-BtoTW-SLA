import os,sys

filelist = [
  'SingleElecton_hadd.root'
  'SingleMuon_hadd.root'
 
  'DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
  'DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
  'DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
  'DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
  'DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
# 'DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',

  'QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
  'QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
  'QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
  'QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
  'QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
  'QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
  'QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',

  'ST_s-channel_antitop_leptonDecays_13TeV_powheg-pythia_hadd.root',
  'ST_s-channel_top_leptonDecays_13TeV_powheg-pythia_hadd.root',
# 'ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-pythia8_hadd.root',
# 'ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-pythia8_hadd.root',
  'ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_hadd.root',
  'ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_hadd.root',

  'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_hadd.root',
  'TTToHadronic_TuneCP5_13TeV-powheg-pythia8_hadd.root',
  'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_hadd.root',
# 'TT_Mtt-1000toInf_TuneCP5_PSweights_13TeV-powheg-pythia8_hadd.root',
  'TT_Mtt-700to1000_TuneCP5_PSweights_13TeV-powheg-pythia8_hadd.root',
  'TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_hadd.root',
  'TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_hadd.root',
  'TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8_hadd.root',
 

  'WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
  'WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
  'WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
  'WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
  'WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
  'WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',

  'WW_TuneCP5_PSweights_13TeV-pythia8_hadd.root',
  'WZ_TuneCP5_PSweights_13TeV-pythia8_hadd.root',
  'ZZ_TuneCP5_PSweights_13TeV-pythia8_hadd.root',
  
# 'ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_hadd.root',
# 'ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8',  

# 'BprimeBprime_M-900_TuneCP5_PSweights_13TeV-madgraph-pythia8_BHBH_hadd.root',
# 'BprimeBprime_M-900_TuneCP5_PSweights_13TeV-madgraph-pythia8_BHTW_hadd.root',
# 'BprimeBprime_M-900_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZBH_hadd.root',
# 'BprimeBprime_M-900_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZBZ_hadd.root',
# 'BprimeBprime_M-900_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZTW_hadd.root',
# 'BprimeBprime_M-900_TuneCP5_PSweights_13TeV-madgraph-pythia8_TWTW_hadd.root',
# 'BprimeBprime_M-1000_TuneCP5_PSweights_13TeV-madgraph-pythia8_BHBH_hadd.root',
# 'BprimeBprime_M-1000_TuneCP5_PSweights_13TeV-madgraph-pythia8_BHTW_hadd.root',
# 'BprimeBprime_M-1000_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZBH_hadd.root',
# 'BprimeBprime_M-1000_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZBZ_hadd.root',
# 'BprimeBprime_M-1000_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZTW_hadd.root',
# 'BprimeBprime_M-1000_TuneCP5_PSweights_13TeV-madgraph-pythia8_TWTW_hadd.root',
  'BprimeBprime_M-1100_TuneCP5_PSweights_13TeV-madgraph-pythia8_BHBH_hadd.root',
  'BprimeBprime_M-1100_TuneCP5_PSweights_13TeV-madgraph-pythia8_BHTW_hadd.root',
  'BprimeBprime_M-1100_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZBH_hadd.root',
  'BprimeBprime_M-1100_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZBZ_hadd.root',
  'BprimeBprime_M-1100_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZTW_hadd.root',
  'BprimeBprime_M-1100_TuneCP5_PSweights_13TeV-madgraph-pythia8_TWTW_hadd.root',
  'BprimeBprime_M-1200_TuneCP5_PSweights_13TeV-madgraph-pythia8_BHBH_hadd.root',
  'BprimeBprime_M-1200_TuneCP5_PSweights_13TeV-madgraph-pythia8_BHTW_hadd.root',
  'BprimeBprime_M-1200_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZBH_hadd.root',
  'BprimeBprime_M-1200_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZBZ_hadd.root',
  'BprimeBprime_M-1200_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZTW_hadd.root',
  'BprimeBprime_M-1200_TuneCP5_PSweights_13TeV-madgraph-pythia8_TWTW_hadd.root',
  'BprimeBprime_M-1300_TuneCP5_PSweights_13TeV-madgraph-pythia8_BHBH_hadd.root',
  'BprimeBprime_M-1300_TuneCP5_PSweights_13TeV-madgraph-pythia8_BHTW_hadd.root',
  'BprimeBprime_M-1300_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZBH_hadd.root',
  'BprimeBprime_M-1300_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZBZ_hadd.root',
  'BprimeBprime_M-1300_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZTW_hadd.root',
  'BprimeBprime_M-1300_TuneCP5_PSweights_13TeV-madgraph-pythia8_TWTW_hadd.root',
  'BprimeBprime_M-1400_TuneCP5_PSweights_13TeV-madgraph-pythia8_BHBH_hadd.root',
  'BprimeBprime_M-1400_TuneCP5_PSweights_13TeV-madgraph-pythia8_BHTW_hadd.root',
  'BprimeBprime_M-1400_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZBH_hadd.root',
  'BprimeBprime_M-1400_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZBZ_hadd.root',
  'BprimeBprime_M-1400_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZTW_hadd.root',
  'BprimeBprime_M-1400_TuneCP5_PSweights_13TeV-madgraph-pythia8_TWTW_hadd.root',
  'BprimeBprime_M-1500_TuneCP5_PSweights_13TeV-madgraph-pythia8_BHBH_hadd.root',
  'BprimeBprime_M-1500_TuneCP5_PSweights_13TeV-madgraph-pythia8_BHTW_hadd.root',
  'BprimeBprime_M-1500_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZBH_hadd.root',
  'BprimeBprime_M-1500_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZBZ_hadd.root',
  'BprimeBprime_M-1500_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZTW_hadd.root',
  'BprimeBprime_M-1500_TuneCP5_PSweights_13TeV-madgraph-pythia8_TWTW_hadd.root',
  'BprimeBprime_M-1600_TuneCP5_PSweights_13TeV-madgraph-pythia8_BHBH_hadd.root',
  'BprimeBprime_M-1600_TuneCP5_PSweights_13TeV-madgraph-pythia8_BHTW_hadd.root',
  'BprimeBprime_M-1600_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZBH_hadd.root',
  'BprimeBprime_M-1600_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZBZ_hadd.root',
  'BprimeBprime_M-1600_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZTW_hadd.root',
  'BprimeBprime_M-1600_TuneCP5_PSweights_13TeV-madgraph-pythia8_TWTW_hadd.root',
  'BprimeBprime_M-1800_TuneCP5_PSweights_13TeV-madgraph-pythia8_BHBH_hadd.root',
  'BprimeBprime_M-1800_TuneCP5_PSweights_13TeV-madgraph-pythia8_BHTW_hadd.root',
  'BprimeBprime_M-1800_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZBH_hadd.root',
  'BprimeBprime_M-1800_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZBZ_hadd.root',
  'BprimeBprime_M-1800_TuneCP5_PSweights_13TeV-madgraph-pythia8_BZTW_hadd.root',
  'BprimeBprime_M-1800_TuneCP5_PSweights_13TeV-madgraph-pythia8_TWTW_hadd.root',

  'TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_BWBW_hadd.root',
  'TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_THBW_hadd.root',
  'TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_THTH_hadd.root',
  'TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_TZBW_hadd.root',
  'TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_TZTH_hadd.root',
  'TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_TZTZ_hadd.root',
# 'TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_BWBW_hadd.root',
# 'TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_THBW_hadd.root',
# 'TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_THTH_hadd.root',
# 'TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_TZBW_hadd.root',
# 'TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_TZTH_hadd.root',
# 'TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_TZTZ_hadd.root',
# 'TprimeTprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_BWBW_hadd.root',
# 'TprimeTprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_THBW_hadd.root',
# 'TprimeTprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_THTH_hadd.root',
# 'TprimeTprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_TZBW_hadd.root',
# 'TprimeTprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_TZTH_hadd.root',
# 'TprimeTprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_TZTZ_hadd.root',
# 'TprimeTprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_BWBW_hadd.root',
# 'TprimeTprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_THBW_hadd.root',
# 'TprimeTprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_THTH_hadd.root',
# 'TprimeTprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_TZBW_hadd.root',
# 'TprimeTprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_TZTH_hadd.root',
# 'TprimeTprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_TZTZ_hadd.root',
# 'TprimeTprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_BWBW_hadd.root',
# 'TprimeTprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_THBW_hadd.root',
# 'TprimeTprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_THTH_hadd.root',
# 'TprimeTprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_TZBW_hadd.root',
# 'TprimeTprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_TZTH_hadd.root',
# 'TprimeTprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_TZTZ_hadd.root',
# 'TprimeTprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_BWBW_hadd.root',
# 'TprimeTprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_THBW_hadd.root',
# 'TprimeTprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_THTH_hadd.root',
# 'TprimeTprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_TZBW_hadd.root',
# 'TprimeTprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_TZTH_hadd.root',
# 'TprimeTprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_TZTZ_hadd.root',
# 'TprimeTprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_BWBW_hadd.root',
  'TprimeTprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_THBW_hadd.root',
  'TprimeTprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_THTH_hadd.root',
  'TprimeTprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_TZBW_hadd.root',
  'TprimeTprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_TZTH_hadd.root',
  'TprimeTprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_TZTZ_hadd.root',
  'TprimeTprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_BWBW_hadd.root',
  'TprimeTprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_THBW_hadd.root',
  'TprimeTprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_THTH_hadd.root',
  'TprimeTprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_TZBW_hadd.root',
  'TprimeTprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_TZTH_hadd.root',
  'TprimeTprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_TZTZ_hadd.root',
# 'TprimeTprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_BWBW_hadd.root',
# 'TprimeTprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_THBW_hadd.root',
# 'TprimeTprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_THTH_hadd.root',
# 'TprimeTprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_TZBW_hadd.root',
# 'TprimeTprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_TZTH_hadd.root',
# 'TprimeTprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_TZTZ_hadd.root',
]

from ROOT import TFile, TH1

for file in filelist:
    print('-------------------------------------------------------')
    rfile = TFile.Open('root://cmseos.fnal.gov//store/user/cholz/FWLJMET102X_1lep2018Dnn_070219_step1hadds'+file)
    hist = rfile.Get("weightHist")
    adjusted = hist.GetBinContent(1)
    integral = hist.GetBinContent(5) + hist.GetBinContent(7)
    newpdf = hist.GetBinContent(7)

    if 'prime' not in file:
        print(str(adjusted)+'. # from integral '+str(integral)+', file '+file)
    else:
        print(str(newpdf)+'. # from integral'+str(integral)+', file'+file)







