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
SingleElecRun2024C0 = sample("SingleElecRun2024C0", 1.0, "2024", "SingleElecRun2024C0NanoList.txt","/EGamma0/Run2024C-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024D0 = sample("SingleElecRun2024D0", 1.0, "2024", "SingleElecRun2024D0NanoList.txt","/EGamma0/Run2024D-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024E0 = sample("SingleElecRun2024E0", 1.0, "2024", "SingleElecRun2024E0NanoList.txt","/EGamma0/Run2024E-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024F0 = sample("SingleElecRun2024F0", 1.0, "2024", "SingleElecRun2024F0NanoList.txt","/EGamma0/Run2024F-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024G0 = sample("SingleElecRun2024G0", 1.0, "2024", "SingleElecRun2024G0NanoList.txt","/EGamma0/Run2024G-MINIv6NANOv15-v2/NANOAOD")
SingleElecRun2024H0 = sample("SingleElecRun2024H0", 1.0, "2024", "SingleElecRun2024H0NanoList.txt","/EGamma0/Run2024H-MINIv6NANOv15-v2/NANOAOD")
SingleElecRun2024I01 = sample("SingleElecRun2024I01", 1.0, "2024", "SingleElecRun2024I01NanoList.txt","/EGamma0/Run2024I-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024I02 = sample("SingleElecRun2024I02", 1.0, "2024", "SingleElecRun2024I02NanoList.txt","/EGamma0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD")
SingleElecRun2024C1 = sample("SingleElecRun2024C1", 1.0, "2024", "SingleElecRun2024C1NanoList.txt","/EGamma1/Run2024C-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024D1 = sample("SingleElecRun2024D1", 1.0, "2024", "SingleElecRun2024D1NanoList.txt","/EGamma1/Run2024D-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024E1 = sample("SingleElecRun2024E1", 1.0, "2024", "SingleElecRun2024E1NanoList.txt","/EGamma1/Run2024E-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024F1 = sample("SingleElecRun2024F1", 1.0, "2024", "SingleElecRun2024F1NanoList.txt","/EGamma1/Run2024F-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024G1 = sample("SingleElecRun2024G1", 1.0, "2024", "SingleElecRun2024G1NanoList.txt","/EGamma1/Run2024G-MINIv6NANOv15-v2/NANOAOD")
SingleElecRun2024H1 = sample("SingleElecRun2024H1", 1.0, "2024", "SingleElecRun2024H1NanoList.txt","/EGamma1/Run2024H-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024I11 = sample("SingleElecRun2024I11", 1.0, "2024", "SingleElecRun2024I11NanoList.txt","/EGamma1/Run2024I-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024I12 = sample("SingleElecRun2024I12", 1.0, "2024", "SingleElecRun2024I12NanoList.txt","/EGamma1/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD")

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
SingleMuonRun2024C0 = sample("SingleMuonRun2024C0", 1.0, "2024", "SingleMuonRun2024C0NanoList.txt","/Muon0/Run2024C-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024D0 = sample("SingleMuonRun2024D0", 1.0, "2024", "SingleMuonRun2024D0NanoList.txt","/Muon0/Run2024D-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024E0 = sample("SingleMuonRun2024E0", 1.0, "2024", "SingleMuonRun2024E0NanoList.txt","/Muon0/Run2024E-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024F0 = sample("SingleMuonRun2024F0", 1.0, "2024", "SingleMuonRun2024F0NanoList.txt","/Muon0/Run2024F-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024G0 = sample("SingleMuonRun2024G0", 1.0, "2024", "SingleMuonRun2024G0NanoList.txt","/Muon0/Run2024G-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024H0 = sample("SingleMuonRun2024H0", 1.0, "2024", "SingleMuonRun2024H0NanoList.txt","/Muon0/Run2024H-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024I01 = sample("SingleMuonRun2024I01", 1.0, "2024", "SingleMuonRun2024I01NanoList.txt","/Muon0/Run2024I-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024I02 = sample("SingleMuonRun2024I02", 1.0, "2024", "SingleMuonRun2024I02NanoList.txt","/Muon0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD")
SingleMuonRun2024C1 = sample("SingleMuonRun2024C1", 1.0, "2024", "SingleMuonRun2024C1NanoList.txt","/Muon1/Run2024C-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024D1 = sample("SingleMuonRun2024D1", 1.0, "2024", "SingleMuonRun2024D1NanoList.txt","/Muon1/Run2024D-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024E1 = sample("SingleMuonRun2024E1", 1.0, "2024", "SingleMuonRun2024E1NanoList.txt","/Muon1/Run2024E-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024F1 = sample("SingleMuonRun2024F1", 1.0, "2024", "SingleMuonRun2024F1NanoList.txt","/Muon1/Run2024F-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024G1 = sample("SingleMuonRun2024G1", 1.0, "2024", "SingleMuonRun2024G1NanoList.txt","/Muon1/Run2024G-MINIv6NANOv15-v2/NANOAOD")
SingleMuonRun2024H1 = sample("SingleMuonRun2024H1", 1.0, "2024", "SingleMuonRun2024H1NanoList.txt","/Muon1/Run2024H-MINIv6NANOv15-v2/NANOAOD")
SingleMuonRun2024I11 = sample("SingleMuonRun2024I11", 1.0, "2024", "SingleMuonRun2024I11NanoList.txt","/Muon1/Run2024I-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024I12 = sample("SingleMuonRun2024I12", 1.0, "2024", "SingleMuonRun2024I12NanoList.txt","/Muon1/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD")

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

# diboson 3L and 4L
WZ3L2022 = sample("WZ3L2022", 4.924, "2022", "WZ3L2022NanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WZ3L2022ext = sample("WZ3L2022ext", 4.924, "2022", "WZ3L2022extNanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM")
WZ3L2022EE = sample("WZ3L2022EE", 4.924, "2022EE", "WZ3L2022EENanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WZ3L2022EEext = sample("WZ3L2022EEext", 4.924, "2022EE", "WZ3L2022EEextNanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
WZ3L2023 = sample("WZ3L2023", 4.924, "2023", "WZ3L2023NanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
WZ3L2023ext = sample("WZ3L2023ext", 4.924, "2023", "WZ3L2023extNanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15_ext1-v2/NANOAODSIM")
WZ3L2023BPix = sample("WZ3L2023BPix", 4.924, "2023BPix", "WZ3L2023BPixNanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")
WZ3L2023BPixext = sample("WZ3L2023BPixext", 4.924, "2023BPix", "WZ3L2023BPixextNanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6_ext1-v2/NANOAODSIM")
ZZ4L2022 = sample("ZZ4L2022", 1.39, "2022", "ZZ4L2022NanoList.txt", "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
ZZ4L2022ext = sample("ZZ4L2022ext", 1.39, "2022", "ZZ4L2022extNanoList.txt", "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
ZZ4L2022EE = sample("ZZ4L2022EE", 1.39, "2022EE", "ZZ4L2022EENanoList.txt", "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
ZZ4L2022EEext = sample("ZZ4L2022EEext", 1.39, "2022EE", "ZZ4L2022EEextNanoList.txt", "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
ZZ4L2023 = sample("ZZ4L2023", 1.39, "2023", "ZZ4L2023NanoList.txt", "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM")
ZZ4L2023BPix = sample("ZZ4L2023BPix", 1.39, "2023BPix", "ZZ4L2023BPixNanoList.txt", "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")

# xsec from H+ -> WA preapp
VHnonbb2022     = sample("VHnonbb2022", 1.0132, "2022", "VHnonbb2022.txt", "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM")
VHnonbb2022EE   = sample("VHnonbb2022EE", 1.0132, "2022EE", "VHnonbb2022EE.txt", "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM")
VHnonbb2023     = sample("VHnonbb2023", 1.0132, "2023", "VHnonbb2023.txt", "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
VHnonbb2023BPix = sample("VHnonbb2023BPix", 1.0132, "2023BPix", "VHnonbb2023BPix.txt", "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

# triboson
WWW2022     = sample("WWW2022", 0.2328, "2022", "WWW2022.txt", "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WWW2022EE   = sample("WWW2022EE", 0.2328, "2022EE", "WWW2022EE.txt", "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WWW2023     = sample("WWW2023", 0.2328, "2023", "WWW2023.txt", "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
WWW2023BPix = sample("WWW2023BPix", 0.2328, "2023BPix", "WWW2023BPix.txt", "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")
WWZ2022     = sample("WWZ2022", 0.1851, "2022", "WWZ2022.txt", "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WWZ2022EE   = sample("WWZ2022EE", 0.1851, "2022EE", "WWZ2022EE.txt", "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WWZ2023     = sample("WWZ2023", 0.1851, "2023", "WWZ2023.txt", "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
WWZ2023BPix = sample("WWZ2023BPix", 0.1851, "2023BPix", "WWZ2023BPix.txt", "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
WWZ4L2022     = sample("WWZ4L2022", 0.002244, "2022", "WWZ4L2022.txt", "/WWZto4L2Nu_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WWZ4L2022EE   = sample("WWZ4L2022EE", 0.002244, "2022EE", "WWZ4L2022EE.txt", "/WWZto4L2Nu_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WWZ4L2023     = sample("WWZ4L2023", 0.002244, "2023", "WWZ4L2023.txt", "/WWZto4L2Nu_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
WWZ4L2023BPix = sample("WWZ4L2023BPix", 0.002244, "2023BPix", "WWZ4L2023BPix.txt", "/WWZto4L2Nu_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

WZZ2022     = sample("WZZ2022", 0.06206, "2022", "WZZ2022.txt", "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WZZ2022EE   = sample("WZZ2022EE", 0.06206, "2022EE", "WZZ2022EE.txt", "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WZZ2023     = sample("WZZ2023", 0.06206, "2023", "WZZ2023.txt", "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
WZZ2023BPix = sample("WZZ2023BPix", 0.06206, "2023BPix", "WZZ2023BPix.txt", "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")
ZZZ2022     = sample("ZZZ2022", 0.01591, "2022", "ZZZ2022.txt", "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
ZZZ2022EE   = sample("ZZZ2022EE", 0.01591, "2022EE", "ZZZ2022EE.txt", "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
ZZZ2023     = sample("ZZZ2023", 0.01591, "2023", "ZZZ2023.txt", "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
ZZZ2023BPix = sample("ZZZ2023BPix", 0.01591, "2023BPix", "ZZZ2023BPix.txt", "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")

# 4 bosons
WWZZ3L2022     = sample("WWZZ3L2022", 0.0004888, "2022", "WWZZ3L2022NanoList.txt", "/WWZZ_3L_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WWZZ3L2022EE   = sample("WWZZ3L2022EE", 0.0004888, "2022EE", "WWZZ3L2022EENanoList.txt", "/WWZZ_3L_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WWZZ3L2023     = sample("WWZZ3L2023", 0.0004888, "2023", "WWZZ3L2023NanoList.txt", "/WWZZ_3L_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
WWZZ3L2023BPix = sample("WWZZ3L2023BPix", 0.0004888, "2023BPix", "WWZZ3L2023BPixNanoList.txt", "/WWZZ_3L_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
WWZZ4L2022     = sample("WWZZ4L2022", 0.0004888, "2022", "WWZZ4L2022NanoList.txt", "/WWZZ_4Lplus_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WWZZ4L2022EE   = sample("WWZZ4L2022EE", 0.0004888, "2022EE", "WWZZ4L2022EENanoList.txt", "/WWZZ_4Lplus_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WWZZ4L2023     = sample("WWZZ4L2023", 0.0004888, "2023", "WWZZ4L2023NanoList.txt", "/WWZZ_4Lplus_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
WWZZ4L2023BPix = sample("WWZZ4L2023BPix", 0.0004888, "2023BPix", "WWZZ4L2023BPixNanoList.txt", "/WWZZ_4Lplus_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

# Photon conversions
ZG2J2022     = sample("ZG2J2022", 0.1136, "2022", "ZG2J2022NanoList.txt", "/ZG2JtoG2L2J_EWK_MLL-50_MJJ-120_TuneCP5_withDipoleRecoil_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
ZG2J2022EE   = sample("ZG2J2022EE", 0.1136, "2022EE", "ZG2J2022EENanoList.txt", "/ZG2JtoG2L2J_EWK_MLL-50_MJJ-120_TuneCP5_withDipoleRecoil_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM")
ZG2J2023     = sample("ZG2J2023", 0.1136, "2023", "ZG2J2023NanoList.txt", "/ZG2JtoG2L2J_EWK_MLL-50_MJJ-120_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
ZG2J2023BPix = sample("ZG2J2023BPix", 0.1136, "2023BPix", "ZG2J2023BPixNanoList.txt", "/ZG2JtoG2L2J_EWK_MLL-50_MJJ-120_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTG1Jpt102022     = sample("TTG1Jpt102022", 4.216, "2022", "TTG1Jpt102022NanoList.txt", "/TTG-1Jets_PTG-10to100_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM")
TTG1Jpt102022EE   = sample("TTG1Jpt102022EE", 4.216, "2022EE", "TTG1Jpt102022EENanoList.txt", "/TTG-1Jets_PTG-10to100_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM")
TTG1Jpt102023     = sample("TTG1Jpt102023", 4.216, "2023", "TTG1Jpt102023NanoList.txt", "/TTG-1Jets_PTG-10to100_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTG1Jpt102023BPix = sample("TTG1Jpt102023BPix", 4.216, "2023BPix", "TTG1Jpt102023BPixNanoList.txt", "/TTG-1Jets_PTG-10to100_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTG1Jpt1002022     = sample("TTG1Jpt1002022", 0.4114, "2022", "TTG1Jpt1002022NanoList.txt", "/TTG-1Jets_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM")
TTG1Jpt1002022EE   = sample("TTG1Jpt1002022EE", 0.4114, "2022EE", "TTG1Jpt1002022EENanoList.txt", "/TTG-1Jets_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM")
TTG1Jpt1002023     = sample("TTG1Jpt1002023", 0.4114, "2023", "TTG1Jpt1002023NanoList.txt", "/TTG-1Jets_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTG1Jpt1002023BPix = sample("TTG1Jpt1002023BPix", 0.4114, "2023BPix", "TTG1Jpt1002023BPixNanoList.txt", "/TTG-1Jets_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTG1Jpt2002022     = sample("TTG1Jpt2002022", 0.1284, "2022", "TTG1Jpt2002022NanoList.txt", "/TTG-1Jets_PTG-200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM")
TTG1Jpt2002022EE   = sample("TTG1Jpt2002022EE", 0.1284, "2022EE", "TTG1Jpt2002022EENanoList.txt", "/TTG-1Jets_PTG-200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM")
TTG1Jpt2002023     = sample("TTG1Jpt2002023", 0.1284, "2023", "TTG1Jpt2002023NanoList.txt", "/TTG-1Jets_PTG-200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTG1Jpt2002023BPix = sample("TTG1Jpt2002023BPix", 0.1284, "2023BPix", "TTG1Jpt2002023BPixNanoList.txt", "/TTG-1Jets_PTG-200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

# t+Z/y
TZQB2022     = sample("TZQB2022", 0.07968, "2022", "TZQB2022NanoList.txt", "/TZQB-Zto2L-4FS_MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TZQB2022EE   = sample("TZQB2022EE", 0.07968, "2022EE", "TZQB2022EENanoList.txt", "/TZQB-Zto2L-4FS_MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TZQB2023     = sample("TZQB2023", 0.07968, "2023", "TZQB2023NanoList.txt", "/TZQB-Zto2L-4FS_MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TZQB2023BPix = sample("TZQB2023BPix", 0.07968, "2023BPix", "TZQB2023BPixNanoList.txt", "/TZQB-Zto2L-4FS_MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v3/NANOAODSIM")
3.873
TGQB2022     = sample("TGQB2022", 0.07968, "2022", "TGQB2022NanoList.txt", "/TGQB-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TGQB2022EE   = sample("TGQB2022EE", 0.07968, "2022EE", "TGQB2022EENanoList.txt", "/TGQB-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TGQB2023     = sample("TGQB2023", 0.07968, "2023", "TGQB2023NanoList.txt", "/TGQB-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TGQB2023BPix = sample("TGQB2023BPix", 0.07968, "2023BPix", "TGQB2023BPixNanoList.txt", "/TGQB-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

# tt+X
TTHnonB2022 = sample("TTHnonB2022", 0.570*(1.0-0.5824), "2022", "TTHnonB2022NanoList.txt", "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM")
TTHnonB2022EE = sample("TTHnonB2022EE", 0.570*(1.0-0.05824), "2022EE", "TTHnonB2022EENanoList.txt", "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTHnonB2023 = sample("TTHnonB2023", 0.570*(1.0-0.05824), "2023", "TTHnonB2023NanoList.txt", "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
TTHnonB2023BPix = sample("TTHnonB2023BPix", 0.570*(1.0-0.05824), "2023BPix", "TTHnonB2023BPixNanoList.txt", "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")

TTWl2022 = sample("TTWl2022", 0.2505, "2022", "TTWl2022NanoList.txt", "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-mg35x_130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTWl2022EE = sample("TTWl2022EE", 0.2505, "2022EE", "TTWl2022EENanoList.txt", "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-mg35x_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTWl2023 = sample("TTWl2023", 0.2505, "2023", "TTWl2023NanoList.txt", "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-mg35x_130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTWl2023BPix = sample("TTWl2023BPix", 0.2505, "2023BPix", "TTWl2023BPixNanoList.txt", "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-mg35x_130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

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

# tt + XX
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
    "WWZZ3L2022":     WWZZ3L2022,
    "WWZZ3L2022EE":   WWZZ3L2022EE,
    "WWZZ3L2023":     WWZZ3L2023,
    "WWZZ3L2023BPix": WWZZ3L2023BPix,
    "WWZZ4L2022":     WWZZ4L2022,
    "WWZZ4L2022EE":   WWZZ4L2022EE,
    "WWZZ4L2023":     WWZZ4L2023,
    "WWZZ4L2023BPix": WWZZ4L2023BPix,
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
    "WWZZ4L2022":     WWZZ4L2022,
    "WWZZ4L2022EE":   WWZZ4L2022EE,
    "WWZZ4L2023":     WWZZ4L2023,
    "WWZZ4L2023BPix": WWZZ4L2023BPix,
}

samples_electroweak3 = {
    "WZ3L2022":       WZ3L2022,
    "WZ3L2022EE":     WZ3L2022EE,
    "WZ3L2023":       WZ3L2023,
    "WZ3L2023BPix":   WZ3L2023BPix,
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

samples_higgs = {
    "VHnonbb2022": VHnonbb2022,
    "VHnonbb2022EE": VHnonbb2022EE,
    "VHnonbb2023": VHnonbb2023,
    "VHnonbb2023BPix": VHnonbb2023BPix,
    }

samples_conversion = {
    "ZG2J2022"           = ZG2J2022,
    "ZG2J2022EE"         = ZG2J2022EE,
    "ZG2J2023"           = ZG2J2023,
    "ZG2J2023BPix"       = ZG2J2023BPix,
    "TTG1Jpt102022"      = TTG1Jpt102022,
    "TTG1Jpt102022EE"    = TTG1Jpt102022EE,   
    "TTG1Jpt102023"      = TTG1Jpt102023, 
    "TTG1Jpt102023BPix"  = TTG1Jpt102023BPix, 
    "TTG1Jpt1002022"     = TTG1Jpt1002022,
    "TTG1Jpt1002022EE"   = TTG1Jpt1002022EE, 
    "TTG1Jpt1002023"     = TTG1Jpt1002023,
    "TTG1Jpt1002023BPix" = TTG1Jpt1002023BPix, 
    "TTG1Jpt2002022"     = TTG1Jpt2002022,
    "TTG1Jpt2002022EE"   = TTG1Jpt2002022EE, 
    "TTG1Jpt2002023"     = TTG1Jpt2002023,
    "TTG1Jpt2002023BPix" = TTG1Jpt2002023BPix, 
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
    "TTZM42022":       TTZM42022,       
    "TTZM42022EE":     TTZM42022EE,     
    "TTZM42023":       TTZM42023,       
    "TTZM42023BPix":   TTZM42023BPix,   
    "TTZM502022":    TTZM502022,    
    "TTZM502022EE":  TTZM502022EE,  
    "TTZM502023":    TTZM502023,    
    "TTZM502023BPix":TTZM502023BPix,
    "TTZM502022ext":    TTZM502022ext  
    "TTZM502022EEext":  TTZM502022EEext
    "TTZM502023ext":    TTZM502023ext  
    "TTZM502023BPixext":TTZM502023BPixext
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
    "TTZM502022ext":    TTZM502022ext  
    "TTZM502022EEext":  TTZM502022EEext
    "TTZM502023ext":    TTZM502023ext  
    "TTZM502023BPixext":TTZM502023BPixext
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
    "TTZM502022ext":    TTZM502022ext  
    "TTZM502022EEext":  TTZM502022EEext
    "TTZM502023ext":    TTZM502023ext  
    "TTZM502023BPixext":TTZM502023BPixext
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
    "TZQB2022" : TZQB2022,
    "TZQB2022EE" : TZQB2022EE,
    "TZQB2023" : TZQB2023,
    "TZQB2023BPix" : TZQB2023BPix,
    "TGQB2022" : TGQB2022,
    "TGQB2022EE" : TGQB2022EE,
    "TGQB2023" : TGQB2023,
    "TGQB2023BPix" : TGQB2023BPix,
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
    TTZM502022ext,    
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
    VHnonbb2022,
    TZQB2022,
    TGQB2022,
    ZG2J2022,
    TTG1Jpt102022,
    TTG1Jpt1002022,
    TTG1Jpt2002022,
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
    TTZM502022EEext,    
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
    VHnonbb2022EE,
    TZQB2022EE,
    TGQB2022EE,
    ZG2J2022EE,
    TTG1Jpt102022EE,   
    TTG1Jpt1002022EE, 
    TTG1Jpt2002022EE, 
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
    TTZM502023ext,    
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
    VHnonbb2023,
    TZQB2023,
    TGQB2023,
    ZG2J2023,
    TTG1Jpt102023, 
    TTG1Jpt1002023,
    TTG1Jpt2002023,
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
    TTZM502023BPixext  
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
    VHnonbb2023BPix,
    TZQB2023BPix,
    TGQB2023BPix,
    ZG2J2023BPix,
    TTG1Jpt102023BPix, 
    TTG1Jpt1002023BPix, 
    TTG1Jpt2002023BPix, 
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

# update May2026
