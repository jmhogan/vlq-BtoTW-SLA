import os,sys,datetime,itertools,math

# python3 doCondorHists.py [region] [procs] [categorize]
# python3 doCondorHists.py all all 0

thisDir = os.getcwd()
if thisDir[-13:] == 'makeTemplates': runDir = thisDir[:-13]
else: runDir = thisDir
if os.getcwd()[-17:] == 'singleLepAnalyzer': os.chdir(os.getcwd()+'/makeTemplates/')
outputDir = thisDir+'/'

region = sys.argv[1] #all, BAX, DCY, individuals
procs = sys.argv[2] #datsig, top, other, all
categorize = int(sys.argv[3]) #0 = L, 1 = EMT, 2 = all the options

cTime=datetime.datetime.now()
date='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
time='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)
pfix = 'templates'+region
if not categorize: pfix='kinematics'+region

pfix+='_Dec2025_RJR'

plotList = [#distribution name as defined in "doHists.py"
        # 'NPV'   ,#:('PV_npvs',linspace(0,80,81).tolist(),';N PVs'),
        #'Nleps' ,#:('NgoodLeptons',linspace(0,5,5).tolist(),';N good leptons'),
        'lepPt' ,#:('Good4Lepton_pt',linspace(0, 1000, 51).tolist(),';lepton p_{T} [GeV]'),
        # 'lepEta',#:('Good4Lepton_eta',linspace(-2.5, 2.5, 51).tolist(),';lepton #eta'),
        # 'lepPhi',#:('Good4Lepton_phi',linspace(-3.2,3.2,65).tolist(),';lepton #phi'),
        #'lepID',#:('Good4Lepton_ID',linspace(0,0.2,51).tolist(),';lepton flavor'),
        #'lepCharge',#:('Good4Lepton_charge',linspace(-2,2,5).tolist(),';lepton charge'),
        #'lepChargeSum',#:('Sum(Good4Lepton_charge)',linspace(-5,5,11).tolist(),';lepton charge sum'),
        # 'MET'   ,#:('MET_ptcorr',linspace(0, 1000, 51).tolist(),';#slash{E}_{T} [GeV]'),
        # 'METphi',#:('MET_phicorr',linspace(-3.2,3.2, 65).tolist(),';#slash{E}_{T} phi'),
        #'HT',#:('gcJet_ht',linspace(0, 5000, 51).tolist(),';H_{T} (GeV)'),
        # 'ST',#:('gcJet_ST',linspace(0, 5000, 51).tolist(),';S_{T} (GeV)'),
        # 'JetEta',#:('gcJet_eta',linspace(-3, 3, 41).tolist(),';central AK4 jet #eta'),
        'JetPt' ,#:('gcJet_pt',linspace(0, 1500, 51).tolist(),';central AK4 jet p_{T} [GeV]'),
        # 'JetPhi',#:('gcJet_phi',linspace(-3.2,3.2, 65).tolist(),';central AK4 jet phi'),
        # 'JetBtag',#:('gcJet_PNet',linspace(0,1,51).tolist(),';central AK4 jet DeepJet disc'),
        # 'NJets' ,#:('NgoodcleanJets',linspace(0, 10, 11).tolist(),';central AK4 jet multiplicity'),
        # 'NBJets',#:('NJets_PNetL',linspace(0, 10, 11).tolist(),';ParticleNet b-tag loose multiplicity'),
        #'BpMassAve',#:('0.5*(B1finalM+B2finalM)',linspace(0,1800,31).tolist(),';Average B quark mass [GeV]'),
        # 'BpMassDiff',#:('abs(B1finalM-B2finalM)',linspace(0,1800,31).tolist(),';Difference in B quark masses [GeV]'),
        # 'BpMass1',#:('B1finalM',linspace(0,1800,31).tolist(),';B quark 1 mass [GeV]'),
        # 'BpMass2',#:('B2finalM',linspace(0,1800,31).tolist(),';B quark 2 mass [GeV]'),
        #'VLQBBbarMass',#:('VLQ_BBbar_mass',linspace(0,4000,51).tolist(),';BBbar mass [GeV]'),
        #'VLQBBbarCosDecayAngle',#:('VLQ_BBbar_cosDecayAngle',linspace(-1.6,1.6,65).tolist(),';BBbar Cos Decay Angle'),
        #'VLQBBbarDeltaPhiDecayAngle',#:('VLQ_BBbar_deltaPhiDecayAngle',linspace(0,3.2,65).tolist(),';BBbar Delta Decay #phi'),
        #'VLQBbarMass',#:('VLQ_Bbar_mass',linspace(0,4000,51).tolist(),';Bbar mass [GeV]'),
        #'VLQBbarCosDecayAngle',#:('VLQ_Bbar_cosDecayAngle',linspace(-1.6,1.6,65).tolist(),';Bbar Cos Decay Angle'),
        #'VLQBbarDeltaPhiDecayAngle',#:('VLQ_Bbar_deltaPhiDecayAngle',linspace(0,3.2,65).tolist(),';Bbar Delta Decay #phi'),
        #'VLQBMass',#:('VLQ_B_mass',linspace(0,4000,51).tolist(),';B mass [GeV]'),
        #'VLQBCosDecayAngle',#:('VLQ_B_cosDecayAngle',linspace(-1.6,1.6,65).tolist(),';B Cos Decay Angle'),
        #'VLQBDeltaPhiDecayAngle',#:('VLQ_B_deltaPhiDecayAngle',linspace(0,3.2,65).tolist(),';B Delta Decay #phi'),
        #'VLQtau11Mass',#:('VLQ_tau11_mass',linspace(0,500,51).tolist(),';tau11 mass [GeV]'),
        #'VLQtau12Mass',#:('VLQ_tau12_mass',linspace(0,500,51).tolist(),';tau12 mass [GeV]'),
        #'VLQtau21Mass',#:('VLQ_tau21_mass',linspace(0,500,51).tolist(),';tau21 mass [GeV]'),
        #'VLQtau22Mass',#:('VLQ_tau22_mass',linspace(0,500,51).tolist(),';tau22 mass [GeV]'),
        #'VLQBBbarDeltaPhiVisible',#:('VLQ_BBbar_DeltaPhiVisible',linspace(0,3.2,65).tolist(),';BBbar Delta #phi Visible'),
        #'VLQBBbarDeltaPhiDecayVisible',#:('VLQ_BBbar_DeltaPhiDecayVisible',linspace(0,3.2,65).tolist(),';BBbar Delta #phi Decay Visible'),
        #'VLQBBbarDeltaPhiBoostVisible',#:('VLQ_BBbar_DeltaPhiBoostVisible',linspace(0,3.2,65).tolist(),';BBbar Delta #phi Boost Visible'),
        #'VLQBBbarVisibleShape',#:('VLQ_BBbar_VisibleShape',linspace(0,1,51).tolist(),';BBbar Visible Shape'),
        #'VLQMassAve',#:('0.5*(VLQBMass+VLQBbarMass)',linspace(0,5000,51).tolist(),';B and Bbar mass averaged [GeV]'),
        #'VLQCosDecayAngleAve',#:('0.5*(VLQ_B_cosDecayAngle+VLQ_Bbar_cosDecayAngle)',linspace(-1.6,1.6,65).tolist(),';cos(Avg(B,Bbar) decay angle)'),
        #'VLQDeltaPhiDecayAngleAve',#:('0.5*(VLQ_B_deltaPhiDecayAngle+VLQ_Bbar_deltaPhiDecayAngle)',linspace(0,3.2,65).tolist(),';Avg(B,Bbar) Delta #phi decay angle)'),
]

isEMlist = ['L'] 
if categorize == 1:
        isEMlist = ['E','M','T']
if categorize == 2:
        pass
        #isEMlist= # long thing.


taglist = ['all']

outDir = outputDir+pfix+'/'
print(outDir)
if not os.path.exists(outDir): os.system('mkdir '+outDir)
if '2D' in outDir:
        os.system('cp ../analyze2D_RDF.py ../utils.py ../samples.py doCondorHists2D.sh '+outDir+'/')
        os.system('cp doHists2D_rdf.py '+outDir+'/doHists2D_rdf_'+procs+'.py')
else:
        os.system('cp ../analyze_RDF.py ../utils.py ../samples.py doCondorHists.sh '+outDir+'/')
        os.system('cp doHists_rdf.py '+outDir+'/doHists_rdf_'+procs+'.py')
os.chdir(outDir)

catlist = list(itertools.product(isEMlist,taglist))

iPlotList = []
dimstr = ''
if '2D' in outDir: ## outdated, not used yet in BtoTW
        dimstr = '2D'
        templist = list(itertools.combinations(plotList,2))
        for item in templist:
                if 'NJetsAK8' not in item[0] and 'NJetsAK8' not in item[1]: continue
                iPlotList.append('X'+item[0]+'Y'+item[1])
else:
        iPlotList = plotList
        
print('Dimensions:',dimstr)
print('iPlotList:',iPlotList)

count=0
mem=2000
if categorize: mem=4000

for iplot in iPlotList:
	for cat in list(itertools.product(isEMlist,taglist)):
		catDir = cat[0]+'_'+cat[1]	
		outDir = outputDir+pfix+'/'+catDir
		if not os.path.exists(outDir): os.system('mkdir '+outDir)
		os.chdir(outDir)			

		dict={'rundir':runDir, 'dir':'.','iPlot':iplot,'region':region,'isCategorized':categorize,'memory':mem,
			  'isEM':cat[0],'tag':cat[1],'2D':dimstr,'procs':procs}
		print(dict)
		jdf=open('condor.job','w')
		jdf.write(
			"""use_x509userproxy = true
universe = vanilla
Executable = ../doCondorHists%(2D)s.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
Transfer_Input_Files = ../analyze_RDF%(2D)s.py, ../samples.py, ../utils.py, ../doHists_rdf%(2D)s_%(procs)s.py
Output = condor_%(iPlot)s_%(procs)s.out
Error = condor_%(iPlot)s_%(procs)s.err
Log = condor_%(iPlot)s_%(procs)s.log
Notification = Never
Arguments = %(dir)s %(iPlot)s %(region)s %(isCategorized)s %(isEM)s %(tag)s %(procs)s


Queue 1"""%dict)
#request_memory = %(memory)s
		jdf.close()

		os.system('condor_submit condor.job')
		os.chdir('..')
		count+=1

print("Total jobs submitted:", count)
