import os,sys
from ROOT import TFile, TCanvas, TLine, TTree, TChain
execfile("/uscms_data/d3/jmanagan/EOSSafeUtils.py")

limitdir = sys.argv[1]
mass = sys.argv[2]

name = limitdir.replace('limits_templatesABCDnn_V_Oct2024_','').replace('limits_templatesABCDnn_DV_Oct2024_','')
path = limitdir+'/cmb/'+mass

os.chdir(path)

RFile=TFile.Open('root://cmseos.fnal.gov//store/user/jmanagan/CombineV10_BpGOF/'+limitdir+'_'+mass+'/higgsCombineTest.GoodnessOfFit.mH120.root')
data = RFile.Get('limit')
data.GetEntry(0)
datachi2 = data.limit

rootfiles = EOSlist_root_files('/store/user/jmanagan/CombineV10_BpGOF/'+limitdir+'_'+mass+'/')	

limit1 = TChain('limit')
for i in range(0,len(rootfiles)):
    if 'higgsCombineTest.GoodnessOfFit' not in rootfiles[i]: continue
    if 'higgsCombineTest.GoodnessOfFit.mH120.root' in rootfiles[i]: continue
    limit1.Add('root://cmseos.fnal.gov//store/user/jmanagan/CombineV10_BpGOF/'+limitdir+'_'+mass+'/'+rootfiles[i])

#RFile1=TFile.Open('higgsCombineTest.GoodnessOfFit.mH120.123456.root')
#limit1=RFile1.Get('limit')
GoF_can=TCanvas('GoodnessOfFit','GoodnessOfFit',800,600)
limit1.Draw('limit','','pe')
line=TLine(datachi2,0,datachi2,25)
line.SetLineColor(2)
line.SetLineWidth(2)
GoF_can.Update()
line.Draw('Draw')

GoF_can.SaveAs('GoodnessOfFit.png')
GoF_can.SaveAs('GoodnessOfFit.pdf')

