# run with ./runPlotting_rdf.sh (chmod +x runPlotting_rdf.sh first if no permission)
# python3 groupHists.py $iPlot $region $isCategorized $pfix
# python3 plotHists.py $iPlot $region $isCategorized $pfix $blind $yLog $isRebinned
#pfix = "_Apr2024SysAll"
#isRebinned = "_rebinned_stat0p2"
# control plots
plotList='lepEta lepPhi lepPt lepIso MET METphi JetEta JetPhi JetPt JetBtag FatJetEta FatJetPhi FatJetPt FatJetTag BpMass'
for iPlot in $plotList; do
    echo $iPlot
    python3 groupHists.py $iPlot all False _Apr2024SysAll
    python3 plotHists.py $iPlot all False _Apr2024SysAll False False
done
#_rebinned_stat0p2

# signal region plots
plotList='BpMass BpMass_ABCDnn'
for iPlot in $plotList; do
    echo $iPlot
    python3 groupHists.py $iPlot D True _Apr2024SysAll
    python3 plotHists.py $iPlot D True _Apr2024SysAll False False
done
 
