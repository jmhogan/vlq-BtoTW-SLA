# run with ./runPlotting_rdf.sh (chmod +x runPlotting_rdf.sh first if no permission)
# python3 groupHists.py $iPlot $region $isCategorized $pfix
# python3 plotHists.py $iPlot $region $isCategorized $pfix $blind $yLog $isRebinned

plotList='JetEta JetPhi JetBtag HT NPV HT JetPt NJets NBJets BpMassAve MET METphi Nleps lepID lepCharge lepChargeSum lepPt lepEta lepID'

for iPlot in $plotList; do
   echo $iPlot
   python3 groupHists.py $iPlot 3lep False _May2026
   python3 plotHists.py $iPlot 3lep False _May2026 False False
done

plotList='BpMassAve VLQBBbarMass VLQBBbarCosDecayAngle VLQBBbarDeltaPhiDecayAngle VLQtau11Mass VLQtau12Mass VLQtau21Mass VLQtau22Mass VLQBBbarDeltaPhiVisible VLQBBbarDeltaPhiDecayVisible VLQBBbarDeltaPhiBoostVisible VLQBBbarVisibleShape VLQMassAve lepPt HT BpMassAve'
for iPlot in $plotList; do
    echo $iPlot
    python3 groupHists.py $iPlot 4lep False _May2026
    python3 plotHists.py $iPlot 4lep False _May2026 True False
done

 
