#!/usr/bin/python
from ROOT import TH1D,TFile,TTree,gROOT
from ctypes import c_double
import os, sys
parent = os.path.dirname(os.getcwd())
sys.path.append(parent)
from samples import lumiStr

gROOT.SetBatch(1)

indirB = 'templatesB_Oct2023SysAll/'
indirD = 'templatesD_Oct2023SysAll/'
iPlot = 'BpMass_ABCDnn'
hFileB = TFile.Open(f'{indirB}/templates_{iPlot}_{lumiStr}.root', "READ")
hFileD = TFile.Open(f'{indirD}/templates_{iPlot}_{lumiStr}.root', "READ")




