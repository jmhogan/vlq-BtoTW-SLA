from sampleList_pdfCheck_Apr2024 import sampleList_fullRun2
import ROOT

for sample in sampleList_fullRun2:
    standard=103 # 101 for BpM,STs 103 for bkg, QCD and most of other bkgs
    try:
        notStandard = ROOT.RDataFrame('Events_Nominal', 'root://cmseos.fnal.gov//store/user/jmanagan/BtoTW_Apr2024_fullRun2/'+sample)\
                     .Filter(f'nLHEPdfWeight!={standard}')\
                     .Count().GetValue()
        
        if notStandard>0:
            print(f'Not {standard}:{sample}')
            
    except:
        print("No pdf branch: "+sample)

