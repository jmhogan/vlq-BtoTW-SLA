import os,sys
from ROOT import TFile, TObject, RooArgSet

## Arguments: limit directory name; mass point; signal amount to inject; number of toys

## Make a datacard first with datacard.py!

limitdir = sys.argv[1]
path = limitdir+'/'
os.chdir(path)
blind = True
morph = False

print('====================================================================')
print('==   Launching limits for in',limitdir)
print('==   ...')

if not morph:
    if blind:

        print('***** Running Asymptotic CLs limits for all masses in'+os.getcwd()+' *****')
        print('Running Asymptotic CLs limits for all masses')
        print('Command = combineTool.py -M AsymptoticLimits -d cmb/*/workspace.root --there -n .limit --run=blind')
        os.system('combineTool.py -M AsymptoticLimits -d cmb/*/workspace.root --there -n .limit --run=blind') #
        
        print('Making a JSON file')
        print('Command = combineTool.py -M CollectLimits cmb/*/*.limit.* --use-dirs -o limits_cmb.json')
        os.system('combineTool.py -M CollectLimits cmb/*/*.limit.* --use-dirs -o limits_cmb.json')

    else:
        print('***** Running Asymptotic CLs limits for all masses in'+os.getcwd()+' *****')
        print('Running Asymptotic CLs limits for all masses')
        print('Command = combineTool.py -M AsymptoticLimits -d cmb/*/workspace.root --there -n .limitUB')
        os.system('combineTool.py -M AsymptoticLimits -d cmb/*/workspace.root --there -n .limitUB') #
        
        print('Making a JSON file')
        print('Command = combineTool.py -M CollectLimits cmb/*/*.limitUB.* --use-dirs -o limitsUB_cmb.json')
        os.system('combineTool.py -M CollectLimits cmb/*/*.limitUB.* --use-dirs -o limitsUB_cmb.json')

else:

    masks = 'mask_Bp_isL_tagTjet_D_0_Combine=1,mask_Bp_isL_tagWjet_D_0_Combine=1,mask_Bp_isL_untagWlep_D_0_Combine=1,mask_Bp_isL_untagTlep_D_0_Combine=1' # mask D for initial fit on untested masses
    # signal scale default is 1 pb, should be good for V-only fit

    for mass in ['800','1000','1200','1300','1400','1500','1600','1700','1800','2000']:
        os.chdir('cmb/'+mass+'/')
        if os.path.exists('morphedWorkspace.root'): continue

        # check for consistency with the initial fit settings used for combine tests. Sometimes specific tweaks may be needed to get consistent converging fits
        print("Running Fit Diagnostics for initial workspace with SR channels masked")
        print('Command = combine -M FitDiagnostics -d workspace.root --rMin -5 --rMax 5 --saveWorkspace -n Masked --cminDefaultMinimizerStrategy 0 --setParameters '+masks)
        os.system('combine -M FitDiagnostics -d workspace.root --rMin -5 --rMax 5 --saveWorkspace -n Masked --cminDefaultMinimizerStrategy 0 --setParameters '+masks)
        
        print("Creating initialFit snapshot file: morphedWorkspace.root")
        w_f = TFile.Open('higgsCombineMasked.FitDiagnostics.mH120.root')
        w = w_f.Get('w')
        fr_f = TFile.Open('fitDiagnosticsMasked.root')
        fr = fr_f.Get('fit_b')
        myargs = RooArgSet(fr.floatParsFinal())
        w.saveSnapshot('initialFit',myargs,True)
        fout = TFile('morphedWorkspace.root', "recreate")
        fout.WriteTObject(w,'w')
        fout.Close()
        os.chdir('../../')

    # now unmask D, remask V
    masks = 'mask_Bp_isL_tagTjet_D_0_Combine=0,mask_Bp_isL_tagWjet_D_0_Combine=0,mask_Bp_isL_untagWlep_D_0_Combine=0,mask_Bp_isL_untagTlep_D_0_Combine=0,mask_Bp_isL_tagTjet_V_0_Combine=1,mask_Bp_isL_tagWjet_V_0_Combine=1,mask_Bp_isL_untagWlep_V_0_Combine=1,mask_Bp_isL_untagTlep_V_0_Combine=1' # unmask D, mask V after initial fit
    masks = masks+',signalScale=0.001' # 1 fb
    
    print('Command = combineTool.py -M AsymptoticLimits -d cmb/*/morphedWorkspace.root --snapshotName initialFit --there -n .limitM --parallel 5 --run=blind --setParameters '+masks)
    os.system('combineTool.py -M AsymptoticLimits -d cmb/*/morphedWorkspace.root --snapshotName initialFit --there -n .limitM --parallel 5 --run=blind --setParameters '+masks) #

    print('Command = combineTool.py -M CollectLimits cmb/*/*.limitM.* --use-dirs -o limitsM_cmb.json')
    os.system('combineTool.py -M CollectLimits cmb/*/*.limitM.* --use-dirs -o limitsM_cmb.json')

print('Done!')
print('====================================================================')
