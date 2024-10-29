import os,sys
from ROOT import TFile, TObject, RooArgSet

## Arguments: limit directory name; mass point; signal amount to inject; number of toys

## Make a datacard first with datacard.py!

print 'HELLO!'

limitdir = sys.argv[1]
mass = sys.argv[2]
rInj = int(sys.argv[3])
nToys = int(sys.argv[4])

name = limitdir.replace('limits_templatesABCDnn_V_Oct2024_','').replace('limits_templatesABCDnn_DV_Oct2024_','')+'InjR'+str(rInj)
path = limitdir+'/cmb/'+mass

isSR = False
if '_D' in limitdir: isSR = True

os.chdir(path)

filename = 'initialFitWorkspace.root'
if isSR: filename = 'morphedWorkspace.root'

if not isSR and not os.path.exists(filename):

    # no masking is needed here since only V will be in the workspace.
    # check whether the 1 pb normalization is fine for getting r ~ 1
    
    print "Running Fit Diagnostics for initial workspace"
    print 'Command = combine -M FitDiagnostics -d workspace.root --saveWorkspace --saveShapes --plots --setParameters signalScale=1'
    os.system('combine -M FitDiagnostics -d workspace.root --saveWorkspace --saveShapes --plots --setParameters signalScale=1')
    
    print "Creating initialFit snapshot file: initialFitWorkspace.root"
    w_f = TFile.Open('higgsCombineTest.FitDiagnostics.mH120.root')
    w = w_f.Get('w')
    fr_f = TFile.Open('fitDiagnostics.root')
    fr = fr_f.Get('fit_b')
    myargs = RooArgSet(fr.floatParsFinal())
    w.saveSnapshot('initialFit',myargs,True)
    fout = TFile('initialFitWorkspace.root',"recreate")
    fout.WriteTObject(w,'w')
    fout.Close()

print 'looking for',filename,'in',path
if isSR and not os.path.exists(filename):
    masks = 'mask_Bp_isL_tagTjet_D_0_Combine=1,mask_Bp_isL_tagWjet_D_0_Combine=1,mask_Bp_isL_untagWlep_D_0_Combine=1' ## this is for MC, adapt for ABCDnn

    masks = masks+',signalScale=1' #1pb for V-only fit

    print "Running Fit Diagnostics for initial workspace with SR channels masked: Mass =",mass
    print 'Command = combine -M FitDiagnostics -d workspace.root --saveWorkspace -n Masked --cminDefaultMinimizerStrategy 0 --setParameters '+masks
    os.system('combine -M FitDiagnostics -d workspace.root --saveWorkspace -n Masked --cminDefaultMinimizerStrategy 0 --setParameters '+masks)
    #print "Running Fit Diagnostics for initial workspace with SR channels masked"
    #print 'Command = combine -M FitDiagnostics -d workspace.root --saveWorkspace --saveShapes --plots -n Masked --setParameters '+masks
    #os.system('combine -M FitDiagnostics -d workspace.root --saveWorkspace --saveShapes --plots -n Masked --setParameters '+masks)

    print "Creating initialFit snapshot file: morphedWorkspace.root"
    w_f = TFile.Open('higgsCombineMasked.FitDiagnostics.mH120.root')
    w = w_f.Get('w')
    fr_f = TFile.Open('fitDiagnosticsMasked.root')
    fr = fr_f.Get('fit_b')
    myargs = RooArgSet(fr.floatParsFinal())
    w.saveSnapshot('initialFit',myargs,True)
    fout = TFile('morphedWorkspace.root', "recreate")
    fout.WriteTObject(w,'w')
    fout.Close()


print "Done!"
print "NOW -- Go run runCondorToys.py!"
