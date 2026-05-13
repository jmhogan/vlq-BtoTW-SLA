import os,sys
from ROOT import TFile, TH1
from samples import sample, mclist_2022, mclist_2022EE, mclist_2023, mclist_2023BPix
from utils import *
from math import sqrt

## something about samples goes here

for sample in mclist_2022:
    #print('-------------------------------------------------------')
    
    samplename = sample.samplename.split('/')[1]
    process = sample.samplename.split('/')[2]
    if (("_ext1" in process)): samplename += "ext1"
    elif (("_ext2" in process)): samplename += "ext2"
    elif (("_ext3" in process)): samplename = "ext3"

    step1dir = 'root://cmseos.fnal.gov//store/user/lpchtop/BBto2b4tau_May2026_Run3/'
    tree = readTreeNominal(samplename,"2022",step1dir,"Runs")

    integral = 0
    adjusted = 0
    for irun in range(tree.GetEntries()):
        tree.GetEntry(irun)
        integral += tree.genEventCount
        adjusted += tree.genEventSumw/sqrt(tree.genEventSumw2/tree.genEventCount)

    print(sample.prefix+'.nrun = '+str(adjusted)+' # from integral '+str(integral)+', file '+sample.prefix)

    #if 'Bp' in sample:
        # use the LHEScaleWeight and LHEPDFWeight to extract the SFs

for sample in mclist_2022EE:
    #print('-------------------------------------------------------')
    
    samplename = sample.samplename.split('/')[1]
    process = sample.samplename.split('/')[2]
    if (("_ext1" in process)): samplename += "ext1"
    elif (("_ext2" in process)): samplename += "ext2"
    elif (("_ext3" in process)): samplename = "ext3"

    step1dir = 'root://cmseos.fnal.gov//store/user/lpchtop/BBto2b4tau_May2026_Run3/'
    tree = readTreeNominal(samplename,"2022EE",step1dir,"Runs")

    integral = 0
    adjusted = 0
    for irun in range(tree.GetEntries()):
        tree.GetEntry(irun)
        integral += tree.genEventCount
        adjusted += tree.genEventSumw/sqrt(tree.genEventSumw2/tree.genEventCount)

    print(sample.prefix+'.nrun = '+str(adjusted)+' # from integral '+str(integral)+', file '+sample.prefix)

    #if 'Bp' in sample:
        # use the LHEScaleWeight and LHEPDFWeight to extract the SFs

for sample in mclist_2023:
    #print('-------------------------------------------------------')
    
    samplename = sample.samplename.split('/')[1]
    process = sample.samplename.split('/')[2]
    if (("_ext1" in process)): samplename += "ext1"
    elif (("_ext2" in process)): samplename += "ext2"
    elif (("_ext3" in process)): samplename = "ext3"

    step1dir = 'root://cmseos.fnal.gov//store/user/lpchtop/BBto2b4tau_May2026_Run3/'
    tree = readTreeNominal(samplename,"2023",step1dir,"Runs")

    integral = 0
    adjusted = 0
    for irun in range(tree.GetEntries()):
        tree.GetEntry(irun)
        integral += tree.genEventCount
        adjusted += tree.genEventSumw/sqrt(tree.genEventSumw2/tree.genEventCount)

    print(sample.prefix+'.nrun = '+str(adjusted)+' # from integral '+str(integral)+', file '+sample.prefix)

    #if 'Bp' in sample:
        # use the LHEScaleWeight and LHEPDFWeight to extract the SFs

for sample in mclist_2023BPix:
    #print('-------------------------------------------------------')
    
    samplename = sample.samplename.split('/')[1]
    process = sample.samplename.split('/')[2]
    if (("_ext1" in process)): samplename += "ext1"
    elif (("_ext2" in process)): samplename += "ext2"
    elif (("_ext3" in process)): samplename = "ext3"

    step1dir = 'root://cmseos.fnal.gov//store/user/lpchtop/BBto2b4tau_May2026_Run3/'
    tree = readTreeNominal(samplename,"2023BPix",step1dir,"Runs")

    integral = 0
    adjusted = 0
    for irun in range(tree.GetEntries()):
        tree.GetEntry(irun)
        integral += tree.genEventCount
        adjusted += tree.genEventSumw/sqrt(tree.genEventSumw2/tree.genEventCount)

    print(sample.prefix+'.nrun = '+str(adjusted)+' # from integral '+str(integral)+', file '+sample.prefix)

    #if 'Bp' in sample:
        # use the LHEScaleWeight and LHEPDFWeight to extract the SFs


