# run with ./runPlotting_rdf.sh (chmod +x runPlotting_rdf.sh first if no permission)
# python3 groupHists.py $iPlot $region $isCategorized $pfix
# python3 plotHists.py $iPlot $region $isCategorized $pfix $blind $yLog $isRebinned
#pfix = "_Apr2024SysAll"
#isRebinned = "_rebinned_stat0p2"
# control plots

plotList='Nleps lepID lepCharge lepChargeSum JetEta JetPhi JetBtag '
#HT NPV lepPt lepEta lepPhi lepID MET METphi HT JetPt NJets NBJets BpMassDiff BpMass1 BpMass2'
#BpMassAve 
for iPlot in $plotList; do
    echo $iPlot
    #python3 groupHists.py $iPlot all False _Oct2025_NoSys
    python3 plotHists.py $iPlot all False _Oct2025_NoSys False False
done

plotList='Nleps lepChargeSum'
# lepPt HT BpMassAve'
#for iPlot in $plotList; do
    #echo $iPlot
    #python3 groupHists.py $iPlot 3lep False _Oct2025_NoSys
    #python3 plotHists.py $iPlot 3lep False _Oct2025_NoSys False False
    #python3 groupHists.py $iPlot 4lep False _Oct2025_NoSys
    #python3 plotHists.py $iPlot 4lep False _Oct2025_NoSys False False
#done


#_rebinned_stat0p2

 
