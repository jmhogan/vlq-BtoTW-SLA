#!/usr/bin/python
from ROOT import TH1D,TTree,TFile,RDataFrame,TH1,EnableImplicitMT
from array import array
from numpy import linspace
from samples import targetlumi, lumiStr
import math,time

TH1.SetDefaultSumw2(True)
EnableImplicitMT()

"""
--This function will make kinematic plots for a given distribution for electron, muon channels and their combination
--Check the cuts below to make sure those are the desired full set of cuts!
--The applied weights are defined in "weights.py". Also, the additional weights (SFs, 
negative MC weights, ets) applied below should be checked!
"""

def analyze(tTree,sample,doAllSys,iPlot,plotDetails,category,region,isCategorized, outHistFile):
        start_time = time.time()
        plotTreeName=plotDetails[0]
        xbins=array('d', plotDetails[1])
        xAxisLabel=plotDetails[2]
        
	# Define categories
        isEM  = category['isEM']
        tag   = category['tag']
        catStr = 'is'+isEM+'_'+tag

        # Define weights
        weightStr = '1'

        print("*****"*20)
        print("PROCESSING:  "+sample.prefix)

	# Design the EM cuts for categories -- THIS WILL BE THE FIRST CUT
        isEMCut=''
        if isEM=='E': 
                isEMCut+='isEl==1'
        elif isEM=='M': 
                isEMCut+='isMu==1'
        elif isEM=='L': 
                isEMCut+='(isMu==1 || isEl==1)'
        if 'SingleMuon' in sample.prefix: # don't let data double count
                isEMCut+=' && isMu==1'
        elif 'SingleElec' in sample.prefix:
                isEMCut+=' && isEl==1'
		
	# Define cuts by region. Use region "all" for all selected events
        cut  = ' && W_MT < 200' # TODO: 160 or 200
        #if 'lowMT' in region:
        #        cut += ' && W_MT < 160'
        if region == 'isoVT':
                cut += ' && lepton_miniIso < 0.05'
        if '1pb' in region: 
                cut += ' && NJets_DeepFlavL > 0'
        elif '2pb' in region: 
                cut += ' && NJets_DeepFlavL > 1'
        elif '0b' in region: 
                cut += ' && NJets_DeepFlavL == 0'
        if region == 'BAX': 
                cut += ' && NJets_forward == 0'                
        elif region == 'DCY': 
                cut += ' && NJets_forward > 0'
        elif region == 'B': 
                cut += ' && NJets_forward == 0 && NJets_DeepFlavL < 3'
        elif region == 'A': 
                cut += ' && NJets_forward == 0 && NJets_DeepFlavL == 3'
        elif region == 'X': 
                cut += ' && NJets_forward == 0 && NJets_DeepFlavL > 3'
        elif region == 'D': 
                cut += ' && NJets_forward > 0 && NJets_DeepFlavL < 3'
        elif region == 'C': 
                cut += ' && NJets_forward > 0 && NJets_DeepFlavL == 3'
        elif region == 'Y': 
                cut += ' && NJets_forward > 0 && NJets_DeepFlavL > 3'

        # Separate ttbar into mass bins for proper normalization 
        if 'TTTo' in sample.prefix:
                if sample.prefix[-4:] == "1000": 
                        cut += ' && genttbarMass > 1000'
                elif sample.prefix[-3:] == "700": 
                        cut += ' && genttbarMass > 700 && genttbarMass <= 1000'
                elif sample.prefix[-1] == "0": 
                        cut += ' && genttbarMass <= 700'

	# Design the tagging cuts for categories
        tagCut = ''
        if isCategorized:
                if tag == 'tagTjet': 
                        tagCut += ' && Bdecay_obs == 1'
                elif tag == 'tagWjet': 
                        tagCut += ' && Bdecay_obs == 2'
                elif tag == 'untagTlep': 
                        tagCut += ' && Bdecay_obs == 3'
                elif tag == 'untagWlep': 
                        tagCut += ' && Bdecay_obs == 4'
                elif tag == 'allWlep': 
                        tagCut += ' && (Bdecay_obs == 4 || Bdecay_obs == 1)'
                elif tag == 'allTlep': 
                        tagCut += ' && (Bdecay_obs == 2 || Bdecay_obs == 3)'

		# signal categories for basic tag counts

                if '2pW' in tag: 
                        tagCut += ' && gcFatJet_nW >= 2'
                elif '2W' in tag: 
                        tagCut += ' && gcFatJet_nW == 2'
                elif '1pW' in tag: 
                        tagCut += ' && gcFatJet_nW >= 1'
                elif '1W' in tag: 
                        tagCut += ' && gcFatJet_nW == 1'
                elif '01W' in tag: 
                        tagCut += ' && gcFatJet_nW <= 1'
                elif '0W' in tag: 
                        tagCut += ' && gcFatJet_nW == 0'		
                if '0T' in tag: 
                        tagCut += ' && gcFatJet_nT == 0'
                elif '01T' in tag: 
                        tagCut += ' && gcFatJet_nT <= 1'
                elif '1T' in tag: 
                        tagCut += ' && gcFatJet_nT == 1'
                elif '1pT' in tag: 
                        tagCut += ' && gcFatJet_nT >= 1'
                elif '2T' in tag: 
                        tagCut += ' && gcFatJet_nT == 2'
                elif '2pT' in tag: 
                        tagCut += ' && gcFatJet_nT >= 2'
	       	

        fullcut = isEMCut+cut+tagCut

        print('plotTreeName: '+plotTreeName)
        print('Flavour: '+isEM+', tag: '+tag)
        #print("Weights: "+weightStr)
        print('Cuts: '+fullcut)

        # Declare histograms --- COMMENTS FOR UNCERTAINTIES NOT BEING RUN YET
        process = sample.prefix
        df = RDataFrame(tTree[process])

        try:
                sel = df.Filter(fullcut).Define('weight',weightStr)
        except:
                print("No dataframe built!!")

        hist = sel.Histo1D((f'{iPlot}_{lumiStr}_{catStr}_{process}',xAxisLabel,len(xbins)-1,xbins),plotTreeName, 'weight')
        hist.Write()

        print("--- Analyze: %s minutes ---" % (round((time.time() - start_time)/60,2)))
