import ROOT
import os 

# Question: A lot of the samples have _PSweights_.  The samples we were working with before didn't have this.  Is it good or bad?
# Sample Dictionaries: samples, samples_2016APVUL, samples_2016UL, samples_2017UL, samples_2018UL, samples_test, samples_QCD

targetlumi = {'2022':5010.4+2970.0, '2022EE':5807.0+17781.9+3082.8, '2023':17794., '2023BPix':9451.}
lumiStr = '62fb' #str(targetlumi/1000).replace('.','p') # 1/fb
systListShort = ['Pileup', 'elRecoSF', 'muRecoSF', 'muRFcorrd', 'btagHFCO', 'btagHFUC', 'btagLFCO', 'btagLFUC', 'jer', 'jec'] #'elIdSF', 'elIsoSF', 'TrigEffEl', 'muIdSF', 'muIsoSF', 'TrigEffMu', , 'jsf', 'toppt', 'PuJetSF'
systListFull = ['Pileup', 'elRecoSF', 'muRecoSF', 'muRFcorrd', 'muR', 'muF', 'btagHFCO', 'btagHFUC', 'btagLFCO', 'btagLFUC', 'jer', 'jec'] #'elIdSF', 'elIsoSF', 'TrigEffEl', 'muIdSF', 'muIsoSF', 'TrigEffMu', , 'pNetTtag', 'pNetWtag', 'PuJetSF', 'jsf', 'toppt'
uncorrList_sf = ['jer', 'jec', 'btagHFUC', 'btagLFUC'] #'TrigEffEl', 'TrigEffMu',
yearList = ["2022", "2022EE", "2023", "2023BPix"]        
systListShortPlots = systListShort.copy()
systListFullPlots = systListFull.copy()
for syst in uncorrList_sf:
    systListShortPlots.remove(syst)
    systListFullPlots.remove(syst)
    for year in yearList:
        systListShortPlots.append(syst+year)
        systListFullPlots.append(syst+year)

# all with direct alpha-ratio. sqrt(sys^2+stat^2+closure^2)

class sample:
    def __init__(self, prefix, xsec, year, textlist, samplename): #, color
        self.prefix = prefix
        self.year = year
        self.textlist = textlist
        self.samplename = samplename
        self.nrun = 1 # dummy
        self.kfactor = 1 # dummy
        self.xsec = xsec # in pb
        self.color = ROOT.kBlack

# fill in these pair production xsec later if desired
xsec = {}

# Update the following block (Bprime), we need our Bprime samples (copy from Timber repo)
Bprime_M1000_2022 = sample("Bprime_M1000_2022", 1.0, "2022", "Bprime_M1000_2022NanoList.txt", "/BprimeBprimeto2B4Tau_MB-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M1000_2022EE = sample("Bprime_M1000_2022EE", 1.0, "2022EE", "Bprime_M1000_2022EENanoList.txt", "/BprimeBprimeto2B4Tau_MB-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M1000_2023 = sample("Bprime_M1000_2023", 1.0, "2023", "Bprime_M1000_2023NanoList.txt", "/BprimeBprimeto2B4Tau_MB-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M1000_2023BPix = sample("Bprime_M1000_2023BPix", 1.0, "2023BPix", "Bprime_M1000_2023BPixNanoList.txt", "/BprimeBprimeto2B4Tau_MB-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M1300_2022 = sample("Bprime_M1300_2022", 1.0, "2022", "Bprime_M1300_2022NanoList.txt", "/BprimeBprimeto2B4Tau_MB-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M1300_2022EE = sample("Bprime_M1300_2022EE", 1.0, "2022EE", "Bprime_M1300_2022EENanoList.txt", "/BprimeBprimeto2B4Tau_MB-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M1300_2023 = sample("Bprime_M1300_2023", 1.0, "2023", "Bprime_M1300_2023NanoList.txt", "/BprimeBprimeto2B4Tau_MB-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M1300_2023BPix = sample("Bprime_M1300_2023BPix", 1.0, "2023BPix", "Bprime_M1300_2023BPixNanoList.txt", "/BprimeBprimeto2B4Tau_MB-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M1600_2022 = sample("Bprime_M1600_2022", 1.0, "2022", "Bprime_M1600_2022NanoList.txt", "/BprimeBprimeto2B4Tau_MB-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M1600_2022EE = sample("Bprime_M1600_2022EE", 1.0, "2022EE", "Bprime_M1600_2022EENanoList.txt", "/BprimeBprimeto2B4Tau_MB-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M1600_2023 = sample("Bprime_M1600_2023", 1.0, "2023", "Bprime_M1600_2023NanoList.txt", "/BprimeBprimeto2B4Tau_MB-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M1600_2023BPix = sample("Bprime_M1600_2023BPix", 1.0, "2023BPix", "Bprime_M1600_2023BPixNanoList.txt", "/BprimeBprimeto2B4Tau_MB-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M700_2022 = sample("Bprime_M700_2022", 1.0, "2022", "Bprime_M700_2022NanoList.txt", "/BprimeBprimeto2B4Tau_MB-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M700_2022EE = sample("Bprime_M700_2022EE", 1.0, "2022EE", "Bprime_M700_2022EENanoList.txt", "/BprimeBprimeto2B4Tau_MB-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M700_2023 = sample("Bprime_M700_2023", 1.0, "2023", "Bprime_M700_2023NanoList.txt", "/BprimeBprimeto2B4Tau_MB-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M700_2023BPix = sample("Bprime_M700_2023BPix", 1.0, "2023BPix", "Bprime_M700_2023BPixNanoList.txt", "/BprimeBprimeto2B4Tau_MB-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M400_2022 = sample("Bprime_M400_2022", 1.0, "2022", "Bprime_M400_2022NanoList.txt", "/BprimeBprimeto2B4Tau_MB-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M400_2022EE = sample("Bprime_M400_2022EE", 1.0, "2022EE", "Bprime_M400_2022EENanoList.txt", "/BprimeBprimeto2B4Tau_MB-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M400_2023 = sample("Bprime_M400_2023", 1.0, "2023", "Bprime_M400_2023NanoList.txt", "/BprimeBprimeto2B4Tau_MB-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M400_2023BPix = sample("Bprime_M400_2023BPix", 1.0, "2023BPix", "Bprime_M400_2023BPixNanoList.txt", "/BprimeBprimeto2B4Tau_MB-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")


DYPT402022 = sample("DYPT402022", 403.7, "2022", "DYPT402022NanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-40to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
DYPT402022EE = sample("DYPT402022EE", 403.7, "2022EE", "DYPT402022EENanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-40to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
DYPT402023 = sample("DYPT402023", 403.7, "2023", "DYPT402023NanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-40to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
DYPT402023BPix = sample("DYPT402023BPix", 403.7, "2023BPix", "DYPT402023BPixNanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-40to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
DYPT1002022 = sample("DYPT1002022", 58.46, "2022", "DYPT1002022NanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
DYPT1002022EE = sample("DYPT1002022EE", 58.46, "2022EE", "DYPT1002022EENanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
DYPT1002023 = sample("DYPT1002023", 58.46, "2023", "DYPT1002023NanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
DYPT1002023BPix = sample("DYPT1002023BPix", 58.46, "2023BPix", "DYPT1002023BPixNanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
DYPT2002022 = sample("DYPT2002022", 6.678, "2022", "DYPT2002022NanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
DYPT2002022EE = sample("DYPT2002022EE", 6.678, "2022EE", "DYPT2002022EENanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
DYPT2002023 = sample("DYPT2002023", 6.678, "2023", "DYPT2002023NanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
DYPT2002023BPix = sample("DYPT2002023BPix", 6.678, "2023BPix", "DYPT2002023BPixNanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
DYPT4002022 = sample("DYPT4002022", 0.3833	, "2022", "DYPT4002022NanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
DYPT4002022EE = sample("DYPT4002022EE", 0.3833	, "2022EE", "DYPT4002022EENanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
DYPT4002023 = sample("DYPT4002023", 0.3833	, "2023", "DYPT4002023NanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
DYPT4002023BPix = sample("DYPT4002023BPix", 0.3833	, "2023BPix", "DYPT4002023BPixNanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
DYPT6002022 = sample("DYPT6002022", 0.06843, "2022", "DYPT6002022NanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
DYPT6002022EE = sample("DYPT6002022EE", 0.06843, "2022EE", "DYPT6002022EENanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
DYPT6002023 = sample("DYPT6002023", 0.06843, "2023", "DYPT6002023NanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
DYPT6002023BPix = sample("DYPT6002023BPix", 0.06843, "2023BPix", "DYPT6002023BPixNanoList.txt", "/DYto2L-4Jets_MLL-50_PTLL-600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

QCDHT10002022  = sample("QCDHT10002022", 883.7, "2022", "QCDHT10002022NanoList.txt", "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
QCDHT10002022EE     = sample("QCDHT10002022EE", 883.7, "2022EE", "QCDHT10002022EENanoList.txt", "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
QCDHT10002023     = sample("QCDHT10002023", 883.7, "2023", "QCDHT10002023NanoList.txt", "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
QCDHT10002023BPix     = sample("QCDHT10002023BPix", 883.7, "2023BPix", "QCDHT10002023BPixNanoList.txt", "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM")
QCDHT12002022  = sample("QCDHT12002022", 383.5, "2022", "QCDHT12002022NanoList.txt", "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
QCDHT12002022EE     = sample("QCDHT12002022EE", 383.5, "2022EE", "QCDHT12002022EENanoList.txt", "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
QCDHT12002023     = sample("QCDHT12002023", 383.5, "2023", "QCDHT12002023NanoList.txt", "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
QCDHT12002023BPix     = sample("QCDHT12002023BPix", 383.5, "2023BPix", "QCDHT12002023BPixNanoList.txt", "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM")
QCDHT15002022  = sample("QCDHT15002022", 125.2, "2022", "QCDHT15002022NanoList.txt", "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
QCDHT15002022EE     = sample("QCDHT15002022EE", 125.2, "2022EE", "QCDHT15002022EENanoList.txt", "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
QCDHT15002023     = sample("QCDHT15002023", 125.2, "2023", "QCDHT15002023NanoList.txt", "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM")
QCDHT15002023BPix     = sample("QCDHT15002023BPix", 125.2, "2023BPix", "QCDHT15002023BPixNanoList.txt", "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
QCDHT20002022  = sample("QCDHT20002022", 26.49, "2022", "QCDHT20002022NanoList.txt", "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
QCDHT20002022EE     = sample("QCDHT20002022EE", 26.49, "2022EE", "QCDHT20002022EENanoList.txt", "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
QCDHT20002023     = sample("QCDHT20002023", 26.49, "2023", "QCDHT20002023NanoList.txt", "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
QCDHT20002023BPix     = sample("QCDHT20002023BPix", 26.49, "2023BPix", "QCDHT20002023BPixNanoList.txt", "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM")
QCDHT2002022   = sample("QCDHT2002022", 1961000., "2022", "QCDHT2002022NanoList.txt", "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
QCDHT2002022EE      = sample("QCDHT2002022EE", 1961000., "2022EE", "QCDHT2002022EENanoList.txt", "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
QCDHT2002023      = sample("QCDHT2002023", 1961000., "2023", "QCDHT2002023NanoList.txt", "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
QCDHT2002023BPix      = sample("QCDHT2002023BPix", 1961000., "2023BPix", "QCDHT2002023BPixNanoList.txt", "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
QCDHT4002022   = sample("QCDHT4002022", 95620., "2022", "QCDHT4002022NanoList.txt", "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
QCDHT4002022EE      = sample("QCDHT4002022EE", 95620., "2022EE", "QCDHT4002022EENanoList.txt", "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
QCDHT4002023      = sample("QCDHT4002023", 95620., "2023", "QCDHT4002023NanoList.txt", "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM")
QCDHT4002023BPix      = sample("QCDHT4002023BPix", 95620., "2023BPix", "QCDHT4002023BPixNanoList.txt", "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM")
QCDHT6002022   = sample("QCDHT6002022", 13540., "2022", "QCDHT6002022NanoList.txt", "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
QCDHT6002022EE      = sample("QCDHT6002022EE", 13540., "2022EE", "QCDHT6002022EENanoList.txt", "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
QCDHT6002023      = sample("QCDHT6002023", 13540., "2023", "QCDHT6002023NanoList.txt", "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
QCDHT6002023BPix      = sample("QCDHT6002023BPix", 13540., "2023BPix", "QCDHT6002023BPixNanoList.txt", "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
QCDHT8002022   = sample("QCDHT8002022", 3033., "2022", "QCDHT8002022NanoList.txt", "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
QCDHT8002022EE      = sample("QCDHT8002022EE", 3033., "2022EE", "QCDHT8002022EENanoList.txt", "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
QCDHT8002023      = sample("QCDHT8002023", 3033., "2023", "QCDHT8002023NanoList.txt", "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
QCDHT8002023BPix      = sample("QCDHT8002023BPix", 3033., "2023BPix", "QCDHT8002023BPixNanoList.txt", "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v4/NANOAODSIM")

SingleElecRun2022C = sample("SingleElecRun2022C", 1.0, "2022", "SingleElecRun2022C2022NanoList.txt", "/EGamma/Run2022C-22Sep2023-v1/NANOAOD")
SingleElecRun2022D = sample("SingleElecRun2022D", 1.0, "2022", "SingleElecRun2022D2022NanoList.txt", "/EGamma/Run2022D-22Sep2023-v1/NANOAOD")
SingleElecRun2022EEE  = sample("SingleElecRun2022EEE", 1.0, "2022EE", "SingleElecRun2022EEE2022EENanoList.txt", "/EGamma/Run2022E-22Sep2023-v1/NANOAOD")
SingleElecRun2022EEF  = sample("SingleElecRun2022EEF", 1.0, "2022EE", "SingleElecRun2022EEF2022EENanoList.txt", "/EGamma/Run2022F-22Sep2023-v1/NANOAOD")
SingleElecRun2022EEG  = sample("SingleElecRun2022EEG", 1.0, "2022EE", "SingleElecRun2022EEG2022EENanoList.txt", "/EGamma/Run2022G-22Sep2023-v2/NANOAOD")
SingleElecRun2023C01  = sample("SingleElecRun2023C01", 1.0, "2023", "SingleElecRun2023C012023NanoList.txt", "/EGamma0/Run2023C-22Sep2023_v1-v1/NANOAOD")
SingleElecRun2023C02  = sample("SingleElecRun2023C02", 1.0, "2023", "SingleElecRun2023C022023NanoList.txt", "/EGamma0/Run2023C-22Sep2023_v2-v1/NANOAOD")
SingleElecRun2023C03  = sample("SingleElecRun2023C03", 1.0, "2023", "SingleElecRun2023C032023NanoList.txt", "/EGamma0/Run2023C-22Sep2023_v3-v1/NANOAOD")
SingleElecRun2023C04  = sample("SingleElecRun2023C04", 1.0, "2023", "SingleElecRun2023C042023NanoList.txt", "/EGamma0/Run2023C-22Sep2023_v4-v1/NANOAOD")
SingleElecRun2023C11  = sample("SingleElecRun2023C11", 1.0, "2023", "SingleElecRun2023C112023NanoList.txt", "/EGamma1/Run2023C-22Sep2023_v1-v1/NANOAOD")
SingleElecRun2023C12  = sample("SingleElecRun2023C12", 1.0, "2023", "SingleElecRun2023C122023NanoList.txt", "/EGamma1/Run2023C-22Sep2023_v2-v1/NANOAOD")
SingleElecRun2023C13  = sample("SingleElecRun2023C13", 1.0, "2023", "SingleElecRun2023C132023NanoList.txt", "/EGamma1/Run2023C-22Sep2023_v3-v1/NANOAOD")
SingleElecRun2023C14  = sample("SingleElecRun2023C14", 1.0, "2023", "SingleElecRun2023C142023NanoList.txt", "/EGamma1/Run2023C-22Sep2023_v4-v1/NANOAOD")
SingleElecRun2023BPixD01  = sample("SingleElecRun2023BPixD01", 1.0, "2023BPix", "SingleElecRun2023BPixD012023BPixNanoList.txt", "/EGamma0/Run2023D-22Sep2023_v1-v1/NANOAOD")
SingleElecRun2023BPixD02  = sample("SingleElecRun2023BPixD02", 1.0, "2023BPix", "SingleElecRun2023BPixD022023BPixNanoList.txt", "/EGamma0/Run2023D-22Sep2023_v2-v1/NANOAOD")
SingleElecRun2023BPixD11  = sample("SingleElecRun2023BPixD11", 1.0, "2023BPix", "SingleElecRun2023BPixD112023BPixNanoList.txt", "/EGamma1/Run2023D-22Sep2023_v1-v1/NANOAOD")
SingleElecRun2023BPixD12  = sample("SingleElecRun2023BPixD12", 1.0, "2023BPix", "SingleElecRun2023BPixD122023BPixNanoList.txt", "/EGamma1/Run2023D-22Sep2023_v2-v1/NANOAOD")

SingleMuonRun2022C = sample("SingleMuonRun2022C", 1.0, "2022", "SingleMuonRun2022C2022NanoList.txt", "/Muon/Run2022C-22Sep2023-v1/NANOAOD")
SingleMuonRun2022D = sample("SingleMuonRun2022D", 1.0, "2022", "SingleMuonRun2022D2022NanoList.txt", "/Muon/Run2022D-22Sep2023-v1/NANOAOD")
SingleMuonRun2022EEE  = sample("SingleMuonRun2022EEE", 1.0, "2022EE", "SingleMuonRun2022EEE2022EENanoList.txt", "/Muon/Run2022E-22Sep2023-v1/NANOAOD")
SingleMuonRun2022EEF  = sample("SingleMuonRun2022EEF", 1.0, "2022EE", "SingleMuonRun2022EEF2022EENanoList.txt", "/Muon/Run2022F-22Sep2023-v2/NANOAOD")
SingleMuonRun2022EEG  = sample("SingleMuonRun2022EEG", 1.0, "2022EE", "SingleMuonRun2022EEG2022EENanoList.txt", "/Muon/Run2022G-22Sep2023-v1/NANOAOD")
SingleMuonRun2023C01  = sample("SingleMuonRun2023C01", 1.0, "2023", "SingleMuonRun2023C012023NanoList.txt", "/Muon0/Run2023C-22Sep2023_v1-v1/NANOAOD")
SingleMuonRun2023C02  = sample("SingleMuonRun2023C02", 1.0, "2023", "SingleMuonRun2023C022023NanoList.txt", "/Muon0/Run2023C-22Sep2023_v2-v1/NANOAOD")
SingleMuonRun2023C03  = sample("SingleMuonRun2023C03", 1.0, "2023", "SingleMuonRun2023C032023NanoList.txt", "/Muon0/Run2023C-22Sep2023_v3-v1/NANOAOD")
SingleMuonRun2023C04  = sample("SingleMuonRun2023C04", 1.0, "2023", "SingleMuonRun2023C042023NanoList.txt", "/Muon0/Run2023C-22Sep2023_v4-v1/NANOAOD")
SingleMuonRun2023C11  = sample("SingleMuonRun2023C11", 1.0, "2023", "SingleMuonRun2023C112023NanoList.txt", "/Muon1/Run2023C-22Sep2023_v1-v1/NANOAOD")
SingleMuonRun2023C12  = sample("SingleMuonRun2023C12", 1.0, "2023", "SingleMuonRun2023C122023NanoList.txt", "/Muon1/Run2023C-22Sep2023_v2-v1/NANOAOD")
SingleMuonRun2023C13  = sample("SingleMuonRun2023C13", 1.0, "2023", "SingleMuonRun2023C132023NanoList.txt", "/Muon1/Run2023C-22Sep2023_v3-v1/NANOAOD")
SingleMuonRun2023C14  = sample("SingleMuonRun2023C14", 1.0, "2023", "SingleMuonRun2023C142023NanoList.txt", "/Muon1/Run2023C-22Sep2023_v4-v2/NANOAOD")
SingleMuonRun2023BPixD01  = sample("SingleMuonRun2023BPixD01", 1.0, "2023BPix", "SingleMuonRun2023BPixD012023BPixNanoList.txt", "/Muon0/Run2023D-22Sep2023_v1-v1/NANOAOD")
SingleMuonRun2023BPixD02  = sample("SingleMuonRun2023BPixD02", 1.0, "2023BPix", "SingleMuonRun2023BPixD022023BPixNanoList.txt", "/Muon0/Run2023D-22Sep2023_v2-v1/NANOAOD")
SingleMuonRun2023BPixD11  = sample("SingleMuonRun2023BPixD11", 1.0, "2023BPix", "SingleMuonRun2023BPixD112023BPixNanoList.txt", "/Muon1/Run2023D-22Sep2023_v1-v1/NANOAOD")
SingleMuonRun2023BPixD12  = sample("SingleMuonRun2023BPixD12", 1.0, "2023BPix", "SingleMuonRun2023BPixD122023BPixNanoList.txt", "/Muon1/Run2023D-22Sep2023_v2-v1/NANOAOD")

STs2022 = sample("STs2022", 7.244*0.333, "2022", "STs2022NanoList.txt", "/TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
STs2022EE = sample("STs2022EE", 7.244*0.333, "2022EE", "STs2022EENanoList.txt", "/TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
STs2023 = sample("STs2023", 7.244*0.333, "2023", "STs2023NanoList.txt", "/TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
STs2023BPix = sample("STs2023BPix", 7.244*0.333, "2023BPix", "STs2023BPixNanoList.txt", "/TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
STbs2022 = sample("STbs2022", 4.534*0.333, "2022", "STbs2022NanoList.txt", "/TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
STbs2022EE = sample("STbs2022EE", 4.534*0.333, "2022EE", "STbs2022EENanoList.txt", "/TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
STbs2023 = sample("STbs2023", 4.534*0.333, "2023", "STbs2023NanoList.txt", "/TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
STbs2023BPix = sample("STbs2023BPix", 4.534*0.333, "2023BPix", "STbs2023BPixNanoList.txt", "/TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

STt2022 = sample("STt2022", 145.0, "2022", "STt2022NanoList.txt", "/TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
STt2022EE = sample("STt2022EE", 145.0, "2022EE", "STt2022EENanoList.txt", "/TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
STt2023 = sample("STt2023", "2023", 145.0, "STt2023NanoList.txt", "/TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
STt2023BPix = sample("STt2023BPix", 145.0, "2023BPix", "STt2023BPixNanoList.txt", "/TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
STtb2022 = sample("STtb2022", 87.2, "2022", "STtb2022NanoList.txt", "/TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
STtb2022EE = sample("STtb2022EE", 87.2, "2022EE", "STtb2022EENanoList.txt", "/TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
STtb2023 = sample("STtb2023", 87.2, "2023", "STtb2023NanoList.txt", "/TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
STtb2023BPix = sample("STtb2023BPix", 87.2, "2023BPix", "STtb2023BPixNanoList.txt", "/TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

# 2L2Nu and 4Q exist, can add if needed
STtW2022 = sample("STtW2022", 43.95, "2022", "STtW2022NanoList.txt", "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
STtW2022ext = sample("STtW2022ext", 43.95, "2022", "STtW2022extNanoList.txt", "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
STtW2022EE = sample("STtW2022EE", 43.95, "2022EE", "STtW2022EENanoList.txt", "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
STtW2022EEext = sample("STtW2022EEext", 43.95, "2022EE", "STtW2022EEextNanoList.txt", "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
STtW2023 = sample("STtW2023", 43.95, "2023", "STtW2023NanoList.txt", "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
STtW2023BPix = sample("STtW2023BPix", 43.95, "2023BPix", "STtW2023BPixNanoList.txt", "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
STtWb2022 = sample("STtWb2022", 43.95, "2022", "STtWb2022NanoList.txt", "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
STtWb2022ext = sample("STtWb2022ext", 43.95, "2022", "STtWb2022extNanoList.txt", "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
STtWb2022EE = sample("STtWb2022EE", 43.95, "2022EE", "STtWb2022EENanoList.txt", "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
STtWb2022EEext = sample("STtWb2022EEext", 43.95, "2022EE", "STtWb2022EEextNanoList.txt", "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
STtWb2023 = sample("STtWb2023", 43.95, "2023", "STtWb2023NanoList.txt", "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
STtWb2023BPix = sample("STtWb2023BPix", 43.95, "2023BPix", "STtWb2023BPixNanoList.txt", "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")

TTHB2022 = sample("TTHB2022", 0.570*0.5824, "2022", "TTHB2022NanoList.txt", "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM")
TTHB2022EE = sample("TTHB2022EE", 0.570*0.5824, "2022EE", "TTHB2022EENanoList.txt", "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM")
TTHB2023 = sample("TTHB2023", 0.570*0.5824, "2023", "TTHB2023NanoList.txt", "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM")
TTHB2023BPix = sample("TTHB2023BPix", 0.570*0.5824, "2023BPix", "TTHB2023BPixNanoList.txt", "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
TTHnonB2022 = sample("TTHnonB2022", 0.570*(1.0-0.5824), "2022", "TTHnonB2022NanoList.txt", "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM")
TTHnonB2022EE = sample("TTHnonB2022EE", 0.570*(1.0-0.05824), "2022EE", "TTHnonB2022EENanoList.txt", "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTHnonB2023 = sample("TTHnonB2023", 0.570*(1.0-0.05824), "2023", "TTHnonB2023NanoList.txt", "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
TTHnonB2023BPix = sample("TTHnonB2023BPix", 0.570*(1.0-0.05824), "2023BPix", "TTHnonB2023BPixNanoList.txt", "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")

#TTMT10002022 = sample("TTMT10002022", 1.0, "2022", "TTMT10002022NanoList.txt", "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
#TTMT10002022EE = sample("TTMT10002022EE", 1.0, "2022EE", "TTMT10002022EENanoList.txt", "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
#TTMT10002023 = sample("TTMT10002023", 1.0, "2023", "TTMT10002023NanoList.txt", "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
#TTMT10002023BPix = sample("TTMT10002023BPix", 1.0, "2023BPix", "TTMT10002023BPixNanoList.txt", "/TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")
#TTMT7002022 = sample("TTMT7002022", 1.0, "2022", "TTMT7002022NanoList.txt", "/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM")
#TTMT7002022EE = sample("TTMT7002022EE", 1.0, "2022EE", "TTMT7002022EENanoList.txt", "/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
#TTMT7002023 = sample("TTMT7002023", 1.0, "2023", "TTMT7002023NanoList.txt", "/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
#TTMT7002023BPix = sample("TTMT7002023BPix", 1.0, "2023BPix", "TTMT7002023BPixNanoList.txt", "/TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")

TTTo2L2Nu2022 = sample("TTTo2L2Nu2022", 923.6*0.105, "2022", "TTTo2L2Nu2022NanoList.txt", "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTTo2L2Nu2022ext = sample("TTTo2L2Nu2022ext", 923.6*0.105, "2022", "TTTo2L2Nu2022extNanoList.txt", "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
TTTo2L2Nu2022EE = sample("TTTo2L2Nu2022EE", 923.6*0.105, "2022EE", "TTTo2L2Nu2022EENanoList.txt", "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTTo2L2Nu2022EEext = sample("TTTo2L2Nu2022EEext", 923.6*0.105, "2022EE", "TTTo2L2Nu2022EEextNanoList.txt", "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
TTTo2L2Nu2023 = sample("TTTo2L2Nu2023", 923.6*0.105, "2023", "TTTo2L2Nu2023NanoList.txt", "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
TTTo2L2Nu2023BPix = sample("TTTo2L2Nu2023BPix", 923.6*0.105, "2023BPix", "TTTo2L2Nu2023BPixNanoList.txt", "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
TTToHadronic2022 = sample("TTToHadronic2022", 923*0.457, "2022", "TTToHadronic2022NanoList.txt", "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTToHadronic2022ext = sample("TTToHadronic2022ext", 923*0.457, "2022", "TTToHadronic2022extNanoList.txt", "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
TTToHadronic2022EE = sample("TTToHadronic2022EE", 923*0.457, "2022EE", "TTToHadronic2022EENanoList.txt", "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTToHadronic2022EEext = sample("TTToHadronic2022EEext", 923*0.457, "2022EE", "TTToHadronic2022EEextNanoList.txt", "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
TTToHadronic2023 = sample("TTToHadronic2023", 923*0.457, "2023", "TTToHadronic2023NanoList.txt", "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
TTToHadronic2023BPix = sample("TTToHadronic2023BPix", 923*0.457, "2023BPix", "TTToHadronic2023BPixNanoList.txt", "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
TTToSemiLeptonic2022 = sample("TTToSemiLeptonic2022", 923*0.438, "2022", "TTToSemiLeptonic2022NanoList.txt", "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTToSemiLeptonic2022ext = sample("TTToSemiLeptonic2022ext", 923*0.438, "2022", "TTToSemiLeptonic2022extNanoList.txt", "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
TTToSemiLeptonic2022EE = sample("TTToSemiLeptonic2022EE", 923*0.438, "2022EE", "TTToSemiLeptonic2022EENanoList.txt", "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTToSemiLeptonic2022EEext = sample("TTToSemiLeptonic2022EEext", 923*0.438, "2022EE", "TTToSemiLeptonic2022EEextNanoList.txt", "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
TTToSemiLeptonic2023 = sample("TTToSemiLeptonic2023", 923*0.438, "2023", "TTToSemiLeptonic2023NanoList.txt", "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
TTToSemiLeptonic2023BPix = sample("TTToSemiLeptonic2023BPix", 923*0.438, "2023BPix", "TTToSemiLeptonic2023BPixNanoList.txt", "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")

TTWl2022 = sample("TTWl2022", 0.2505, "2022", "TTWl2022NanoList.txt", "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-mg35x_130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTWl2022EE = sample("TTWl2022EE", 0.2505, "2022EE", "TTWl2022EENanoList.txt", "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-mg35x_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTWl2023 = sample("TTWl2023", 0.2505, "2023", "TTWl2023NanoList.txt", "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-mg35x_130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTWl2023BPix = sample("TTWl2023BPix", 0.2505, "2023BPix", "TTWl2023BPixNanoList.txt", "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-mg35x_130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
# not using W to hadrons for 4tau2tb, old sample names from Run 2
TTWq2022 = sample("TTWq2022", 1.0, "2022", "TTWq2022NanoList.txt", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTWq2022EE = sample("TTWq2022EE", 1.0, "2022EE", "TTWq2022EENanoList.txt", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer2022NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM")
TTWq2023 = sample("TTWq2023", 1.0, "2023", "TTWq2023NanoList.txt", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer2023NanoAODv9-106X_mc2023_realistic_v9-v1/NANOAODSIM")
TTWq2023BPix = sample("TTWq2023BPix", 1.0, "2023BPix", "TTWq2023BPixNanoList.txt", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer2023NanoAODv9-106X_upgrade2023BPix_realistic_v16_L1v1-v1/NANOAODSIM")

WJetsHT1002022 = sample("WJetsHT1002022", 1626., "2022", "WJetsHT1002022NanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM")
WJetsHT1002022EE = sample("WJetsHT1002022EE", 1626., "2022EE", "WJetsHT1002022EENanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM")
WJetsHT1002023 = sample("WJetsHT1002023", 1626., "2023", "WJetsHT1002023NanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
WJetsHT1002023BPix = sample("WJetsHT1002023BPix", 1626., "2023BPix", "WJetsHT1002023BPixNanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
WJetsHT15002022 = sample("WJetsHT15002022", 0.4477, "2022", "WJetsHT15002022NanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WJetsHT15002022EE = sample("WJetsHT15002022EE", 0.4477, "2022EE", "WJetsHT15002022EENanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WJetsHT15002023 = sample("WJetsHT15002023", 0.4477, "2023", "WJetsHT15002023NanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM")
WJetsHT15002023BPix = sample("WJetsHT15002023BPix", 0.4477, "2023BPix", "WJetsHT15002023BPixNanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
WJetsHT25002022 = sample("WJetsHT25002022", 0.03075, "2022", "WJetsHT25002022NanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WJetsHT25002022EE = sample("WJetsHT25002022EE", 0.03075, "2022EE", "WJetsHT25002022EENanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WJetsHT25002023 = sample("WJetsHT25002023", 0.03075, "2023", "WJetsHT25002023NanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM")
WJetsHT25002023BPix = sample("WJetsHT25002023BPix", 0.03075, "2023BPix", "WJetsHT25002023BPixNanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM") #invalid
WJetsHT4002022 = sample("WJetsHT4002022", 59.99, "2022", "WJetsHT4002022NanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM")
WJetsHT4002022EE = sample("WJetsHT4002022EE", 59.99, "2022EE", "WJetsHT4002022EENanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM")
WJetsHT4002023 = sample("WJetsHT4002023", 59.99, "2023", "WJetsHT4002023NanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
WJetsHT4002023BPix = sample("WJetsHT4002023BPix", 59.99, "2023BPix", "WJetsHT4002023BPixNanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
WJetsHT8002022 = sample("WJetsHT8002022", 6.23, "2022", "WJetsHT8002022NanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WJetsHT8002022EE = sample("WJetsHT8002022EE", 6.23, "2022EE", "WJetsHT8002022EENanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WJetsHT8002023 = sample("WJetsHT8002023", 6.23, "2023", "WJetsHT8002023NanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v5/NANOAODSIM")
WJetsHT8002023BPix = sample("WJetsHT8002023BPix", 6.23, "2023BPix", "WJetsHT8002023BPixNanoList.txt", "/WtoLNu-4Jets_MLNu-0to120_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
WJetsM120HT1002022 = sample("WJetsM120HT1002022", 10.19, "2022", "WJetsM120HT1002022NanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WJetsM120HT1002022EE = sample("WJetsM120HT1002022EE", 10.19, "2022EE", "WJetsM120HT1002022EENanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WJetsM120HT1002023 = sample("WJetsM120HT1002023", 10.19, "2023", "WJetsM120HT1002023NanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM")
WJetsM120HT1002023BPix = sample("WJetsM120HT1002023BPix", 10.19, "2023BPix", "WJetsM120HT1002023BPixNanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
WJetsM120HT15002022 = sample("WJetsM120HT15002022", 0.005066, "2022", "WJetsM120HT15002022NanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WJetsM120HT15002022EE = sample("WJetsM120HT15002022EE", 0.005066, "2022EE", "WJetsM120HT15002022EENanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WJetsM120HT15002023 = sample("WJetsM120HT15002023", 0.005066, "2023", "WJetsM120HT15002023NanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM")
WJetsM120HT15002023BPix = sample("WJetsM120HT15002023BPix", 0.005066, "2023BPix", "WJetsM120HT15002023BPixNanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
WJetsM120HT25002022 = sample("WJetsM120HT25002022", 0.0003788, "2022", "WJetsM120HT25002022NanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WJetsM120HT25002022EE = sample("WJetsM120HT25002022EE", 0.0003788, "2022EE", "WJetsM120HT25002022EENanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WJetsM120HT25002023 = sample("WJetsM120HT25002023", 0.0003788, "2023", "WJetsM120HT25002023NanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM")
WJetsM120HT25002023BPix = sample("WJetsM120HT25002023BPix", 0.0003788, "2023BPix", "WJetsM120HT25002023BPixNanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
WJetsM120HT4002022 = sample("WJetsM120HT4002022", 0.5239, "2022", "WJetsM120HT4002022NanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WJetsM120HT4002022EE = sample("WJetsM120HT4002022EE", 0.5239, "2022EE", "WJetsM120HT4002022EENanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WJetsM120HT4002023 = sample("WJetsM120HT4002023", 0.5239, "2023", "WJetsM120HT4002023NanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM")
WJetsM120HT4002023BPix = sample("WJetsM120HT4002023BPix", 0.5239, "2023BPix", "WJetsM120HT4002023BPixNanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM") #invalid
WJetsM120HT8002022 = sample("WJetsM120HT8002022", 0.06255, "2022", "WJetsM120HT8002022NanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WJetsM120HT8002022EE = sample("WJetsM120HT8002022EE", 0.06255, "2022EE", "WJetsM120HT8002022EENanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WJetsM120HT8002023 = sample("WJetsM120HT8002023", 0.06255, "2023", "WJetsM120HT8002023NanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM")
WJetsM120HT8002023BPix = sample("WJetsM120HT8002023BPix", 0.06255, "2023BPix", "WJetsM120HT8002023BPixNanoList.txt", "/WtoLNu-4Jets_MLNu-120_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v3/NANOAODSIM")

# 4Q exists, could add if needed
WW2L2022 = sample("WW2L2022", 11.79, "2022", "WW2L2022NanoList.txt", "/WWto2L2Nu-2Jets_OS_noTop_EW-QCD_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WW2L2022ext = sample("WW2L2022ext", 11.79, "2022", "WW2L2022extNanoList.txt", "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
WW2L2022EE = sample("WW2L2022EE", 11.79, "2022EE", "WW2L2022EENanoList.txt", "/WWto2L2Nu-2Jets_OS_noTop_EW-QCD_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WW2L2022EEext = sample("WW2L2022EEext", 11.79, "2022EE", "WW2L2022EEextNanoList.txt", "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
WW2L2023 = sample("WW2L2023", 11.79, "2023", "WW2L2023NanoList.txt", "/WWto2L2Nu-2Jets_OS_noTop_EW-QCD_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
WW2L2023BPix = sample("WW2L2023BPix", 11.79, "2023BPix", "WW2L2023BPixNanoList.txt", "/WWto2L2Nu-2Jets_OS_noTop_EW-QCD_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
# not using 1l for 4tau2tb
WW1L2022 = sample("WW1L2022", 48.94, "2022", "WW1L2022NanoList.txt", "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WW1L2022ext = sample("WW1L2022ext", 48.94, "2022", "WW1L2022extNanoList.txt", "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
WW1L2022EE = sample("WW1L2022EE", 48.94, "2022EE", "WW1L2022EENanoList.txt", "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WW1L2022EEext = sample("WW1L2022EEext", 48.94, "2022EE", "WW1L2022EEextNanoList.txt", "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
WW1L2023 = sample("WW1L2023", 48.94, "2023", "WW1L2023NanoList.txt", "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM")
WW1L2023BPix = sample("WW1L2023BPix", 48.94, "2023BPix", "WW1L2023BPixNanoList.txt", "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")

WZ3L2022 = sample("WZ3L2022", 0.5437, "2022", "WZ3L2022NanoList.txt", "/WZto3LNu-2Jets_EWK-QCD_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WZ3L2022EE = sample("WZ3L2022EE", 0.5437, "2022EE", "WZ3L2022EENanoList.txt", "/WZto3LNu-2Jets_EWK-QCD_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WZ3L2023 = sample("WZ3L2023", "2023", 0.5437, "WZ3L2023NanoList.txt", "/WZto3LNu-2Jets_EWK-QCD_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
WZ3L2023BPix = sample("WZ3L2023BPix", 0.5437, "2023BPix", "WZ3L2023BPixNanoList.txt", "/WZto3LNu-2Jets_EWK-QCD_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
WZ2L2022 = sample("WZ2L2022", 7.568, "2022", "WZ2L2022NanoList.txt", "/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WZ2L2022ext = sample("WZ2L2022ext", 7.568, "2022", "WZ2L2022extNanoList.txt", "/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
WZ2L2022EE = sample("WZ2L2022EE", 7.568, "2022EE", "WZ2L2022EENanoList.txt", "/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WZ2L2022EEext = sample("WZ2L2022EEext", 7.568, "2022EE", "WZ2L2022EEextNanoList.txt", "/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
WZ2L2023 = sample("WZ2L2023", 7.568, "2023", "WZ2L2023NanoList.txt", "/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM")
WZ2L2023BPix = sample("WZ2L2023BPix", 7.568, "2023BPix", "WZ2L2023BPixNanoList.txt", "/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")
WZ1L2022 = sample("WZ1L2022", 15.87, "2022", "WZ1L2022NanoList.txt", "/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WZ1L2022ext = sample("WZ1L2022ext", 15.87, "2022", "WZ1L2022extNanoList.txt", "/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
WZ1L2022EE = sample("WZ1L2022EE", 15.87, "2022EE", "WZ1L2022EENanoList.txt", "/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WZ1L2022EEext = sample("WZ1L2022EEext", 15.87, "2022EE", "WZ1L2022EEextNanoList.txt", "/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
WZ1L2023 = sample("WZ1L2023", 15.87, "2023", "WZ1L2023NanoList.txt", "/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
WZ1L2023BPix = sample("WZ1L2023BPix", 15.87, "2023BPix", "WZ1L2023BPixNanoList.txt", "/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")

#Additional Samples
WWW2022     = sample("WWW2022", 0.2328, "2022", "WWW2022.txt", "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WWW2022EE   = sample("WWW2022EE", 0.2328, "2022EE", "WWW2022EE.txt", "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WWW2023     = sample("WWW2023", 0.2328, "2023", "WWW2023.txt", "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
WWW2023BPix = sample("WWW2023BPix", 0.2328, "2023BPix", "WWW2023BPix.txt", "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")
WWZ2022     = sample("WWZ2022", 0.1851, "2022", "WWZ2022.txt", "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WWZ2022EE   = sample("WWZ2022EE", 0.1851, "2022EE", "WWZ2022EE.txt", "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WWZ2023     = sample("WWZ2023", 0.1851, "2023", "WWZ2023.txt", "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
WWZ2023BPix = sample("WWZ2023BPix", 0.1851, "2023BPix", "WWZ2023BPix.txt", "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
WZZ2022     = sample("WZZ2022", 0.06206, "2022", "WZZ2022.txt", "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WZZ2022EE   = sample("WZZ2022EE", 0.06206, "2022EE", "WZZ2022EE.txt", "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WZZ2023     = sample("WZZ2023", 0.06206, "2023", "WZZ2023.txt", "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
WZZ2023BPix = sample("WZZ2023BPix", 0.06206, "2023BPix", "WZZ2023BPix.txt", "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")
ZZZ2022     = sample("ZZZ2022", 0.01591, "2022", "ZZZ2022.txt", "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
ZZZ2022EE   = sample("ZZZ2022EE", 0.01591, "2022EE", "ZZZ2022EE.txt", "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
ZZZ2023     = sample("ZZZ2023", 0.01591, "2023", "ZZZ2023.txt", "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
ZZZ2023BPix = sample("ZZZ2023BPix", 0.01591, "2023BPix", "ZZZ2023BPix.txt", "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")

TTWH2022     = sample("TTWH2022", 0.001252, "2022", "TTWH2022.txt", "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTWH2022EE   = sample("TTWH2022EE", 0.001252, "2022EE", "TTWH2022EE.txt", "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTWH2023     = sample("TTWH2023", 0.001252, "2023", "TTWH2023.txt", "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM")
TTWH2023BPix = sample("TTWH2023BPix", 0.001252, "2023BPix", "TTWH2023BPix.txt", "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTWW2022     = sample("TTWW2022", 0.008203, "2022", "TTWW2022.txt", "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTWW2022EE   = sample("TTWW2022EE", 0.008203, "2022EE", "TTWW2022EE.txt", "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTWW2023     = sample("TTWW2023", 0.008203, "2023", "TTWW2023.txt", "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTWW2023BPix = sample("TTWW2023BPix", 0.008203, "2023BPix", "TTWW2023BPix.txt", "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTWZ2022     = sample("TTWZ2022", 0.002715, "2022", "TTWZ2022.txt", "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTWZ2022EE   = sample("TTWZ2022EE", 0.002715, "2022EE", "TTWZ2022EE.txt", "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTWZ2023     = sample("TTWZ2023", 0.002715, "2023", "TTWZ2023.txt", "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTWZ2023BPix = sample("TTWZ2023BPix", 0.002715, "2023BPix", "TTWZ2023BPix.txt", "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTZH2022     = sample("TTZH2022", 0.001288, "2022", "TTZH2022.txt", "/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTZH2022EE   = sample("TTZH2022EE", 0.001288, "2022EE", "TTZH2022EE.txt", "/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM")
TTZH2023     = sample("TTZH2023", 0.001288, "2023", "TTZH2023.txt", "/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM")
TTZH2023BPix = sample("TTZH2023BPix", 0.001288, "2023BPix", "TTZH2023BPix.txt", "/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTZZ2022     = sample("TTZZ2022", 0.001579, "2022", "TTZZ2022NanoList.txt", "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTZZ2022EE   = sample("TTZZ2022EE", 0.001579, "2022EE", "TTZZ2022EENanoList.txt", "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM")
TTZZ2023     = sample("TTZZ2023", 0.001579, "2023", "TTZZ2023NanoList.txt", "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM")
TTZZ2023BPix = sample("TTZZ2023BPix", 0.001579, "2023BPix", "TTZZ2023BPixNanoList.txt", "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTTT2022     = sample("TTTT2022", 0.009652, "2022", "TTTT2022NanoList.txt", "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTTT2022EE   = sample("TTTT2022EE", 0.009652, "2022EE", "TTTT2022EENanoList.txt", "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM")
TTTT2023     = sample("TTTT2023", 0.009652, "2023", "TTTT2023NanoList.txt", "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTTT2023BPix = sample("TTTT2023BPix", 0.009652, "2023BPix", "TTTT2023BPixNanoList.txt", "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

WWZZ3L2022     = sample("WWZZ3L2022", 0.0004888, "2022", "WWZZ3L2022NanoList.txt", "/WWZZ_3L_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WWZZ3L2022EE   = sample("WWZZ3L2022EE", 0.0004888, "2022EE", "WWZZ3L2022EENanoList.txt", "/WWZZ_3L_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WWZZ3L2023     = sample("WWZZ3L2023", 0.0004888, "2023", "WWZZ3L2023NanoList.txt", "/WWZZ_3L_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
WWZZ3L2023BPix = sample("WWZZ3L2023BPix", 0.0004888, "2023BPix", "WWZZ3L2023BPixNanoList.txt", "/WWZZ_3L_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
WWZZ4L2022     = sample("WWZZ4L2022", 0.0004888, "2022", "WWZZ4L2022NanoList.txt", "/WWZZ_4Lplus_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WWZZ4L2022EE   = sample("WWZZ4L2022EE", 0.0004888, "2022EE", "WWZZ4L2022EENanoList.txt", "/WWZZ_4Lplus_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WWZZ4L2023     = sample("WWZZ4L2023", 0.0004888, "2023", "WWZZ4L2023NanoList.txt", "/WWZZ_4Lplus_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
WWZZ4L2023BPix = sample("WWZZ4L2023BPix", 0.0004888, "2023BPix", "WWZZ4L2023BPixNanoList.txt", "/WWZZ_4Lplus_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

MuonEGRun2022C = sample("MuonEGRun2022C", 1.0, "2022", "MuonEGRun2022C2022NanoList.txt", "/MuonEG/Run2022C-22Sep2023-v1/NANOAOD")
MuonEGRun2022D = sample("MuonEGRun2022D", 1.0, "2022", "MuonEGRun2022D2022NanoList.txt", "/MuonEG/Run2022D-22Sep2023-v1/NANOAOD")
MuonEGRun2022EEE  = sample("MuonEGRun2022EEE", 1.0, "2022EE", "MuonEGRun2022EEE2022EENanoList.txt", "/MuonEG/Run2022E-22Sep2023-v1/NANOAOD")
MuonEGRun2022EEF  = sample("MuonEGRun2022EEF", 1.0, "2022EE", "MuonEGRun2022EEF2022EENanoList.txt", "/MuonEG/Run2022F-22Sep2023-v1/NANOAOD")
MuonEGRun2022EEG  = sample("MuonEGRun2022EEG", 1.0, "2022EE", "MuonEGRun2022EEG2022EENanoList.txt", "/MuonEG/Run2022G-22Sep2023-v1/NANOAOD")
MuonEGRun2023C01  = sample("MuonEGRun2023C01", 1.0, "2023", "MuonEGRun2023C012023NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v1-v1/NANOAOD")
MuonEGRun2023C02  = sample("MuonEGRun2023C02", 1.0, "2023", "MuonEGRun2023C022023NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v2-v1/NANOAOD")
MuonEGRun2023C03  = sample("MuonEGRun2023C03", 1.0, "2023", "MuonEGRun2023C032023NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v3-v1/NANOAOD")
MuonEGRun2023C04  = sample("MuonEGRun2023C04", 1.0, "2023", "MuonEGRun2023C042023NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v4-v1/NANOAOD")
MuonEGRun2023BPixD01  = sample("MuonEGRun2023BPixD01", 1.0, "2023BPix", "MuonEGRun2023BPixD012023BPixNanoList.txt", "/MuonEG/Run2023D-22Sep2023_v1-v1/NANOAOD")
MuonEGRun2023BPixD02  = sample("MuonEGRun2023BPixD02", 1.0, "2023BPix", "MuonEGRun2023BPixD022023BPixNanoList.txt", "/MuonEG/Run2023D-22Sep2023_v2-v1/NANOAOD")

TauRun2022C = sample("TauRun2022C", 1.0, "2022", "TauRun2022C2022NanoList.txt", "/Tau/Run2022C-22Sep2023-v1/NANOAOD")
TauRun2022D = sample("TauRun2022D", 1.0, "2022", "TauRun2022D2022NanoList.txt", "/Tau/Run2022D-22Sep2023-v1/NANOAOD")
TauRun2022EEE  = sample("TauRun2022EEE", 1.0, "2022EE", "TauRun2022EEE2022EENanoList.txt", "/Tau/Run2022E-22Sep2023-v1/NANOAOD")
TauRun2022EEF  = sample("TauRun2022EEF", 1.0, "2022EE", "TauRun2022EEF2022EENanoList.txt", "/Tau/Run2022F-22Sep2023-v1/NANOAOD")
TauRun2022EEG  = sample("TauRun2022EEG", 1.0, "2022EE", "TauRun2022EEG2022EENanoList.txt", "/Tau/Run2022G-22Sep2023-v1/NANOAOD")
TauRun2023C01  = sample("TauRun2023C01", 1.0, "2023", "TauRun2023C012023NanoList.txt", "/Tau/Run2023C-22Sep2023_v1-v2/NANOAOD")
TauRun2023C02  = sample("TauRun2023C02", 1.0, "2023", "TauRun2023C022023NanoList.txt", "/Tau/Run2023C-22Sep2023_v2-v1/NANOAOD")
TauRun2023C03  = sample("TauRun2023C03", 1.0, "2023", "TauRun2023C032023NanoList.txt", "/Tau/Run2023C-22Sep2023_v3-v1/NANOAOD")
TauRun2023C04  = sample("TauRun2023C04", 1.0, "2023", "TauRun2023C042023NanoList.txt", "/Tau/Run2023C-22Sep2023_v4-v1/NANOAOD")
TauRun2023BPixD01  = sample("TauRun2023BPixD01", 1.0, "2023BPix", "TauRun2023BPixD012023BPixNanoList.txt", "/Tau/Run2023D-22Sep2023_v1-v1/NANOAOD")
TauRun2023BPixD02  = sample("TauRun2023BPixD02", 1.0, "2023BPix", "TauRun2023BPixD022023BPixNanoList.txt", "/Tau/Run2023D-22Sep2023_v2-v1/NANOAOD")

TTZM42022 = sample("TTZM42022", 0.03949, "2022", "TTZM42022NanoList.txt", "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTZM42022EE = sample("TTZM42022EE", 0.03949, "2022EE", "TTZM42022EENanoList.txt", "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTZM42023 = sample("TTZM42023",  0.03949,"2023", "TTZM42023NanoList.txt", "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTZM42023BPix = sample("TTZM42023BPix", 0.03949, "2023BPix", "TTZM42023BPixNanoList.txt", "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTZM502022 = sample("TTZM502022", 0.08646, "2022", "TTZM502022NanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTZM502022EE = sample("TTZM502022EE", 0.08646, "2022EE", "TTZM502022EENanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTZM502023 = sample("TTZM502023", 0.08646, "2023", "TTZM502023NanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTZM502023BPix = sample("TTZM502023BPix", 0.08646, "2023BPix", "TTZM502023BPixNanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTZM502022ext = sample("TTZM502022ext", 0.08646, "2022", "TTZM502022extNanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM")
TTZM502022EEext = sample("TTZM502022EEext", 0.08646, "2022EE", "TTZM502022EEextNanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
TTZM502023ext = sample("TTZM502023ext", 0.08646, "2023", "TTZM502023extNanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15_ext1-v2/NANOAODSIM")
TTZM502023BPixext = sample("TTZM502023BPixext", 0.08646, "2023BPix", "TTZM502023BPixextNanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6_ext1-v2/NANOAODSIM")

WZ3L2022 = sample("WZ3L2022", 0.5437, "2022", "WZ3L2022NanoList.txt", "/WZto3LNu-2Jets_EWK-QCD_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WZ3L2022EE = sample("WZ3L2022EE", 0.5437, "2022EE", "WZ3L2022EENanoList.txt", "/WZto3LNu-2Jets_EWK-QCD_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WZ3L2023 = sample("WZ3L2023", "2023", 0.5437, "WZ3L2023NanoList.txt", "/WZto3LNu-2Jets_EWK-QCD_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
WZ3L2023BPix = sample("WZ3L2023BPix", 0.5437, "2023BPix", "WZ3L2023BPixNanoList.txt", "/WZto3LNu-2Jets_EWK-QCD_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

ZZ2L2022 = sample("ZZ2L2022", 0.09783, "2022", "ZZ2L2022NanoList.txt", "/ZZto2L2Nu-2Jets_EW-QCD_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
ZZ2L2022EE = sample("ZZ2L2022EE", 0.09783, "2022EE", "ZZ2L2022EENanoList.txt", "/ZZto2L2Nu-2Jets_EW-QCD_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
ZZ2L2023 = sample("ZZ2L2023", 0.09783, "2023", "ZZ2L2023NanoList.txt", "/ZZto2L2Nu-2Jets_EW-QCD_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
ZZ2L2023BPix = sample("ZZ2L2023BPix", 0.09783, "2023BPix", "ZZ2L2023BPixNanoList.txt", "/ZZto2L2Nu-2Jets_EW-QCD_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v3/NANOAODSIM")
ZZ4L2022 = sample("ZZ4L2022", 0.02157, "2022", "ZZ4L2022NanoList.txt", "/ZZto4L-2Jets_EW-QCD_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
ZZ4L2022EE = sample("ZZ4L2022EE", 0.02157, "2022EE", "ZZ4L2022EENanoList.txt", "/ZZto4L-2Jets_EW-QCD_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
ZZ4L2023 = sample("ZZ4L2023", 0.02157, "2023", "ZZ4L2023NanoList.txt", "/ZZto4L-2Jets_EW-QCD_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
ZZ4L2023BPix = sample("ZZ4L2023BPix", 0.02157, "2023BPix", "ZZ4L2023BPixNanoList.txt", "/ZZto4L-2Jets_EW-QCD_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

NonpromptSingleElecRun2022C = sample("NonpromptSingleElecRun2022C", 1.0, "2022", "SingleElecRun2022C2022NanoList.txt", "/EGamma/Run2022C-22Sep2023-v1/NANOAOD")
NonpromptSingleElecRun2022D = sample("NonpromptSingleElecRun2022D", 1.0, "2022", "SingleElecRun2022D2022NanoList.txt", "/EGamma/Run2022D-22Sep2023-v1/NANOAOD")
NonpromptSingleElecRun2022EEE  = sample("NonpromptSingleElecRun2022EEE", 1.0, "2022EE", "SingleElecRun2022EEE2022EENanoList.txt", "/EGamma/Run2022E-22Sep2023-v1/NANOAOD")
NonpromptSingleElecRun2022EEF  = sample("NonpromptSingleElecRun2022EEF", 1.0, "2022EE", "SingleElecRun2022EEF2022EENanoList.txt", "/EGamma/Run2022F-22Sep2023-v1/NANOAOD")
NonpromptSingleElecRun2022EEG  = sample("NonpromptSingleElecRun2022EEG", 1.0, "2022EE", "SingleElecRun2022EEG2022EENanoList.txt", "/EGamma/Run2022G-22Sep2023-v2/NANOAOD")
NonpromptSingleElecRun2023C01  = sample("NonpromptSingleElecRun2023C01", 1.0, "2023", "SingleElecRun2023C012023NanoList.txt", "/EGamma0/Run2023C-22Sep2023_v1-v1/NANOAOD")
NonpromptSingleElecRun2023C02  = sample("NonpromptSingleElecRun2023C02", 1.0, "2023", "SingleElecRun2023C022023NanoList.txt", "/EGamma0/Run2023C-22Sep2023_v2-v1/NANOAOD")
NonpromptSingleElecRun2023C03  = sample("NonpromptSingleElecRun2023C03", 1.0, "2023", "SingleElecRun2023C032023NanoList.txt", "/EGamma0/Run2023C-22Sep2023_v3-v1/NANOAOD")
NonpromptSingleElecRun2023C04  = sample("NonpromptSingleElecRun2023C04", 1.0, "2023", "SingleElecRun2023C042023NanoList.txt", "/EGamma0/Run2023C-22Sep2023_v4-v1/NANOAOD")
NonpromptSingleElecRun2023C11  = sample("NonpromptSingleElecRun2023C11", 1.0, "2023", "SingleElecRun2023C112023NanoList.txt", "/EGamma1/Run2023C-22Sep2023_v1-v1/NANOAOD")
NonpromptSingleElecRun2023C12  = sample("NonpromptSingleElecRun2023C12", 1.0, "2023", "SingleElecRun2023C122023NanoList.txt", "/EGamma1/Run2023C-22Sep2023_v2-v1/NANOAOD")
NonpromptSingleElecRun2023C13  = sample("NonpromptSingleElecRun2023C13", 1.0, "2023", "SingleElecRun2023C132023NanoList.txt", "/EGamma1/Run2023C-22Sep2023_v3-v1/NANOAOD")
NonpromptSingleElecRun2023C14  = sample("NonpromptSingleElecRun2023C14", 1.0, "2023", "SingleElecRun2023C142023NanoList.txt", "/EGamma1/Run2023C-22Sep2023_v4-v1/NANOAOD")
NonpromptSingleElecRun2023BPixD01  = sample("NonpromptSingleElecRun2023BPixD01", 1.0, "2023BPix", "SingleElecRun2023BPixD012023BPixNanoList.txt", "/EGamma0/Run2023D-22Sep2023_v1-v1/NANOAOD")
NonpromptSingleElecRun2023BPixD02  = sample("NonpromptSingleElecRun2023BPixD02", 1.0, "2023BPix", "SingleElecRun2023BPixD022023BPixNanoList.txt", "/EGamma0/Run2023D-22Sep2023_v2-v1/NANOAOD")
NonpromptSingleElecRun2023BPixD11  = sample("NonpromptSingleElecRun2023BPixD11", 1.0, "2023BPix", "SingleElecRun2023BPixD112023BPixNanoList.txt", "/EGamma1/Run2023D-22Sep2023_v1-v1/NANOAOD")
NonpromptSingleElecRun2023BPixD12  = sample("NonpromptSingleElecRun2023BPixD12", 1.0, "2023BPix", "SingleElecRun2023BPixD122023BPixNanoList.txt", "/EGamma1/Run2023D-22Sep2023_v2-v1/NANOAOD")

NonpromptSingleMuonRun2022C = sample("NonpromptSingleMuonRun2022C", 1.0, "2022", "SingleMuonRun2022C2022NanoList.txt", "/Muon/Run2022C-22Sep2023-v1/NANOAOD")
NonpromptSingleMuonRun2022D = sample("NonpromptSingleMuonRun2022D", 1.0, "2022", "SingleMuonRun2022D2022NanoList.txt", "/Muon/Run2022D-22Sep2023-v1/NANOAOD")
NonpromptSingleMuonRun2022EEE  = sample("NonpromptSingleMuonRun2022EEE", 1.0, "2022EE", "SingleMuonRun2022EEE2022EENanoList.txt", "/Muon/Run2022E-22Sep2023-v1/NANOAOD")
NonpromptSingleMuonRun2022EEF  = sample("NonpromptSingleMuonRun2022EEF", 1.0, "2022EE", "SingleMuonRun2022EEF2022EENanoList.txt", "/Muon/Run2022F-22Sep2023-v2/NANOAOD")
NonpromptSingleMuonRun2022EEG  = sample("NonpromptSingleMuonRun2022EEG", 1.0, "2022EE", "SingleMuonRun2022EEG2022EENanoList.txt", "/Muon/Run2022G-22Sep2023-v1/NANOAOD")
NonpromptSingleMuonRun2023C01  = sample("NonpromptSingleMuonRun2023C01", 1.0, "2023", "SingleMuonRun2023C012023NanoList.txt", "/Muon0/Run2023C-22Sep2023_v1-v1/NANOAOD")
NonpromptSingleMuonRun2023C02  = sample("NonpromptSingleMuonRun2023C02", 1.0, "2023", "SingleMuonRun2023C022023NanoList.txt", "/Muon0/Run2023C-22Sep2023_v2-v1/NANOAOD")
NonpromptSingleMuonRun2023C03  = sample("NonpromptSingleMuonRun2023C03", 1.0, "2023", "SingleMuonRun2023C032023NanoList.txt", "/Muon0/Run2023C-22Sep2023_v3-v1/NANOAOD")
NonpromptSingleMuonRun2023C04  = sample("NonpromptSingleMuonRun2023C04", 1.0, "2023", "SingleMuonRun2023C042023NanoList.txt", "/Muon0/Run2023C-22Sep2023_v4-v1/NANOAOD")
NonpromptSingleMuonRun2023C11  = sample("NonpromptSingleMuonRun2023C11", 1.0, "2023", "SingleMuonRun2023C112023NanoList.txt", "/Muon1/Run2023C-22Sep2023_v1-v1/NANOAOD")
NonpromptSingleMuonRun2023C12  = sample("NonpromptSingleMuonRun2023C12", 1.0, "2023", "SingleMuonRun2023C122023NanoList.txt", "/Muon1/Run2023C-22Sep2023_v2-v1/NANOAOD")
NonpromptSingleMuonRun2023C13  = sample("NonpromptSingleMuonRun2023C13", 1.0, "2023", "SingleMuonRun2023C132023NanoList.txt", "/Muon1/Run2023C-22Sep2023_v3-v1/NANOAOD")
NonpromptSingleMuonRun2023C14  = sample("NonpromptSingleMuonRun2023C14", 1.0, "2023", "SingleMuonRun2023C142023NanoList.txt", "/Muon1/Run2023C-22Sep2023_v4-v2/NANOAOD")
NonpromptSingleMuonRun2023BPixD01  = sample("NonpromptSingleMuonRun2023BPixD01", 1.0, "2023BPix", "SingleMuonRun2023BPixD012023BPixNanoList.txt", "/Muon0/Run2023D-22Sep2023_v1-v1/NANOAOD")
NonpromptSingleMuonRun2023BPixD02  = sample("NonpromptSingleMuonRun2023BPixD02", 1.0, "2023BPix", "SingleMuonRun2023BPixD022023BPixNanoList.txt", "/Muon0/Run2023D-22Sep2023_v2-v1/NANOAOD")
NonpromptSingleMuonRun2023BPixD11  = sample("NonpromptSingleMuonRun2023BPixD11", 1.0, "2023BPix", "SingleMuonRun2023BPixD112023BPixNanoList.txt", "/Muon1/Run2023D-22Sep2023_v1-v1/NANOAOD")
NonpromptSingleMuonRun2023BPixD12  = sample("NonpromptSingleMuonRun2023BPixD12", 1.0, "2023BPix", "SingleMuonRun2023BPixD122023BPixNanoList.txt", "/Muon1/Run2023D-22Sep2023_v2-v1/NANOAOD")

NonpromptMuonEGRun2022C = sample("NonpromptMuonEGRun2022C", 1.0, "2022", "MuonEGRun2022C2022NanoList.txt", "/MuonEG/Run2022C-22Sep2023-v1/NANOAOD")
NonpromptMuonEGRun2022D = sample("NonpromptMuonEGRun2022D", 1.0, "2022", "MuonEGRun2022D2022NanoList.txt", "/MuonEG/Run2022D-22Sep2023-v1/NANOAOD")
NonpromptMuonEGRun2022EEE  = sample("NonpromptMuonEGRun2022EEE", 1.0, "2022EE", "MuonEGRun2022EEE2022EENanoList.txt", "/MuonEG/Run2022E-22Sep2023-v1/NANOAOD")
NonpromptMuonEGRun2022EEF  = sample("NonpromptMuonEGRun2022EEF", 1.0, "2022EE", "MuonEGRun2022EEF2022EENanoList.txt", "/MuonEG/Run2022F-22Sep2023-v1/NANOAOD")
NonpromptMuonEGRun2022EEG  = sample("NonpromptMuonEGRun2022EEG", 1.0, "2022EE", "MuonEGRun2022EEG2022EENanoList.txt", "/MuonEG/Run2022G-22Sep2023-v1/NANOAOD")
NonpromptMuonEGRun2023C01  = sample("NonpromptMuonEGRun2023C01", 1.0, "2023", "MuonEGRun2023C012023NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v1-v1/NANOAOD")
NonpromptMuonEGRun2023C02  = sample("NonpromptMuonEGRun2023C02", 1.0, "2023", "MuonEGRun2023C022023NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v2-v1/NANOAOD")
NonpromptMuonEGRun2023C03  = sample("NonpromptMuonEGRun2023C03", 1.0, "2023", "MuonEGRun2023C032023NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v3-v1/NANOAOD")
NonpromptMuonEGRun2023C04  = sample("NonpromptMuonEGRun2023C04", 1.0, "2023", "MuonEGRun2023C042023NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v4-v1/NANOAOD")
NonpromptMuonEGRun2023BPixD01  = sample("NonpromptMuonEGRun2023BPixD01", 1.0, "2023BPix", "MuonEGRun2023BPixD012023BPixNanoList.txt", "/MuonEG/Run2023D-22Sep2023_v1-v1/NANOAOD")
NonpromptMuonEGRun2023BPixD02  = sample("NonpromptMuonEGRun2023BPixD02", 1.0, "2023BPix", "MuonEGRun2023BPixD022023BPixNanoList.txt", "/MuonEG/Run2023D-22Sep2023_v2-v1/NANOAOD")

NonpromptTauRun2022C = sample("NonpromptTauRun2022C", 1.0, "2022", "TauRun2022C2022NanoList.txt", "/Tau/Run2022C-22Sep2023-v1/NANOAOD")
NonpromptTauRun2022D = sample("NonpromptTauRun2022D", 1.0, "2022", "TauRun2022D2022NanoList.txt", "/Tau/Run2022D-22Sep2023-v1/NANOAOD")
NonpromptTauRun2022EEE  = sample("NonpromptTauRun2022EEE", 1.0, "2022EE", "TauRun2022EEE2022EENanoList.txt", "/Tau/Run2022E-22Sep2023-v1/NANOAOD")
NonpromptTauRun2022EEF  = sample("NonpromptTauRun2022EEF", 1.0, "2022EE", "TauRun2022EEF2022EENanoList.txt", "/Tau/Run2022F-22Sep2023-v1/NANOAOD")
NonpromptTauRun2022EEG  = sample("NonpromptTauRun2022EEG", 1.0, "2022EE", "TauRun2022EEG2022EENanoList.txt", "/Tau/Run2022G-22Sep2023-v1/NANOAOD")
NonpromptTauRun2023C01  = sample("NonpromptTauRun2023C01", 1.0, "2023", "TauRun2023C012023NanoList.txt", "/Tau/Run2023C-22Sep2023_v1-v2/NANOAOD")
NonpromptTauRun2023C02  = sample("NonpromptTauRun2023C02", 1.0, "2023", "TauRun2023C022023NanoList.txt", "/Tau/Run2023C-22Sep2023_v2-v1/NANOAOD")
NonpromptTauRun2023C03  = sample("NonpromptTauRun2023C03", 1.0, "2023", "TauRun2023C032023NanoList.txt", "/Tau/Run2023C-22Sep2023_v3-v1/NANOAOD")
NonpromptTauRun2023C04  = sample("NonpromptTauRun2023C04", 1.0, "2023", "TauRun2023C042023NanoList.txt", "/Tau/Run2023C-22Sep2023_v4-v1/NANOAOD")
NonpromptTauRun2023BPixD01  = sample("NonpromptTauRun2023BPixD01", 1.0, "2023BPix", "TauRun2023BPixD012023BPixNanoList.txt", "/Tau/Run2023D-22Sep2023_v1-v1/NANOAOD")
NonpromptTauRun2023BPixD02  = sample("NonpromptTauRun2023BPixD02", 1.0, "2023BPix", "TauRun2023BPixD022023BPixNanoList.txt", "/Tau/Run2023D-22Sep2023_v2-v1/NANOAOD")

samples_test = {
    "SingleElecRun2022C":      SingleElecRun2022C,
}

samples_data = {
    "SingleElecRun2022C":      SingleElecRun2022C,      
    "SingleElecRun2022D":      SingleElecRun2022D,      
    "SingleElecRun2022EEE":    SingleElecRun2022EEE,    
    "SingleElecRun2022EEF":    SingleElecRun2022EEF,    
    "SingleElecRun2022EEG":    SingleElecRun2022EEG,    
    "SingleElecRun2023C01":    SingleElecRun2023C01,    
    "SingleElecRun2023C02":    SingleElecRun2023C02,    
    "SingleElecRun2023C03":    SingleElecRun2023C03,    
    "SingleElecRun2023C04":    SingleElecRun2023C04,    
    "SingleElecRun2023C11":    SingleElecRun2023C11,    
    "SingleElecRun2023C12":    SingleElecRun2023C12,    
    "SingleElecRun2023C13":    SingleElecRun2023C13,    
    "SingleElecRun2023C14":    SingleElecRun2023C14,    
    "SingleElecRun2023BPixD01":SingleElecRun2023BPixD01,
    "SingleElecRun2023BPixD02":SingleElecRun2023BPixD02,
    "SingleElecRun2023BPixD11":SingleElecRun2023BPixD11,
    "SingleElecRun2023BPixD12":SingleElecRun2023BPixD12,
    "SingleMuonRun2022C":      SingleMuonRun2022C,      
    "SingleMuonRun2022D":      SingleMuonRun2022D,      
    "SingleMuonRun2022EEE":    SingleMuonRun2022EEE,    
    "SingleMuonRun2022EEF":    SingleMuonRun2022EEF,    
    "SingleMuonRun2022EEG":    SingleMuonRun2022EEG,    
    "SingleMuonRun2023C01":    SingleMuonRun2023C01,    
    "SingleMuonRun2023C02":    SingleMuonRun2023C02,    
    "SingleMuonRun2023C03":    SingleMuonRun2023C03,    
    "SingleMuonRun2023C04":    SingleMuonRun2023C04,    
    "SingleMuonRun2023C11":    SingleMuonRun2023C11,    
    "SingleMuonRun2023C12":    SingleMuonRun2023C12,    
    "SingleMuonRun2023C13":    SingleMuonRun2023C13,    
    "SingleMuonRun2023C14":    SingleMuonRun2023C14,    
    "SingleMuonRun2023BPixD01":SingleMuonRun2023BPixD01,
    "SingleMuonRun2023BPixD02":SingleMuonRun2023BPixD02,
    "SingleMuonRun2023BPixD11":SingleMuonRun2023BPixD11,
    "SingleMuonRun2023BPixD12":SingleMuonRun2023BPixD12,
    "MuonEGRun2022C":      MuonEGRun2022C,
    "MuonEGRun2022D":      MuonEGRun2022D,
    "MuonEGRun2022EEE":    MuonEGRun2022EEE,
    "MuonEGRun2022EEF":    MuonEGRun2022EEF,
    "MuonEGRun2022EEG":    MuonEGRun2022EEG,
    "MuonEGRun2023C01":    MuonEGRun2023C01,
    "MuonEGRun2023C02":    MuonEGRun2023C02,
    "MuonEGRun2023C03":    MuonEGRun2023C03,
    "MuonEGRun2023C04":    MuonEGRun2023C04,
    "MuonEGRun2023BPixD01":MuonEGRun2023BPixD01,
    "MuonEGRun2023BPixD02":MuonEGRun2023BPixD02,
    #"TauRun2022C":      TauRun2022C,
    #"TauRun2022D":      TauRun2022D,
    "TauRun2022EEE":    TauRun2022EEE,
    "TauRun2022EEF":    TauRun2022EEF,
    "TauRun2022EEG":    TauRun2022EEG,
    "TauRun2023C01":    TauRun2023C01,
    #"TauRun2023C02":    TauRun2023C02,
    "TauRun2023C03":    TauRun2023C03,
    "TauRun2023C04":    TauRun2023C04,
    #"TauRun2023BPixD01":TauRun2023BPixD01,
    #"TauRun2023BPixD02":TauRun2023BPixD02,
}

samples_nonprompt = {
    "NonpromptSingleElecRun2022C":      NonpromptSingleElecRun2022C,      
    "NonpromptSingleElecRun2022D":      NonpromptSingleElecRun2022D,      
    "NonpromptSingleElecRun2022EEE":    NonpromptSingleElecRun2022EEE,    
    "NonpromptSingleElecRun2022EEF":    NonpromptSingleElecRun2022EEF,    
    "NonpromptSingleElecRun2022EEG":    NonpromptSingleElecRun2022EEG,    
    "NonpromptSingleElecRun2023C01":    NonpromptSingleElecRun2023C01,    
    "NonpromptSingleElecRun2023C02":    NonpromptSingleElecRun2023C02,    
    "NonpromptSingleElecRun2023C03":    NonpromptSingleElecRun2023C03,    
    "NonpromptSingleElecRun2023C04":    NonpromptSingleElecRun2023C04,    
    "NonpromptSingleElecRun2023C11":    NonpromptSingleElecRun2023C11,    
    "NonpromptSingleElecRun2023C12":    NonpromptSingleElecRun2023C12,    
    "NonpromptSingleElecRun2023C13":    NonpromptSingleElecRun2023C13,    
    "NonpromptSingleElecRun2023C14":    NonpromptSingleElecRun2023C14,    
    "NonpromptSingleElecRun2023BPixD01":NonpromptSingleElecRun2023BPixD01,
    "NonpromptSingleElecRun2023BPixD02":NonpromptSingleElecRun2023BPixD02,
    "NonpromptSingleElecRun2023BPixD11":NonpromptSingleElecRun2023BPixD11,
    "NonpromptSingleElecRun2023BPixD12":NonpromptSingleElecRun2023BPixD12,
    "NonpromptSingleMuonRun2022C":      NonpromptSingleMuonRun2022C,      
    "NonpromptSingleMuonRun2022D":      NonpromptSingleMuonRun2022D,      
    "NonpromptSingleMuonRun2022EEE":    NonpromptSingleMuonRun2022EEE,    
    "NonpromptSingleMuonRun2022EEF":    NonpromptSingleMuonRun2022EEF,    
    "NonpromptSingleMuonRun2022EEG":    NonpromptSingleMuonRun2022EEG,    
    "NonpromptSingleMuonRun2023C01":    NonpromptSingleMuonRun2023C01,    
    "NonpromptSingleMuonRun2023C02":    NonpromptSingleMuonRun2023C02,    
    "NonpromptSingleMuonRun2023C03":    NonpromptSingleMuonRun2023C03,    
    "NonpromptSingleMuonRun2023C04":    NonpromptSingleMuonRun2023C04,    
    "NonpromptSingleMuonRun2023C11":    NonpromptSingleMuonRun2023C11,    
    "NonpromptSingleMuonRun2023C12":    NonpromptSingleMuonRun2023C12,    
    "NonpromptSingleMuonRun2023C13":    NonpromptSingleMuonRun2023C13,    
    "NonpromptSingleMuonRun2023C14":    NonpromptSingleMuonRun2023C14,    
    "NonpromptSingleMuonRun2023BPixD01":NonpromptSingleMuonRun2023BPixD01,
    "NonpromptSingleMuonRun2023BPixD02":NonpromptSingleMuonRun2023BPixD02,
    "NonpromptSingleMuonRun2023BPixD11":NonpromptSingleMuonRun2023BPixD11,
    "NonpromptSingleMuonRun2023BPixD12":NonpromptSingleMuonRun2023BPixD12,
    "NonpromptMuonEGRun2022C":      NonpromptMuonEGRun2022C,
    "NonpromptMuonEGRun2022D":      NonpromptMuonEGRun2022D,
    "NonpromptMuonEGRun2022EEE":    NonpromptMuonEGRun2022EEE,
    "NonpromptMuonEGRun2022EEF":    NonpromptMuonEGRun2022EEF,
    "NonpromptMuonEGRun2022EEG":    NonpromptMuonEGRun2022EEG,
    "NonpromptMuonEGRun2023C01":    NonpromptMuonEGRun2023C01,
    "NonpromptMuonEGRun2023C02":    NonpromptMuonEGRun2023C02,
    "NonpromptMuonEGRun2023C03":    NonpromptMuonEGRun2023C03,
    "NonpromptMuonEGRun2023C04":    NonpromptMuonEGRun2023C04,
    "NonpromptMuonEGRun2023BPixD01":NonpromptMuonEGRun2023BPixD01,
    "NonpromptMuonEGRun2023BPixD02":NonpromptMuonEGRun2023BPixD02,
    "NonpromptTauRun2022C":      NonpromptTauRun2022C,
    "NonpromptTauRun2022D":      NonpromptTauRun2022D,
    "NonpromptTauRun2022EEE":    NonpromptTauRun2022EEE,
    "NonpromptTauRun2022EEF":    NonpromptTauRun2022EEF,
    "NonpromptTauRun2022EEG":    NonpromptTauRun2022EEG,
    "NonpromptTauRun2023C01":    NonpromptTauRun2023C01,
    "NonpromptTauRun2023C02":    NonpromptTauRun2023C02,
    "NonpromptTauRun2023C03":    NonpromptTauRun2023C03,
    "NonpromptTauRun2023C04":    NonpromptTauRun2023C04,
    "NonpromptTauRun2023BPixD01":NonpromptTauRun2023BPixD01,
    "NonpromptTauRun2023BPixD02":NonpromptTauRun2023BPixD02,
}

samples_signal={
    "Bprime_M1000_2022":    Bprime_M1000_2022,    
    "Bprime_M1000_2022EE":  Bprime_M1000_2022EE,  
    "Bprime_M1000_2023":    Bprime_M1000_2023,    
    "Bprime_M1000_2023BPix":Bprime_M1000_2023BPix,
    "Bprime_M1300_2022":    Bprime_M1300_2022,    
    "Bprime_M1300_2022EE":  Bprime_M1300_2022EE,  
    "Bprime_M1300_2023":    Bprime_M1300_2023,    
    "Bprime_M1300_2023BPix":Bprime_M1300_2023BPix,
    "Bprime_M1600_2022":    Bprime_M1600_2022,    
    "Bprime_M1600_2022EE":  Bprime_M1600_2022EE,  
    "Bprime_M1600_2023":    Bprime_M1600_2023,    
    "Bprime_M1600_2023BPix":Bprime_M1600_2023BPix,
    "Bprime_M700_2022":    Bprime_M700_2022,    
    "Bprime_M700_2022EE":  Bprime_M700_2022EE,  
    "Bprime_M700_2023":    Bprime_M700_2023,    
    "Bprime_M700_2023BPix":Bprime_M700_2023BPix,
    "Bprime_M400_2022":     Bprime_M400_2022,
    "Bprime_M400_2022EE":   Bprime_M400_2022EE,
    "Bprime_M400_2023":     Bprime_M400_2023,
    "Bprime_M400_2023BPix": Bprime_M400_2023BPix,
}

samples_electroweak = {
    "WW2L2022":     WW2L2022,     
    "WW2L2022EE":   WW2L2022EE,   
    "WW2L2023":     WW2L2023,     
    "WW2L2023BPix": WW2L2023BPix, 
    "WZ2L2022":     WZ2L2022,     
    "WZ2L2022EE":   WZ2L2022EE,   
    "WZ2L2023":     WZ2L2023,     
    "WZ2L2023BPix": WZ2L2023BPix, 
    "ZZ2L2022":       ZZ2L2022,
    "ZZ2L2022EE":     ZZ2L2022EE,
    "ZZ2L2023":       ZZ2L2023,
    "ZZ2L2023BPix":   ZZ2L2023BPix,
    "ZZ4L2022":       ZZ4L2022,
    "ZZ4L2022EE":     ZZ4L2022EE,
    "ZZ4L2023":       ZZ4L2023,
    "ZZ4L2023BPix":   ZZ4L2023BPix,
    "DYPT402022":     DYPT402022,     
    "DYPT402022EE":   DYPT402022EE,   
    "DYPT402023":     DYPT402023,     
    "DYPT402023BPix": DYPT402023BPix, 
    "DYPT1002022":    DYPT1002022,    
    "DYPT1002022EE":  DYPT1002022EE,  
    "DYPT1002023":    DYPT1002023,    
    "DYPT1002023BPix":DYPT1002023BPix,
    "DYPT2002022":    DYPT2002022,    
    "DYPT2002022EE":  DYPT2002022EE,  
    "DYPT2002023":    DYPT2002023,    
    "DYPT2002023BPix":DYPT2002023BPix,
    "DYPT4002022":    DYPT4002022,    
    "DYPT4002022EE":  DYPT4002022EE,  
    "DYPT4002023":    DYPT4002023,    
    "DYPT4002023BPix":DYPT4002023BPix,
    "DYPT6002022":    DYPT6002022,    
    "DYPT6002022EE":  DYPT6002022EE,  
    "DYPT6002023":    DYPT6002023,    
    "DYPT6002023BPix":DYPT6002023BPix,
    "WWW2022"     :     WWW2022     ,
    "WWW2022EE"   :     WWW2022EE   ,
    "WWW2023"     :     WWW2023     ,
    "WWW2023BPix" :     WWW2023BPix ,
    "WWZ2022"     :     WWZ2022     ,
    "WWZ2022EE"   :     WWZ2022EE   ,
    "WWZ2023"     :     WWZ2023     ,
    "WWZ2023BPix" :     WWZ2023BPix ,
    "WZZ2022"     :     WZZ2022     ,
    "WZZ2022EE"   :     WZZ2022EE   ,
    "WZZ2023"     :     WZZ2023     ,
    "WZZ2023BPix" :     WZZ2023BPix ,
    "ZZZ2022"     :     ZZZ2022     ,
    "ZZZ2022EE"   :     ZZZ2022EE   ,
    "ZZZ2023"     :     ZZZ2023     ,
    "ZZZ2023BPix" :     ZZZ2023BPix ,
}

samples_electroweak4 = {
    "ZZ4L2022":       ZZ4L2022,
    "ZZ4L2022EE":     ZZ4L2022EE,
    "ZZ4L2023":       ZZ4L2023,
    "ZZ4L2023BPix":   ZZ4L2023BPix,
    "WWZ2022"     :     WWZ2022     ,
    "WWZ2022EE"   :     WWZ2022EE   ,
    "WWZ2023"     :     WWZ2023     ,
    "WWZ2023BPix" :     WWZ2023BPix ,
    "WZZ2022"     :     WZZ2022     ,
    "WZZ2022EE"   :     WZZ2022EE   ,
    "WZZ2023"     :     WZZ2023     ,
    "WZZ2023BPix" :     WZZ2023BPix ,
    "ZZZ2022"     :     ZZZ2022     ,
    "ZZZ2022EE"   :     ZZZ2022EE   ,
    "ZZZ2023"     :     ZZZ2023     ,
    "ZZZ2023BPix" :     ZZZ2023BPix ,
}

samples_electroweak3 = {
    "ZZ4L2022":       ZZ4L2022,
    "ZZ4L2022EE":     ZZ4L2022EE,
    "ZZ4L2023":       ZZ4L2023,
    "ZZ4L2023BPix":   ZZ4L2023BPix,
    "WWW2022"     :     WWW2022     ,
    "WWW2022EE"   :     WWW2022EE   ,
    "WWW2023"     :     WWW2023     ,
    "WWW2023BPix" :     WWW2023BPix ,
    "WWZ2022"     :     WWZ2022     ,
    "WWZ2022EE"   :     WWZ2022EE   ,
    "WWZ2023"     :     WWZ2023     ,
    "WWZ2023BPix" :     WWZ2023BPix ,
    "WZZ2022"     :     WZZ2022     ,
    "WZZ2022EE"   :     WZZ2022EE   ,
    "WZZ2023"     :     WZZ2023     ,
    "WZZ2023BPix" :     WZZ2023BPix ,
    "ZZZ2022"     :     ZZZ2022     ,
    "ZZZ2022EE"   :     ZZZ2022EE   ,
    "ZZZ2023"     :     ZZZ2023     ,
    "ZZZ2023BPix" :     ZZZ2023BPix ,
}

samples_qcd = {
    #"QCDHT10002022":   QCDHT10002022 ,   
    #"QCDHT10002022EE":  QCDHT10002022EE,  
    "QCDHT10002023":    QCDHT10002023,    
    "QCDHT10002023BPix":QCDHT10002023BPix,
    "QCDHT12002022":    QCDHT12002022,    
    "QCDHT12002022EE":  QCDHT12002022EE,  
    "QCDHT12002023":    QCDHT12002023,    
    "QCDHT12002023BPix":QCDHT12002023BPix,
    "QCDHT15002022":    QCDHT15002022,    
    "QCDHT15002022EE":  QCDHT15002022EE,  
    "QCDHT15002023":    QCDHT15002023,    
    "QCDHT15002023BPix":QCDHT15002023BPix,
    "QCDHT20002022":    QCDHT20002022,    
    "QCDHT20002022EE":  QCDHT20002022EE,  
    "QCDHT20002023":    QCDHT20002023,    
    "QCDHT20002023BPix":QCDHT20002023BPix,
    "QCDHT2002022":     QCDHT2002022,     
    "QCDHT2002022EE":   QCDHT2002022EE,   
    "QCDHT2002023":     QCDHT2002023,     
    "QCDHT2002023BPix": QCDHT2002023BPix, 
    "QCDHT4002022":     QCDHT4002022,     
    "QCDHT4002022EE":   QCDHT4002022EE,   
    "QCDHT4002023":     QCDHT4002023,     
    "QCDHT4002023BPix": QCDHT4002023BPix, 
    "QCDHT6002022":     QCDHT6002022,     
    "QCDHT6002022EE":   QCDHT6002022EE,   
    "QCDHT6002023":     QCDHT6002023,     
    "QCDHT6002023BPix": QCDHT6002023BPix, 
    "QCDHT8002022":     QCDHT8002022,     
    "QCDHT8002022EE":   QCDHT8002022EE,   
    "QCDHT8002023":     QCDHT8002023,     
    "QCDHT8002023BPix": QCDHT8002023BPix,
}

samples_singletop = {
    "STs2022":       STs2022,       
    "STs2022EE":     STs2022EE,     
    "STs2023":       STs2023,       
    "STs2023BPix":   STs2023BPix,   
    "STbs2022":      STbs2022,      
    "STbs2022EE":    STbs2022EE,    
    "STbs2023":      STbs2023,      
    "STbs2023BPix":  STbs2023BPix,  
    "STt2022":       STt2022,       
    "STt2022EE":     STt2022EE,     
    "STt2023":       STt2023,       
    "STt2023BPix":   STt2023BPix,   
    "STtb2022":      STtb2022,      
    "STtb2022EE":    STtb2022EE,    
    "STtb2023":      STtb2023,      
    "STtb2023BPix":  STtb2023BPix,  
    "STtW2022":      STtW2022,      
    "STtW2022EE":    STtW2022EE,    
    "STtW2023":      STtW2023,      
    "STtW2023BPix":  STtW2023BPix,  
    "STtWb2022":     STtWb2022,     
    "STtWb2022EE":   STtWb2022EE,   
    #"STtWb2023":     STtWb2023,     
    #"STtWb2023BPix": STtWb2023BPix,
}

samples_ttbarx = {
    "TTHB2022":       TTHB2022,       
    "TTHB2022EE":     TTHB2022EE,     
    "TTHB2023":       TTHB2023,       
    "TTHB2023BPix":   TTHB2023BPix,   
    "TTHnonB2022":    TTHnonB2022,    
    "TTHnonB2022EE":  TTHnonB2022EE,  
    "TTHnonB2023":    TTHnonB2023,    
    "TTHnonB2023BPix":TTHnonB2023BPix,
    "TTWl2022":         TTWl2022,         
    "TTWl2022EE":       TTWl2022EE,       
    "TTWl2023":         TTWl2023,         
    "TTWl2023BPix":     TTWl2023BPix,     
    #"TTWq2022":         TTWq2022,         
    #"TTWq2022EE":       TTWq2022EE,       
    #"TTWq2023":         TTWq2023,         
    #"TTWq2023BPix":     TTWq2023BPix,     
    "TTZM42022":       TTZM42022,       
    "TTZM42022EE":     TTZM42022EE,     
    "TTZM42023":       TTZM42023,       
    "TTZM42023BPix":   TTZM42023BPix,   
    "TTZM502022":    TTZM502022,    
    "TTZM502022EE":  TTZM502022EE,  
    "TTZM502023":    TTZM502023,    
    "TTZM502023BPix":TTZM502023BPix,
    "TTWH2022"     : TTWH2022     ,
    "TTWH2022EE"   : TTWH2022EE  ,
    "TTWH2023"     : TTWH2023    ,
    "TTWH2023BPix" : TTWH2023BPix,
    "TTWW2022"     : TTWW2022    ,
    "TTWW2022EE"   : TTWW2022EE  ,
    "TTWW2023"     : TTWW2023    ,
    "TTWW2023BPix" : TTWW2023BPix,
    #"TTWZ2022"     : TTWZ2022    ,
    #"TTWZ2022EE"   : TTWZ2022EE  ,
    "TTWZ2023"     : TTWZ2023    ,
    "TTWZ2023BPix" : TTWZ2023BPix,
    "TTZH2022"     : TTZH2022    ,
    "TTZH2022EE"   : TTZH2022EE  ,
    "TTZH2023"     : TTZH2023    ,
    "TTZH2023BPix" : TTZH2023BPix,
    "TTZZ2022"     : TTZZ2022    ,
    "TTZZ2022EE"   : TTZZ2022EE  ,
    "TTZZ2023"     : TTZZ2023    ,
    "TTZZ2023BPix" : TTZZ2023BPix,
    "TTTT2022"     : TTTT2022    ,
    "TTTT2022EE"   : TTTT2022EE  ,
    "TTTT2023"     : TTTT2023    ,
    "TTTT2023BPix" : TTTT2023BPix,
}

samples_ttbarx4 = {
    "TTHnonB2022":    TTHnonB2022,    
    "TTHnonB2022EE":  TTHnonB2022EE,  
    "TTHnonB2023":    TTHnonB2023,    
    "TTHnonB2023BPix":TTHnonB2023BPix,
    "TTZM42022":       TTZM42022,       
    "TTZM42022EE":     TTZM42022EE,     
    "TTZM42023":       TTZM42023,       
    "TTZM42023BPix":   TTZM42023BPix,   
    "TTZM502022":    TTZM502022,    
    "TTZM502022EE":  TTZM502022EE,  
    "TTZM502023":    TTZM502023,    
    "TTZM502023BPix":TTZM502023BPix,
    "TTWH2022"     : TTWH2022     ,
    "TTWH2022EE"   : TTWH2022EE  ,
    "TTWH2023"     : TTWH2023    ,
    "TTWH2023BPix" : TTWH2023BPix,
    "TTWW2022"     : TTWW2022    ,
    "TTWW2022EE"   : TTWW2022EE  ,
    "TTWW2023"     : TTWW2023    ,
    "TTWW2023BPix" : TTWW2023BPix,
    "TTWZ2022"     : TTWZ2022    ,
    "TTWZ2022EE"   : TTWZ2022EE  ,
    "TTWZ2023"     : TTWZ2023    ,
    "TTWZ2023BPix" : TTWZ2023BPix,
    "TTZH2022"     : TTZH2022    ,
    "TTZH2022EE"   : TTZH2022EE  ,
    "TTZH2023"     : TTZH2023    ,
    "TTZH2023BPix" : TTZH2023BPix,
    "TTZZ2022"     : TTZZ2022    ,
    "TTZZ2022EE"   : TTZZ2022EE  ,
    "TTZZ2023"     : TTZZ2023    ,
    "TTZZ2023BPix" : TTZZ2023BPix,
    "TTTT2022"     : TTTT2022    ,
    "TTTT2022EE"   : TTTT2022EE  ,
    "TTTT2023"     : TTTT2023    ,
    "TTTT2023BPix" : TTTT2023BPix,
}

samples_ttbarx3 = {
    "TTHnonB2022":    TTHnonB2022,    
    "TTHnonB2022EE":  TTHnonB2022EE,  
    "TTHnonB2023":    TTHnonB2023,    
    "TTHnonB2023BPix":TTHnonB2023BPix,
    "TTWl2022":         TTWl2022,         
    "TTWl2022EE":       TTWl2022EE,       
    "TTWl2023":         TTWl2023,         
    "TTWl2023BPix":     TTWl2023BPix,     
    "TTZM42022":       TTZM42022,       
    "TTZM42022EE":     TTZM42022EE,     
    "TTZM42023":       TTZM42023,       
    "TTZM42023BPix":   TTZM42023BPix,   
    "TTZM502022":    TTZM502022,    
    "TTZM502022EE":  TTZM502022EE,  
    "TTZM502023":    TTZM502023,    
    "TTZM502023BPix":TTZM502023BPix,
    "TTWH2022"     : TTWH2022     ,
    "TTWH2022EE"   : TTWH2022EE  ,
    "TTWH2023"     : TTWH2023    ,
    "TTWH2023BPix" : TTWH2023BPix,
    "TTWW2022"     : TTWW2022    ,
    "TTWW2022EE"   : TTWW2022EE  ,
    "TTWW2023"     : TTWW2023    ,
    "TTWW2023BPix" : TTWW2023BPix,
    "TTWZ2022"     : TTWZ2022    ,
    "TTWZ2022EE"   : TTWZ2022EE  ,
    "TTWZ2023"     : TTWZ2023    ,
    "TTWZ2023BPix" : TTWZ2023BPix,
    "TTZH2022"     : TTZH2022    ,
    "TTZH2022EE"   : TTZH2022EE  ,
    "TTZH2023"     : TTZH2023    ,
    "TTZH2023BPix" : TTZH2023BPix,
    "TTZZ2022"     : TTZZ2022    ,
    "TTZZ2022EE"   : TTZZ2022EE  ,
    "TTZZ2023"     : TTZZ2023    ,
    "TTZZ2023BPix" : TTZZ2023BPix,
    "TTTT2022"     : TTTT2022    ,
    "TTTT2022EE"   : TTTT2022EE  ,
    "TTTT2023"     : TTTT2023    ,
    "TTTT2023BPix" : TTTT2023BPix,
}

samples_ttbar = {
    "TTTo2L2Nu2022":            TTTo2L2Nu2022,            
    "TTTo2L2Nu2022EE":          TTTo2L2Nu2022EE,          
    "TTTo2L2Nu2023":            TTTo2L2Nu2023,            
    "TTTo2L2Nu2023BPix":        TTTo2L2Nu2023BPix,        
    "TTToHadronic2022":         TTToHadronic2022,         
    "TTToHadronic2022EE":       TTToHadronic2022EE,       
    "TTToHadronic2023":         TTToHadronic2023,         
    "TTToHadronic2023BPix":     TTToHadronic2023BPix,     
    "TTToSemiLeptonic2022":     TTToSemiLeptonic2022,     
    "TTToSemiLeptonic2022EE":   TTToSemiLeptonic2022EE,   
    "TTToSemiLeptonic2023":     TTToSemiLeptonic2023,     
    "TTToSemiLeptonic2023BPix": TTToSemiLeptonic2023BPix,
}

samples_wjets = {
    "WJetsHT1002022":         WJetsHT1002022,         
    "WJetsHT1002022EE":       WJetsHT1002022EE,       
    "WJetsHT1002023":         WJetsHT1002023,         
    "WJetsHT1002023BPix":     WJetsHT1002023BPix,     
    "WJetsHT15002022":        WJetsHT15002022,        
    "WJetsHT15002022EE":      WJetsHT15002022EE,      
    "WJetsHT15002023":        WJetsHT15002023,        
    "WJetsHT15002023BPix":    WJetsHT15002023BPix,    
    "WJetsHT25002022":        WJetsHT25002022,        
    "WJetsHT25002022EE":      WJetsHT25002022EE,      
    "WJetsHT25002023":        WJetsHT25002023,        
    "WJetsHT25002023BPix":    WJetsHT25002023BPix,    
    "WJetsHT4002022":         WJetsHT4002022,         
    "WJetsHT4002022EE":       WJetsHT4002022EE,       
    "WJetsHT4002023":         WJetsHT4002023,         
    "WJetsHT4002023BPix":     WJetsHT4002023BPix,     
    "WJetsHT8002022":         WJetsHT8002022,         
    "WJetsHT8002022EE":       WJetsHT8002022EE,       
    "WJetsHT8002023":         WJetsHT8002023,         
    "WJetsHT8002023BPix":     WJetsHT8002023BPix,     
    "WJetsM120HT1002022":     WJetsM120HT1002022,     
    "WJetsM120HT1002022EE":   WJetsM120HT1002022EE,   
    "WJetsM120HT1002023":     WJetsM120HT1002023,     
    "WJetsM120HT1002023BPix": WJetsM120HT1002023BPix, 
    "WJetsM120HT15002022":    WJetsM120HT15002022,    
    "WJetsM120HT15002022EE":  WJetsM120HT15002022EE,  
    "WJetsM120HT15002023":    WJetsM120HT15002023,    
    "WJetsM120HT15002023BPix":WJetsM120HT15002023BPix,
    "WJetsM120HT25002022":    WJetsM120HT25002022,    
    "WJetsM120HT25002022EE":  WJetsM120HT25002022EE,  
    "WJetsM120HT25002023":    WJetsM120HT25002023,    
    "WJetsM120HT25002023BPix":WJetsM120HT25002023BPix,
    "WJetsM120HT4002022":     WJetsM120HT4002022,     
    "WJetsM120HT4002022EE":   WJetsM120HT4002022EE,   
    "WJetsM120HT4002023":     WJetsM120HT4002023,     
    "WJetsM120HT4002023BPix": WJetsM120HT4002023BPix, 
    "WJetsM120HT8002022":     WJetsM120HT8002022,     
    "WJetsM120HT8002022EE":   WJetsM120HT8002022EE,   
    "WJetsM120HT8002023":     WJetsM120HT8002023,     
    "WJetsM120HT8002023BPix": WJetsM120HT8002023BPix,  
}

samples_mc={
    "Bprime_M1000_2022":    Bprime_M1000_2022,
    "Bprime_M1000_2022EE":  Bprime_M1000_2022EE,
    "Bprime_M1000_2023":    Bprime_M1000_2023,
    "Bprime_M1000_2023BPix":Bprime_M1000_2023BPix,
    "Bprime_M1300_2022":    Bprime_M1300_2022,
    "Bprime_M1300_2022EE":  Bprime_M1300_2022EE,
    "Bprime_M1300_2023":    Bprime_M1300_2023,
    "Bprime_M1300_2023BPix":Bprime_M1300_2023BPix,
    "Bprime_M1600_2022":    Bprime_M1600_2022,
    "Bprime_M1600_2022EE":  Bprime_M1600_2022EE,
    "Bprime_M1600_2023":    Bprime_M1600_2023,
    "Bprime_M1600_2023BPix":Bprime_M1600_2023BPix,
    "Bprime_M700_2022":    Bprime_M700_2022,
    "Bprime_M700_2022EE":  Bprime_M700_2022EE,
    "Bprime_M700_2023":    Bprime_M700_2023,
    "Bprime_M700_2023BPix":Bprime_M700_2023BPix,
    "Bprime_M400_2022":    Bprime_M400_2022,
    "Bprime_M400_2022EE":  Bprime_M400_2022EE,
    "Bprime_M400_2023":    Bprime_M400_2023,
    "Bprime_M400_2023BPix":Bprime_M400_2023BPix,
    "DYPT402022":     DYPT402022,
    "DYPT402022EE":   DYPT402022EE,
    "DYPT402023":     DYPT402023,
    "DYPT402023BPix": DYPT402023BPix,
    "DYPT1002022":    DYPT1002022,
    "DYPT1002022EE":  DYPT1002022EE,
    "DYPT1002023":    DYPT1002023,
    "DYPT1002023BPix":DYPT1002023BPix,
    "DYPT2002022":    DYPT2002022,
    "DYPT2002022EE":  DYPT2002022EE,
    "DYPT2002023":    DYPT2002023,
    "DYPT2002023BPix":DYPT2002023BPix,
    "DYPT4002022":    DYPT4002022,
    "DYPT4002022EE":  DYPT4002022EE,
    "DYPT4002023":    DYPT4002023,
    "DYPT4002023BPix":DYPT4002023BPix,
    "DYPT6002022":    DYPT6002022,
    "DYPT6002022EE":  DYPT6002022EE,
    "DYPT6002023":    DYPT6002023,
    "DYPT6002023BPix":DYPT6002023BPix,
    "QCDHT10002022 ":   QCDHT10002022 ,
    "QCDHT10002022EE":  QCDHT10002022EE,
    "QCDHT10002023":    QCDHT10002023,
    "QCDHT10002023BPix":QCDHT10002023BPix,
    "QCDHT12002022":    QCDHT12002022,
    "QCDHT12002022EE":  QCDHT12002022EE,
    "QCDHT12002023":    QCDHT12002023,
    "QCDHT12002023BPix":QCDHT12002023BPix,
    "QCDHT15002022":    QCDHT15002022,
    "QCDHT15002022EE":  QCDHT15002022EE,
    "QCDHT15002023":    QCDHT15002023,
    "QCDHT15002023BPix":QCDHT15002023BPix,
    "QCDHT20002022":    QCDHT20002022,
    "QCDHT20002022EE":  QCDHT20002022EE,
    "QCDHT20002023":    QCDHT20002023,
    "QCDHT20002023BPix":QCDHT20002023BPix,
    "QCDHT2002022":     QCDHT2002022,
    "QCDHT2002022EE":   QCDHT2002022EE,
    "QCDHT2002023":     QCDHT2002023,
    "QCDHT2002023BPix": QCDHT2002023BPix,
    "QCDHT4002022":     QCDHT4002022,
    "QCDHT4002022EE":   QCDHT4002022EE,
    "QCDHT4002023":     QCDHT4002023,
    "QCDHT4002023BPix": QCDHT4002023BPix,
    "QCDHT6002022":     QCDHT6002022,
    "QCDHT6002022EE":   QCDHT6002022EE,
    "QCDHT6002023":     QCDHT6002023,
    "QCDHT6002023BPix": QCDHT6002023BPix,
    "QCDHT8002022":     QCDHT8002022,
    "QCDHT8002022EE":   QCDHT8002022EE,
    "QCDHT8002023":     QCDHT8002023,
    "QCDHT8002023BPix": QCDHT8002023BPix,
    "TTHB2022":       TTHB2022,
    "TTHB2022EE":     TTHB2022EE,
    "TTHB2023":       TTHB2023,
    "TTHB2023BPix":   TTHB2023BPix,
    "TTHnonB2022":    TTHnonB2022,
    "TTHnonB2022EE":  TTHnonB2022EE,
    "TTHnonB2023":    TTHnonB2023,
    "TTHnonB2023BPix":TTHnonB2023BPix,
    "TTTo2L2Nu2022":            TTTo2L2Nu2022,
    "TTTo2L2Nu2022ext":         TTTo2L2Nu2022ext,
    "TTTo2L2Nu2022EE":          TTTo2L2Nu2022EE,
    "TTTo2L2Nu2022EEext":       TTTo2L2Nu2022EEext,
    "TTTo2L2Nu2023":            TTTo2L2Nu2023,
    "TTTo2L2Nu2023BPix":        TTTo2L2Nu2023BPix,
    "TTToHadronic2022":         TTToHadronic2022,
    "TTToHadronic2022ext":      TTToHadronic2022ext,
    "TTToHadronic2022EE":       TTToHadronic2022EE,
    "TTToHadronic2022EEext":    TTToHadronic2022EEext,
    "TTToHadronic2023":         TTToHadronic2023,
    "TTToHadronic2023BPix":     TTToHadronic2023BPix,
    "TTToSemiLeptonic2022":     TTToSemiLeptonic2022,
    "TTToSemiLeptonic2022ext":  TTToSemiLeptonic2022ext,
    "TTToSemiLeptonic2022EE":   TTToSemiLeptonic2022EE,
    "TTToSemiLeptonic2022EEext":TTToSemiLeptonic2022EEext,
    "TTToSemiLeptonic2023":     TTToSemiLeptonic2023,
    "TTToSemiLeptonic2023BPix": TTToSemiLeptonic2023BPix,
    "TTWl2022":         TTWl2022,
    "TTWl2022EE":       TTWl2022EE,
    "TTWl2023":         TTWl2023,
    "TTWl2023BPix":     TTWl2023BPix,
    "TTZM42022":       TTZM42022,
    "TTZM42022EE":     TTZM42022EE,
    "TTZM42023":       TTZM42023,
    "TTZM42023BPix":   TTZM42023BPix,
    "TTZM502022":    TTZM502022,
    "TTZM502022EE":  TTZM502022EE,
    "TTZM502023":    TTZM502023,
    "TTZM502023BPix":TTZM502023BPix,
    "TTZM502022ext":    TTZM502022ext,
    "TTZM502022EEext":  TTZM502022EEext,
    "TTZM502023ext":    TTZM502023ext,
    "TTZM502023BPixext":TTZM502023BPixext,
    "WW2L2022":     WW2L2022,
    "WW2L2022EE":   WW2L2022EE,
    "WW2L2023":     WW2L2023,
    "WW2L2023BPix": WW2L2023BPix,
    "WZ2L2022ext":  WZ2L2022ext,
    "WZ2L2022EEext":WZ2L2022EEext,
    "WZ3L2022":     WZ3L2022,
    "WZ3L2022EE":   WZ3L2022EE,
    "WZ3L2023":     WZ3L2023,
    "WZ3L2023BPix": WZ3L2023BPix,
    "ZZ2L2022":       ZZ2L2022,
    "ZZ2L2022EE":     ZZ2L2022EE,
    "ZZ2L2023":       ZZ2L2023,
    "ZZ2L2023BPix":   ZZ2L2023BPix,
    "ZZ4L2022":       ZZ4L2022,
    "ZZ4L2022EE":     ZZ4L2022EE,
    "ZZ4L2023":       ZZ4L2023,
    "ZZ4L2023BPix":   ZZ4L2023BPix,
    "WWW2022":     WWW2022,
    "WWW2022EE":   WWW2022EE,
    "WWW2023":     WWW2023,
    "WWW2023BPix": WWW2023BPix,
    "WWZ2022":     WWZ2022,
    "WWZ2022EE":   WWZ2022EE,
    "WWZ2023":     WWZ2023,
    "WWZ2023BPix": WWZ2023BPix,
    "WZZ2022":     WZZ2022,
    "WZZ2022EE":   WZZ2022EE,
    "WZZ2023":     WZZ2023,
    "WZZ2023BPix": WZZ2023BPix,
    "ZZZ2022":     ZZZ2022,
    "ZZZ2022EE":   ZZZ2022EE,
    "ZZZ2023":     ZZZ2023,
    "ZZZ2023BPix": ZZZ2023BPix,
    "TTWH2022":     TTWH2022,
    "TTWH2022EE":   TTWH2022EE,
    "TTWH2023":     TTWH2023,
    "TTWH2023BPix": TTWH2023BPix,
    "TTWW2022":     TTWW2022,
    "TTWW2022EE":   TTWW2022EE,
    "TTWW2023":     TTWW2023,
    "TTWW2023BPix": TTWW2023BPix,
    "TTWZ2022":     TTWZ2022,
    "TTWZ2022EE":   TTWZ2022EE,
    "TTWZ2023":     TTWZ2023,
    "TTWZ2023BPix": TTWZ2023BPix,
    "TTZH2022":     TTZH2022,
    "TTZH2022EE":   TTZH2022EE,
    "TTZH2023":     TTZH2023,
    "TTZH2023BPix": TTZH2023BPix,
    "TTZZ2022":     TTZZ2022,
    "TTZZ2022EE":   TTZZ2022EE,
    "TTZZ2023":     TTZZ2023,
    "TTZZ2023BPix": TTZZ2023BPix,
    "TTTT2022":     TTTT2022,
    "TTTT2022EE":   TTTT2022EE,
    "TTTT2023":     TTTT2023,
    "TTTT2023BPix": TTTT2023BPix,
    "WWZZ3L2022":     WWZZ3L2022,
    "WWZZ3L2022EE":   WWZZ3L2022EE,
    "WWZZ3L2023":     WWZZ3L2023,
    "WWZZ3L2023BPix": WWZZ3L2023BPix,
    "WWZZ4L2022":     WWZZ4L2022,
    "WWZZ4L2022EE":   WWZZ4L2022EE,
    "WWZZ4L2023":     WWZZ4L2023,
    "WWZZ4L2023BPix": WWZZ4L2023BPix,
}

# Use if refreshing nRun on all the MC
# mclist_2022 = [
#     Bprime_M1000_2022,    
#     Bprime_M1300_2022,    
#     Bprime_M1600_2022,    
#     Bprime_M700_2022,
#     Bprime_M400_2022,
#     DYPT402022,     
#     DYPT1002022,    
#     DYPT2002022,    
#     DYPT4002022,    
#     DYPT6002022,    
#     QCDHT10002022 ,   
#     QCDHT12002022,    
#     QCDHT15002022,    
#     QCDHT20002022,    
#     QCDHT2002022,     
#     QCDHT4002022,     
#     QCDHT6002022,     
#     QCDHT8002022,     
#     TTHB2022,       
#     TTHnonB2022,    
#     TTTo2L2Nu2022,            
#     TTToHadronic2022,         
#     TTToSemiLeptonic2022,     
#     TTWl2022,         
#     TTZM42022,
#     TTZM502022,    
#     WW2L2022,     
#     WZ2L2022,     
#     WZ3L2022,
#     ZZ2L2022,
#     ZZ4L2022,
#     WWW2022,
#     WWZ2022,
#     WZZ2022,
#     ZZZ2022,
#     TTWH2022,
#     TTWW2022,
#     TTWZ2022,
#    TTZH2022,
#    TTZZ2022,
#    TTTT2022,
#    WWZZ3L2022,
#    WWZZ4L2022,
# ]
    
# mclist_2022EE = [
#     Bprime_M1000_2022EE,    
#     Bprime_M1300_2022EE,    
#     Bprime_M1600_2022EE,    
#     Bprime_M700_2022EE,
#     Bprime_M400_2022EE,
#     DYPT402022EE,     
#     DYPT1002022EE,    
#     DYPT2002022EE,    
#     DYPT4002022EE,    
#     DYPT6002022EE,    
#     QCDHT10002022EE ,   
#     QCDHT12002022EE,    
#     QCDHT15002022EE,    
#     QCDHT20002022EE,    
#     QCDHT2002022EE,     
#     QCDHT4002022EE,     
#     QCDHT6002022EE,     
#     QCDHT8002022EE,     
#     TTHB2022EE,       
#     TTHnonB2022EE,    
#     TTTo2L2Nu2022EE,            
#     TTToHadronic2022EE,         
#     TTToSemiLeptonic2022EE,     
#     TTWl2022EE,         
#     TTZM42022EE,
#     TTZM502022EE,    
#     WW2L2022EE,     
#     WZ3L2022EE,
#     WZ2L2022EE,     
#     ZZ2L2022EE,
#     ZZ4L2022EE,
#     WWW2022EE,
#     WWZ2022EE,
#     WZZ2022EE,
#     ZZZ2022EE,
#     TTWH2022EE,
#     TTWW2022EE,
#     TTWZ2022EE,
#     TTZH2022EE,
#     TTZZ2022EE,
#     TTTT2022EE,
#     WWZZ3L2022EE,
#     WWZZ4L2022EE,
# ]

# mclist_2023 = [
#    Bprime_M1000_2023,    
#    Bprime_M1300_2023,    
#    Bprime_M1600_2023,    
#    Bprime_M400_2023,
#    Bprime_M700_2023,
#    DYPT402023,     
#    DYPT1002023,    
#    DYPT2002023,    
#    DYPT4002023,    
#    DYPT6002023,    
#    QCDHT10002023 ,   
#    QCDHT12002023,    
#    QCDHT15002023,    
#    QCDHT20002023,    
#    QCDHT2002023,     
#    QCDHT4002023,     
#    QCDHT6002023,     
#    QCDHT8002023,     
#    TTHB2023,       
#    TTHnonB2023,    
#    TTTo2L2Nu2023,            
#    TTToHadronic2023,         
#    TTToSemiLeptonic2023,     
#    TTWl2023,         
#    TTZM42023,
#    TTZM502023,    
#    WW2L2023,     
#    WZ3L2023,
#    WZ2L2023,     
#    ZZ2L2023,
#    ZZ4L2023,
#    WWW2023,
#    WWZ2023,
#    WZZ2023,
#    ZZZ2023,
#    TTWH2023,
#    TTWW2023,
#    TTWZ2023,
#    TTZH2023,
#    TTZZ2023,
#    TTTT2023,
#    WWZZ3L2023,
#    WWZZ4L2023,
# ]

# mclist_2023BPix = [
#    Bprime_M1000_2023BPix,    
#    Bprime_M1300_2023BPix,    
#    Bprime_M1600_2023BPix,    
#    Bprime_M400_2023BPix,
#    Bprime_M700_2023BPix,
#    DYPT402023BPix,     
#    DYPT1002023BPix,    
#    DYPT2002023BPix,    
#    DYPT4002023BPix,    
#    DYPT6002023BPix,    
#    QCDHT10002023BPix ,   
#    QCDHT12002023BPix,    
#    QCDHT15002023BPix,    
#    QCDHT20002023BPix,    
#    QCDHT2002023BPix,     
#    QCDHT4002023BPix,     
#    QCDHT6002023BPix,     
#    QCDHT8002023BPix,     
#    TTHB2023BPix,       
#    TTHnonB2023BPix,    
#    TTTo2L2Nu2023BPix,            
#    TTToHadronic2023BPix,         
#    TTToSemiLeptonic2023BPix,     
#    TTWl2023BPix,         
#    TTZM42023BPix,
#    TTZM502023BPix,    
#    WW2L2023BPix,     
#    WZ3L2023BPix,
#    WZ2L2023BPix,     
#    ZZ2L2023BPix,
#    ZZ4L2023BPix,
#    WWW2023BPix,
#    WWZ2023BPix,
#    WZZ2023BPix,
#    ZZZ2023BPix,
#    TTWH2023BPix,
#    TTWW2023BPix,
#    TTWZ2023BPix,
#    TTZH2023BPix,
#    TTZZ2023BPix,
#    TTTT2023BPix,
#    WWZZ3L2023BPix,
#    WWZZ4L2023BPix,
# ]

mclist_2022 = [
    Bprime_M1000_2022,    
    Bprime_M1300_2022,    
    Bprime_M1600_2022,    
    Bprime_M700_2022,
    Bprime_M400_2022,
    TTHnonB2022,    
    TTWl2022,         
    TTZM42022,
    TTZM502022,    
    WZ3L2022,
    ZZ4L2022,
    WWW2022,
    WWZ2022,
    WZZ2022,
    ZZZ2022,
    TTWH2022,
    TTWW2022,
    TTWZ2022,
    TTZH2022,
    TTZZ2022,
    TTTT2022,
    WWZZ3L2022,
    WWZZ4L2022,
]
    
mclist_2022EE = [
    Bprime_M1000_2022EE,    
    Bprime_M1300_2022EE,    
    Bprime_M1600_2022EE,    
    Bprime_M700_2022EE,
    Bprime_M400_2022EE,
    TTHnonB2022EE,    
    TTWl2022EE,         
    TTZM42022EE,
    TTZM502022EE,    
    WZ3L2022EE,
    ZZ4L2022EE,
    WWW2022EE,
    WWZ2022EE,
    WZZ2022EE,
    ZZZ2022EE,
    TTWH2022EE,
    TTWW2022EE,
    TTWZ2022EE,
    TTZH2022EE,
    TTZZ2022EE,
    TTTT2022EE,
    WWZZ3L2022EE,
    WWZZ4L2022EE,
]

mclist_2023 = [
   Bprime_M1000_2023,    
   Bprime_M1300_2023,    
   Bprime_M1600_2023,    
   Bprime_M400_2023,
   Bprime_M700_2023,
   TTHnonB2023,    
   TTWl2023,         
   TTZM42023,
   TTZM502023,    
   WZ3L2023,
   ZZ4L2023,
   WWW2023,
   WWZ2023,
   WZZ2023,
   ZZZ2023,
   TTWH2023,
   TTWW2023,
   TTWZ2023,
   TTZH2023,
   TTZZ2023,
   TTTT2023,
   WWZZ3L2023,
   WWZZ4L2023,
]

mclist_2023BPix = [
   Bprime_M1000_2023BPix,    
   Bprime_M1300_2023BPix,    
   Bprime_M1600_2023BPix,    
   Bprime_M400_2023BPix,
   Bprime_M700_2023BPix,
   TTHnonB2023BPix,    
   TTWl2023BPix,         
   TTZM42023BPix,
   TTZM502023BPix,    
   WZ3L2023BPix,
   ZZ4L2023BPix,
   WWW2023BPix,
   WWZ2023BPix,
   WZZ2023BPix,
   ZZZ2023BPix,
   TTWH2023BPix,
   TTWW2023BPix,
   TTWZ2023BPix,
   TTZH2023BPix,
   TTZZ2023BPix,
   TTTT2023BPix,
   WWZZ3L2023BPix,
   WWZZ4L2023BPix,
]

Bprime_M1000_2022.nrun = 115000.0 # from integral 115000, file Bprime_M1000_2022
Bprime_M1300_2022.nrun = 112272.0 # from integral 112272, file Bprime_M1300_2022
Bprime_M1600_2022.nrun = 110198.0 # from integral 110198, file Bprime_M1600_2022
Bprime_M700_2022.nrun = 115000.0 # from integral 115000, file Bprime_M700_2022
Bprime_M400_2022.nrun = 114284.0 # from integral 114284, file Bprime_M400_2022
DYPT402022.nrun = 49282604.17516168 # from integral 49283329, file DYPT402022
DYPT1002022.nrun = 19464992.024960656 # from integral 19465186, file DYPT1002022
DYPT2002022.nrun = 2079558.6324841394 # from integral 2079572, file DYPT2002022
DYPT4002022.nrun = 896821.4795599106 # from integral 896827, file DYPT4002022
DYPT6002022.nrun = 1059483.7292160057 # from integral 1059489, file DYPT6002022
QCDHT10002022.nrun = 20641783.522358507 # from integral 20642169, file QCDHT10002022
QCDHT12002022.nrun = 21112465.288620733 # from integral 21112863, file QCDHT12002022
QCDHT15002022.nrun = 21191233.26849927 # from integral 21191630, file QCDHT15002022
QCDHT20002022.nrun = 18132331.822590925 # from integral 18132719, file QCDHT20002022
QCDHT2002022.nrun = 20642232.586233716 # from integral 20642715, file QCDHT2002022
QCDHT4002022.nrun = 19602367.15867858 # from integral 19602817, file QCDHT4002022
QCDHT6002022.nrun = 19028037.088266045 # from integral 19028458, file QCDHT6002022
QCDHT8002022.nrun = 21601643.41405326 # from integral 21602068, file QCDHT8002022
TTHB2022.nrun = 3107723.999999993 # from integral 3177628, file TTHB2022
TTHnonB2022.nrun = 3762216.999999989 # from integral 3846525, file TTHnonB2022
TTTo2L2Nu2022.nrun = 23585788.0 # from integral 23778148, file TTTo2L2Nu2022
TTToHadronic2022.nrun = 53171840.0 # from integral 53605620, file TTToHadronic2022
TTToSemiLeptonic2022.nrun = 49368400.0 # from integral 49771670, file TTToSemiLeptonic2022
TTWl2022.nrun = 1070287.0000000002 # from integral 2056905, file TTWl2022
TTZM42022.nrun = 166448.0 # from integral 300000, file TTZM42022
TTZM502022.nrun = 208736.0 # from integral 400000, file TTZM502022
WW2L2022.nrun = 100000.0 # from integral 100000, file WW2L2022
WZ2L2022.nrun = 4163435.0 # from integral 4167791, file WZ2L2022
WZ3L2022.nrun = 98532.0 # from integral 98532, file WZ3L2022
ZZ2L2022.nrun = 97807.0 # from integral 97807, file ZZ2L2022
ZZ4L2022.nrun = 99312.0 # from integral 99312, file ZZ4L2022
WWW2022.nrun = 408136.0 # from integral 450000, file WWW2022
WWZ2022.nrun = 1774030.0 # from integral 1950044, file WWZ2022
WZZ2022.nrun = 1806417.9999999998 # from integral 1987058, file WZZ2022
ZZZ2022.nrun = 1751582.0 # from integral 1970234, file ZZZ2022
TTWH2022.nrun = 790196.0 # from integral 790196, file TTWH2022
TTWW2022.nrun = 448443.0 # from integral 448443, file TTWW2022
#TTWZ2022.nrun = 88328.0 # from integral 88328, file TTWZ2022
TTZH2022.nrun = 798996.0 # from integral 798996, file TTZH2022
TTZZ2022.nrun = 443238.0 # from integral 443238, file TTZZ2022
TTTT2022.nrun = 1076871.0 # from integral 2396925, file TTTT2022
WWZZ3L2022.nrun = 222222.0 # from integral 222222, file WWZZ3L2022
WWZZ4L2022.nrun = 222222.0 # from integral 222222, file WWZZ4L2022
Bprime_M1000_2022EE.nrun = 383618.0 # from integral 383618, file Bprime_M1000_2022EE
Bprime_M1300_2022EE.nrun = 381505.0 # from integral 381505, file Bprime_M1300_2022EE
Bprime_M1600_2022EE.nrun = 383638.0 # from integral 383638, file Bprime_M1600_2022EE
Bprime_M700_2022EE.nrun = 381495.0 # from integral 381495, file Bprime_M700_2022EE
Bprime_M400_2022EE.nrun = 378574.0 # from integral 378574, file Bprime_M400_2022EE
DYPT402022EE.nrun = 147508040.14920852 # from integral 147510349, file DYPT402022EE
DYPT1002022EE.nrun = 69960581.8077609 # from integral 69961256, file DYPT1002022EE
DYPT2002022EE.nrun = 6931428.870097844 # from integral 6931476, file DYPT2002022EE
DYPT4002022EE.nrun = 3355476.8823475027 # from integral 3355496, file DYPT4002022EE
DYPT6002022EE.nrun = 3470699.4213957614 # from integral 3470735, file DYPT6002022EE
QCDHT10002022EE.nrun = 70853284.84093562 # from integral 70854616, file QCDHT10002022EE
QCDHT12002022EE.nrun = 70803132.95404007 # from integral 70804499, file QCDHT12002022EE
QCDHT15002022EE.nrun = 63306472.68059759 # from integral 63307771, file QCDHT15002022EE
QCDHT20002022EE.nrun = 65101510.36544891 # from integral 65102938, file QCDHT20002022EE
QCDHT2002022EE.nrun = 70273873.3288849 # from integral 70275585, file QCDHT2002022EE
QCDHT4002022EE.nrun = 68705567.3962436 # from integral 68707093, file QCDHT4002022EE
QCDHT6002022EE.nrun = 63296582.77763329 # from integral 63298004, file QCDHT6002022EE
QCDHT8002022EE.nrun = 66614121.559668995 # from integral 66615474, file QCDHT8002022EE
TTHB2022EE.nrun = 10856129.999999981 # from integral 11099294, file TTHB2022EE
TTHnonB2022EE.nrun = 13649278.0 # from integral 13955780, file TTHnonB2022EE
TTTo2L2Nu2022EE.nrun = 84124383.0 # from integral 84809345, file TTTo2L2Nu2022EE
TTToHadronic2022EE.nrun = 177617421.0 # from integral 179069201, file TTToHadronic2022EE
TTToSemiLeptonic2022EE.nrun = 264850224.0 # from integral 267007920, file TTToSemiLeptonic2022EE
TTWl2022EE.nrun = 3751873.9999999995 # from integral 7212758, file TTWl2022EE
TTZM42022EE.nrun = 582589.0 # from integral 1049999, file TTZM42022EE
TTZM502022EE.nrun = 700033.0 # from integral 1343867, file TTZM502022EE
WW2L2022EE.nrun = 350000.0 # from integral 350000, file WW2L2022EE
WZ3L2022EE.nrun = 350000.0 # from integral 350000, file WZ3L2022EE
WZ2L2022EE.nrun = 14919908.0 # from integral 14935574, file WZ2L2022EE
ZZ2L2022EE.nrun = 347801.0 # from integral 347801, file ZZ2L2022EE
ZZ4L2022EE.nrun = 338117.0 # from integral 338117, file ZZ4L2022EE
WWW2022EE.nrun = 1345746.0 # from integral 1482480, file WWW2022EE
WWZ2022EE.nrun = 5094734.0 # from integral 5601076, file WWZ2022EE
WZZ2022EE.nrun = 4809662.0 # from integral 5290014, file WZZ2022EE
ZZZ2022EE.nrun = 5159256.0 # from integral 5803440, file ZZZ2022EE
TTWH2022EE.nrun = 2800000.0 # from integral 2800000, file TTWH2022EE
TTWW2022EE.nrun = 1536000.0 # from integral 1536000, file TTWW2022EE
#TTWZ2022EE.nrun = 1085872.0 # from integral 1085872, file TTWZ2022EE
TTZH2022EE.nrun = 2785771.0 # from integral 2785771, file TTZH2022EE
TTZZ2022EE.nrun = 1054000.0 # from integral 1054000, file TTZZ2022EE
TTTT2022EE.nrun = 3857788.0 # from integral 8571152, file TTTT2022EE
WWZZ3L2022EE.nrun = 777778.0 # from integral 777778, file WWZZ3L2022EE
WWZZ4L2022EE.nrun = 777778.0 # from integral 777778, file WWZZ4L2022EE
Bprime_M1000_2023.nrun = 320000.0 # from integral 320000, file Bprime_M1000_2023
Bprime_M1300_2023.nrun = 314000.0 # from integral 314000, file Bprime_M1300_2023
Bprime_M1600_2023.nrun = 320000.0 # from integral 320000, file Bprime_M1600_2023
Bprime_M400_2023.nrun = 317000.0 # from integral 317000, file Bprime_M400_2023
Bprime_M700_2023.nrun = 320000.0 # from integral 320000, file Bprime_M700_2023
DYPT402023.nrun = 100005017.52188459 # from integral 100005339, file DYPT402023
DYPT1002023.nrun = 38700477.0610977 # from integral 38700590, file DYPT1002023
DYPT2002023.nrun = 4023243.296301864 # from integral 4023259, file DYPT2002023
DYPT4002023.nrun = 2105387.3219252555 # from integral 2105393, file DYPT4002023
DYPT6002023.nrun = 2241005.0940107354 # from integral 2241010, file DYPT6002023
QCDHT10002023.nrun = 32193911.98883141 # from integral 32193981, file QCDHT10002023
QCDHT12002023.nrun = 40348858.36224707 # from integral 40348927, file QCDHT12002023
QCDHT15002023.nrun = 39490220.78218561 # from integral 39490287, file QCDHT15002023
QCDHT20002023.nrun = 42353757.052990794 # from integral 42353820, file QCDHT20002023
QCDHT2002023.nrun = 37041471.41085277 # from integral 37041533, file QCDHT2002023
QCDHT4002023.nrun = 36482983.455677524 # from integral 36483071, file QCDHT4002023
QCDHT6002023.nrun = 34513258.284363054 # from integral 34513335, file QCDHT6002023
QCDHT8002023.nrun = 37794453.052513905 # from integral 37794527, file QCDHT8002023
TTHB2023.nrun = 10607763.999999998 # from integral 10846000, file TTHB2023
TTHnonB2023.nrun = 11639625.999999998 # from integral 11901980, file TTHnonB2023
TTTo2L2Nu2023.nrun = 47811502.0 # from integral 48203000, file TTTo2L2Nu2023
TTToHadronic2023.nrun = 103547205.99999999 # from integral 104393000, file TTToHadronic2023
TTToSemiLeptonic2023.nrun = 151559604.0 # from integral 152797000, file TTToSemiLeptonic2023
TTWl2023.nrun = 2046979.0 # from integral 3935565, file TTWl2023
TTZM42023.nrun = 326292.0000000001 # from integral 591000, file TTZM42023
TTZM502023.nrun = 412853.9999999999 # from integral 794000, file TTZM502023
WW2L2023.nrun = 250000.0 # from integral 250000, file WW2L2023
WZ3L2023.nrun = 250000.0 # from integral 250000, file WZ3L2023
WZ2L2023.nrun = 8345164.000000004 # from integral 8354000, file WZ2L2023
ZZ2L2023.nrun = 250000.0 # from integral 250000, file ZZ2L2023
ZZ4L2023.nrun = 250000.0 # from integral 250000, file ZZ4L2023
WWW2023.nrun = 849916.0000000002 # from integral 936000, file WWW2023
WWZ2023.nrun = 3275962.0 # from integral 3600000, file WWZ2023
WZZ2023.nrun = 3265158.0000000023 # from integral 3591000, file WZZ2023
ZZZ2023.nrun = 3201469.9999999995 # from integral 3600000, file ZZZ2023
TTWH2023.nrun = 1960000.0 # from integral 1960000, file TTWH2023
TTWW2023.nrun = 14912000.0 # from integral 14912000, file TTWW2023
TTWZ2023.nrun = 1000000.0 # from integral 1000000, file TTWZ2023
TTZH2023.nrun = 1993000.0 # from integral 1993000, file TTZH2023
TTZZ2023.nrun = 1994000.0 # from integral 1994000, file TTZZ2023
TTTT2023.nrun = 2247088.0000000014 # from integral 4994204, file TTTT2023
WWZZ3L2023.nrun = 662667.0 # from integral 662667, file WWZZ3L2023
WWZZ4L2023.nrun = 662667.0 # from integral 662667, file WWZZ4L2023
Bprime_M1000_2023BPix.nrun = 180000.0 # from integral 180000, file Bprime_M1000_2023BPix
Bprime_M1300_2023BPix.nrun = 180000.0 # from integral 180000, file Bprime_M1300_2023BPix
Bprime_M1600_2023BPix.nrun = 177000.0 # from integral 177000, file Bprime_M1600_2023BPix
Bprime_M400_2023BPix.nrun = 180000.0 # from integral 180000, file Bprime_M400_2023BPix
Bprime_M700_2023BPix.nrun = 180000.0 # from integral 180000, file Bprime_M700_2023BPix
DYPT402023BPix.nrun = 49902787.84549243 # from integral 49902948, file DYPT402023BPix
DYPT1002023BPix.nrun = 19572849.89596818 # from integral 19572906, file DYPT1002023BPix
DYPT2002023BPix.nrun = 1964832.0398116782 # from integral 1964840, file DYPT2002023BPix
DYPT4002023BPix.nrun = 945303.1280374804 # from integral 945306, file DYPT4002023BPix
DYPT6002023BPix.nrun = 967545.5462698748 # from integral 967548, file DYPT6002023BPix
QCDHT10002023BPix.nrun = 18270242.636743385 # from integral 18270279, file QCDHT10002023BPix
QCDHT12002023BPix.nrun = 18878580.836200703 # from integral 18878616, file QCDHT12002023BPix
QCDHT15002023BPix.nrun = 17117836.22191938 # from integral 17117867, file QCDHT15002023BPix
QCDHT20002023BPix.nrun = 20420257.33347684 # from integral 20420289, file QCDHT20002023BPix
QCDHT2002023BPix.nrun = 17128014.176195327 # from integral 17128041, file QCDHT2002023BPix
QCDHT4002023BPix.nrun = 20454181.85687471 # from integral 20454226, file QCDHT4002023BPix
QCDHT6002023BPix.nrun = 19666302.66666342 # from integral 19666345, file QCDHT6002023BPix
QCDHT8002023BPix.nrun = 17683770.365553465 # from integral 17683808, file QCDHT8002023BPix
TTHB2023BPix.nrun = 5453381.999999998 # from integral 5576000, file TTHB2023BPix
TTHnonB2023BPix.nrun = 5759494.999999999 # from integral 5887987, file TTHnonB2023BPix
TTTo2L2Nu2023BPix.nrun = 24449706.000000004 # from integral 24649000, file TTTo2L2Nu2023BPix
TTToHadronic2023BPix.nrun = 52615819.99999999 # from integral 53044000, file TTToHadronic2023BPix
TTToSemiLeptonic2023BPix.nrun = 81394396.00000001 # from integral 82058000, file TTToSemiLeptonic2023BPix
TTWl2023BPix.nrun = 1028267.0 # from integral 1981391, file TTWl2023BPix
TTZM42023BPix.nrun = 162042.00000000003 # from integral 294000, file TTZM42023BPix
TTZM502023BPix.nrun = 208364.0 # from integral 400000, file TTZM502023BPix
WW2L2023BPix.nrun = 125000.0 # from integral 125000, file WW2L2023BPix
WZ3L2023BPix.nrun = 125000.0 # from integral 125000, file WZ3L2023BPix
WZ2L2023BPix.nrun = 4262560.000000002 # from integral 4267000, file WZ2L2023BPix
ZZ2L2023BPix.nrun = 121000.0 # from integral 121000, file ZZ2L2023BPix
ZZ4L2023BPix.nrun = 125000.0 # from integral 125000, file ZZ4L2023BPix
WWW2023BPix.nrun = 423054.00000000023 # from integral 466500, file WWW2023BPix
WWZ2023BPix.nrun = 1588206.0 # from integral 1746000, file WWZ2023BPix
WZZ2023BPix.nrun = 1625116.0000000014 # from integral 1788000, file WZZ2023BPix
ZZZ2023BPix.nrun = 1589388.0000000002 # from integral 1788000, file ZZZ2023BPix
TTWH2023BPix.nrun = 969000.0 # from integral 969000, file TTWH2023BPix
TTWW2023BPix.nrun = 7288000.0 # from integral 7288000, file TTWW2023BPix
TTWZ2023BPix.nrun = 497000.0 # from integral 497000, file TTWZ2023BPix
TTZH2023BPix.nrun = 994000.0 # from integral 994000, file TTZH2023BPix
TTZZ2023BPix.nrun = 992000.0 # from integral 992000, file TTZZ2023BPix
TTTT2023BPix.nrun = 1114459.0000000007 # from integral 2477775, file TTTT2023BPix
WWZZ3L2023BPix.nrun = 329333.0 # from integral 329333, file WWZZ3L2023BPix
WWZZ4L2023BPix.nrun = 325333.0 # from integral 325333, file WWZZ4L2023BPix

# update Feb2026
Bprime_M1000_2022.nrun = 115000.0 # from integral 115000, file Bprime_M1000_2022
Bprime_M1300_2022.nrun = 112272.0 # from integral 112272, file Bprime_M1300_2022
Bprime_M1600_2022.nrun = 110198.0 # from integral 110198, file Bprime_M1600_2022
Bprime_M700_2022.nrun = 115000.0 # from integral 115000, file Bprime_M700_2022
Bprime_M400_2022.nrun = 114284.0 # from integral 114284, file Bprime_M400_2022
TTHnonB2022.nrun = 3762216.999999989 # from integral 3846525, file TTHnonB2022
TTWl2022.nrun = 1070287.0000000002 # from integral 2056905, file TTWl2022
TTZM42022.nrun = 166448.0 # from integral 300000, file TTZM42022
TTZM502022.nrun = 207839.99999999994 # from integral 399000, file TTZM502022
WZ3L2022.nrun = 98532.0 # from integral 98532, file WZ3L2022
ZZ4L2022.nrun = 99312.0 # from integral 99312, file ZZ4L2022
WWW2022.nrun = 408136.0 # from integral 450000, file WWW2022
WWZ2022.nrun = 1774030.0 # from integral 1950044, file WWZ2022
WZZ2022.nrun = 1806417.9999999998 # from integral 1987058, file WZZ2022
ZZZ2022.nrun = 1751582.0 # from integral 1970234, file ZZZ2022
TTWH2022.nrun = 790196.0 # from integral 790196, file TTWH2022
TTWW2022.nrun = 448443.0 # from integral 448443, file TTWW2022
TTWZ2022.nrun = 400000.0 # from integral 400000, file TTWZ2022
TTZH2022.nrun = 798996.0 # from integral 798996, file TTZH2022
TTZZ2022.nrun = 443238.0 # from integral 443238, file TTZZ2022
TTTT2022.nrun = 1076871.0 # from integral 2396925, file TTTT2022
WWZZ3L2022.nrun = 222222.0 # from integral 222222, file WWZZ3L2022
WWZZ4L2022.nrun = 222222.0 # from integral 222222, file WWZZ4L2022
Bprime_M1000_2022EE.nrun = 383618.0 # from integral 383618, file Bprime_M1000_2022EE
Bprime_M1300_2022EE.nrun = 381505.0 # from integral 381505, file Bprime_M1300_2022EE
Bprime_M1600_2022EE.nrun = 383638.0 # from integral 383638, file Bprime_M1600_2022EE
Bprime_M700_2022EE.nrun = 381495.0 # from integral 381495, file Bprime_M700_2022EE
Bprime_M400_2022EE.nrun = 378574.0 # from integral 378574, file Bprime_M400_2022EE
TTHnonB2022EE.nrun = 13649278.0 # from integral 13955780, file TTHnonB2022EE
TTWl2022EE.nrun = 3751873.9999999995 # from integral 7212758, file TTWl2022EE
TTZM42022EE.nrun = 582589.0 # from integral 1049999, file TTZM42022EE
TTZM502022EE.nrun = 727998.0 # from integral 1400000, file TTZM502022EE
WZ3L2022EE.nrun = 350000.0 # from integral 350000, file WZ3L2022EE
ZZ4L2022EE.nrun = 338117.0 # from integral 338117, file ZZ4L2022EE
WWW2022EE.nrun = 1345746.0 # from integral 1482480, file WWW2022EE
WWZ2022EE.nrun = 5094734.0 # from integral 5601076, file WWZ2022EE
WZZ2022EE.nrun = 4809662.0 # from integral 5290014, file WZZ2022EE
ZZZ2022EE.nrun = 5159256.0 # from integral 5803440, file ZZZ2022EE
TTWH2022EE.nrun = 2800000.0 # from integral 2800000, file TTWH2022EE
TTWW2022EE.nrun = 1536000.0 # from integral 1536000, file TTWW2022EE
TTWZ2022EE.nrun = 1085872.0 # from integral 1085872, file TTWZ2022EE
TTZH2022EE.nrun = 2785771.0 # from integral 2785771, file TTZH2022EE
TTZZ2022EE.nrun = 1054000.0 # from integral 1054000, file TTZZ2022EE
TTTT2022EE.nrun = 3857788.0 # from integral 8571152, file TTTT2022EE
WWZZ3L2022EE.nrun = 777778.0 # from integral 777778, file WWZZ3L2022EE
WWZZ4L2022EE.nrun = 777778.0 # from integral 777778, file WWZZ4L2022EE
Bprime_M1000_2023.nrun = 320000.0 # from integral 320000, file Bprime_M1000_2023
Bprime_M1300_2023.nrun = 314000.0 # from integral 314000, file Bprime_M1300_2023
Bprime_M1600_2023.nrun = 320000.0 # from integral 320000, file Bprime_M1600_2023
Bprime_M400_2023.nrun = 317000.0 # from integral 317000, file Bprime_M400_2023
Bprime_M700_2023.nrun = 320000.0 # from integral 320000, file Bprime_M700_2023
TTHnonB2023.nrun = 11639625.999999998 # from integral 11901980, file TTHnonB2023
TTWl2023.nrun = 2046979.0 # from integral 3935565, file TTWl2023
TTZM42023.nrun = 326292.0000000001 # from integral 591000, file TTZM42023
TTZM502023.nrun = 415913.9999999998 # from integral 800000, file TTZM502023
WZ3L2023.nrun = 250000.0 # from integral 250000, file WZ3L2023
ZZ4L2023.nrun = 250000.0 # from integral 250000, file ZZ4L2023
WWW2023.nrun = 849916.0000000002 # from integral 936000, file WWW2023
WWZ2023.nrun = 3275962.0000000005 # from integral 3600000, file WWZ2023
WZZ2023.nrun = 3265158.0000000023 # from integral 3591000, file WZZ2023
ZZZ2023.nrun = 3201469.9999999995 # from integral 3600000, file ZZZ2023
TTWH2023.nrun = 1960000.0 # from integral 1960000, file TTWH2023
TTWW2023.nrun = 14912000.0 # from integral 14912000, file TTWW2023
TTWZ2023.nrun = 1000000.0 # from integral 1000000, file TTWZ2023
TTZH2023.nrun = 1993000.0 # from integral 1993000, file TTZH2023
TTZZ2023.nrun = 1994000.0 # from integral 1994000, file TTZZ2023
TTTT2023.nrun = 2247088.0000000014 # from integral 4994204, file TTTT2023
WWZZ3L2023.nrun = 662667.0 # from integral 662667, file WWZZ3L2023
WWZZ4L2023.nrun = 662667.0 # from integral 662667, file WWZZ4L2023
Bprime_M1000_2023BPix.nrun = 180000.0 # from integral 180000, file Bprime_M1000_2023BPix
Bprime_M1300_2023BPix.nrun = 180000.0 # from integral 180000, file Bprime_M1300_2023BPix
Bprime_M1600_2023BPix.nrun = 177000.0 # from integral 177000, file Bprime_M1600_2023BPix
Bprime_M400_2023BPix.nrun = 180000.0 # from integral 180000, file Bprime_M400_2023BPix
Bprime_M700_2023BPix.nrun = 180000.0 # from integral 180000, file Bprime_M700_2023BPix
TTHnonB2023BPix.nrun = 5759494.999999999 # from integral 5887987, file TTHnonB2023BPix
TTWl2023BPix.nrun = 1028267.0 # from integral 1981391, file TTWl2023BPix
TTZM42023BPix.nrun = 162042.00000000003 # from integral 294000, file TTZM42023BPix
TTZM502023BPix.nrun = 207706.0 # from integral 400000, file TTZM502023BPix
WZ3L2023BPix.nrun = 125000.0 # from integral 125000, file WZ3L2023BPix
ZZ4L2023BPix.nrun = 125000.0 # from integral 125000, file ZZ4L2023BPix
WWW2023BPix.nrun = 423054.00000000023 # from integral 466500, file WWW2023BPix
WWZ2023BPix.nrun = 1588206.0 # from integral 1746000, file WWZ2023BPix
WZZ2023BPix.nrun = 1625116.0000000014 # from integral 1788000, file WZZ2023BPix
ZZZ2023BPix.nrun = 1589388.0000000002 # from integral 1788000, file ZZZ2023BPix
TTWH2023BPix.nrun = 969000.0 # from integral 969000, file TTWH2023BPix
TTWW2023BPix.nrun = 7288000.0 # from integral 7288000, file TTWW2023BPix
TTWZ2023BPix.nrun = 497000.0 # from integral 497000, file TTWZ2023BPix
TTZH2023BPix.nrun = 994000.0 # from integral 994000, file TTZH2023BPix
TTZZ2023BPix.nrun = 992000.0 # from integral 992000, file TTZZ2023BPix
TTTT2023BPix.nrun = 1114459.0000000007 # from integral 2477775, file TTTT2023BPix
WWZZ3L2023BPix.nrun = 329333.0 # from integral 329333, file WWZZ3L2023BPix
WWZZ4L2023BPix.nrun = 325333.0 # from integral 325333, file WWZZ4L2023BPix
