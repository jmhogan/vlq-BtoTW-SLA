#!/usr/bin/python

# python3 -u plotHists.py [iPlot='BpMassAve'] [region='all'] [isCategorized=False] [blind] [yLog=false]
# python3 -u plotHists.py VLQBMass

import os,sys,time,math
parent = os.path.dirname(os.getcwd())
sys.path.append(parent)
from ROOT import gROOT, TFile, kAzure, TColor, kMagenta, kOrange, kGreen, TGraphAsymmErrors, TH1, TTree, TH2, RDataFrame, TLegend, TCanvas, kBlack, TGraphAsymmErrors, TGraph, TPad, TStyle, THStack, gStyle, TLatex, SetOwnership
from samples import lumiStr, systListShortPlots, systListFullPlots, xsec
from utils import poissonErrors

gROOT.SetBatch(1)
start_time = time.time()

lumi=61.9 #for plots #56.1 #
lumiInTemplates= lumiStr

iPlot='BpMassAve'
if len(sys.argv)>1: iPlot=str(sys.argv[1])
region='3lep'
if len(sys.argv)>2: region=str(sys.argv[2])
isCategorized=False
if len(sys.argv)>3: isCategorized=bool(eval(sys.argv[3]))
if isCategorized:
        pfix=f'templates{region}'
else:
        pfix=f'kinematics{region}'      #'TEST' is TEMP
if len(sys.argv)>4:
        pfix+=str(sys.argv[4])
else:
        pfix='kinematics3lep'    # TEMP
templateDir = f'{os.getcwd()}/{pfix}/'

year = 'all'
if len(sys.argv)>8: year=sys.argv[8]

print('Plotting',region,'is categorized?',isCategorized,' for year',year)

if len(sys.argv)>7:
        isRebinned=str(sys.argv[7])
else:
        isRebinned=''
        
saveKey = '' # tag for plot names

datalabel = 'data_obs'
shiftlist = ['Up','Down'] # change to Down for future
sig1='BpM700' #  choose the 1st signal to plot
sig1leg='B#bar{B} (0.7 TeV, 1 pb)'
sig2='BpM1300' #  choose the 2nd signal to plot
sig2leg='B#bar{B} (1.3 TeV, 1 pb)'


scaleSignals = True
#if not isCategorized: scaleSignals = True
sigScaleFact = 0.2
if region == '4lep':
        sigScaleFact = 0.01
print('Scaling signals?',scaleSignals)
print('Scale factor = ',sigScaleFact)
tempsig='templates_'+iPlot+'_'+lumiInTemplates+''+isRebinned+'.root'#+'_Data18.root'
if year != 'all': tempsig='templates_'+iPlot+'_'+lumiInTemplates+'_'+year+''+isRebinned+'.root'#+'_Data18.root'

plotLowSide = True

bkgProcList = [#'qcd',
        'np',
        'ttx',
        'conv',
        'ewk',
        #'higgs',
        #'wjets',                       
        #'singletop',
        #'ttbar'
]
bkgHistColors = {'np':TColor.GetColor("#5790FC"),'ttx':TColor.GetColor("#F89C20"),'conv':TColor.GetColor("#E42536"),'ewk':TColor.GetColor("#964A8B"),'higgs':TColor.GetColor("9C9CA1")}
#'ttbar':kAzure+8,'wjets':kMagenta-2,'qcd':kOrange-3,'singletop':kGreen-6,

doAllSys = False

doNormByBinWidth=False
if len(isRebinned)>0 and 'stat1p1' not in isRebinned and 'mvagof' not in isRebinned: doNormByBinWidth = True

doOneBand = True
if not doAllSys: doOneBand = True # Don't change this!
doRealPull = False
if doRealPull: doOneBand=False

plotNorm = False

blind = False
if len(sys.argv)>5: blind=bool(eval(sys.argv[5]))

yLog  = False
if len(sys.argv)>6: yLog=bool(eval(sys.argv[6]))
print('Plotting blind?',blind,' yLog?',yLog)
if yLog or region == 'V' or 'validation' in pfix: scaleSignals = False

partialBlind = False

isEMlist =['L']#'E','M']
taglist = ['all']
if isCategorized == True:
        print('IMPLEMENT CATEGORIES IN PLOTHISTS!')
        exit(1)
else:
        if (region == '3lep' or region == '4lep') and ('Mass' in iPlot or 'JetPt' in iPlot or 'HT' in iPlot or 'ST' in iPlot):
                partialBlind = True

lumiSys = 0.018 # lumi uncertainty

#### Consider: Did not set removeThreshold
####           No doPDF

def getNormUnc(hist,ibin,modelingUnc):
        contentsquared = hist.GetBinContent(ibin)**2
        error = lumiSys*lumiSys*contentsquared  #might be others in future
        return error

def formatUpperHist(histogram,th1hist):
        histogram.GetXaxis().SetLabelSize(0)
        if plotLowSide:
                lowside = th1hist.GetBinLowEdge(1)
        else:
                lowside =  400 #TEMP: plotting only high BpM for ABCDnn
        highside = th1hist.GetBinLowEdge(th1hist.GetNbinsX()+1)
        histogram.GetXaxis().SetRangeUser(lowside,highside)
        histogram.GetXaxis().SetNdivisions(506)
                
        #if 'BpMass' in histogram.GetName():
        #        histogram.GetYaxis().SetTitleOffset(1.0)

        if blind == True:
                histogram.GetXaxis().SetLabelSize(0.045)
                histogram.GetXaxis().SetTitleSize(0.055)
                histogram.GetYaxis().SetLabelSize(0.04)
                histogram.GetYaxis().SetTitleSize(0.05)
                histogram.GetYaxis().SetTitleOffset(1.1)
                if 'YLD' in iPlot: histogram.GetXaxis().LabelsOption("u")
        else:
                histogram.GetYaxis().SetLabelSize(0.05)
                histogram.GetYaxis().SetTitleSize(0.06)
                histogram.GetYaxis().SetTitleOffset(1.1) #used to be 0.82. overlaps with label

        histogram.GetYaxis().CenterTitle()
        if plotNorm:
                if yLog: uPad.SetLogy()
                histogram.SetMaximum(1.0)
        else:
                if not yLog: 
                        if region == 'SR' and isCategorized:
                                histogram.SetMinimum(0.000101);
                        else: 
                                histogram.SetMinimum(0.25)		

                if yLog:
                        uPad.SetLogy()
                        if not doNormByBinWidth:
                                histogram.SetMaximum(200*histogram.GetMaximum())
                        else: 
                                histogram.SetMaximum(200*histogram.GetMaximum())
                        if iPlot=='YLD': 
                                histogram.SetMaximum(200*histogram.GetMaximum())
                                histogram.SetMinimum(0.1)

def formatLowerHist(histogram):
        histogram.GetXaxis().SetLabelSize(.15)
        histogram.GetXaxis().SetTitleSize(0.18)
        histogram.GetXaxis().SetTitleOffset(0.95)
        histogram.GetXaxis().SetNdivisions(506)
        #histogram.GetXaxis().SetTitle('Avg(B,#bar{B}) Delta #phi')     # TEST: SET X-AXIS LABEL
        if 'YLD' in iPlot: histogram.GetXaxis().LabelsOption("u")

        histogram.GetYaxis().SetLabelSize(0.15)
        histogram.GetYaxis().SetTitleSize(0.145)
        histogram.GetYaxis().SetTitleOffset(0.3)
        if not doRealPull: 
                histogram.GetYaxis().SetTitle('Data/Bkg')
        else: 
                histogram.GetYaxis().SetTitle('#frac{(data-bkg)}{std. dev.}')
        histogram.GetYaxis().SetNdivisions(7)
        if doRealPull: 
                histogram.GetYaxis().SetRangeUser(-2.99,2.99)
        elif yLog and doNormByBinWidth:
                histogram.GetYaxis().SetRangeUser(0.1,1.9)
        else: 
                histogram.GetYaxis().SetRangeUser(0.1,3.9)
        histogram.GetYaxis().CenterTitle()
        if not plotLowSide:
                lowside =  400 #TEMP
                highside = histogram.GetBinLowEdge(histogram.GetNbinsX()+1) #TEMP
                histogram.GetXaxis().SetRangeUser(lowside,highside) #TEMP

                
print(templateDir+tempsig)
RFile1 = TFile(templateDir+tempsig)
print(templateDir+tempsig)
print(RFile1)
bkghists = {}
bkghistsmerged = {}
systHists = {}
totBkgTemp1 = {}
totBkgTemp2 = {}
totBkgTemp3 = {}
for tag in taglist:
        perNGeV = 50 # Setting goes with "doNormByBinWidth". Choose what "unit" to use for bin widths, similar to the smaller bin widths in the plot. Values < 1 are ok for e.g. NN scores
        print('------------------ ',tag,' with perNGeV = ',perNGeV,' -----------------------')

        tagStr=tag
        for isEM in isEMlist:
                histPrefix=iPlot+'_'+lumiInTemplates+'_'
                catStr='is'+isEM+'_'+tagStr
                histPrefix+=catStr
                if isCategorized: histPrefix+='_'+region
                totBkg = 0.
                totMajor = 0.
                totMinor = 0.
                for proc in bkgProcList: 
                        try:
                                bkghists[proc+catStr] = RFile1.Get(histPrefix+'__'+proc).Clone()
                        except:
                                print("There is no "+proc+"!!!!!!!!")
                                print("tried to open "+histPrefix+'__'+proc)
                                pass

                if plotNorm:
                        for proc in bkgProcList:
                                bkghists[proc+catStr].Scale(1/totBkg)
                        totBkg = 1.0

                hData = RFile1.Get(histPrefix+'__'+datalabel).Clone()
                print('Data:',hData.Integral())
                if plotNorm:
                        hData.Scale(1/hData.Integral())

                for proc in bkgProcList:
                        try:
                                totBkg += bkghists[proc+catStr].Integral()
                        except:
                                print('cant add',proc)
                                pass

                if partialBlind: # Todo: generalize it for other branches
                        start_bin = hData.GetNbinsX()+1
                        if iPlot == 'BpMassAve':
                                start_bin = hData.GetXaxis().FindFixBin(200)+1
                        elif iPlot == 'VLQMassAve':
                                start_bin = hData.GetXaxis().FindFixBin(400)+1
                        elif iPlot == 'JetPt':
                                start_bin = hData.GetXaxis().FindFixBin(100)+1
                        elif iPlot == 'HT':
                                start_bin = hData.GetXaxis().FindFixBin(400)+1
                        end_bin = hData.GetNbinsX()+1
                        for b in range(start_bin, end_bin):
                                hData.SetBinContent(b, 0)
                                hData.SetBinError(b, 0)

                gaeData = TGraphAsymmErrors(hData.Clone(hData.GetName().replace(datalabel,'gaeDATA')))
                hsig1 = RFile1.Get(histPrefix+'__'+sig1).Clone(histPrefix+'__sig1')
                hsig2 = RFile1.Get(histPrefix+'__'+sig2).Clone(histPrefix+'__sig2')
               
                if plotNorm:
                        hsig1.Scale(1/hsig1.Integral())
                        hsig2.Scale(1/hsig2.Integral())
                if isCategorized:
                        hsig1.Scale(xsec[sig1[3:]])
                        hsig2.Scale(xsec[sig2[3:]])
                #if len(isRebinned) > 0: ## FIXME later
                #        hsig1.Scale(10) # 100fb input -> 1pb
                #        hsig2.Scale(10)
                if doNormByBinWidth:
                        poissonNormByBinWidth(gaeData,hData,perNGeV)
                        for proc in bkgProcList:
                                try:
                                        print('normByBinWidth: '+proc)
                                        normByBinWidth(bkghists[proc+catStr],perNGeV)
                                except: pass
                        normByBinWidth(hsig1,perNGeV)
                        normByBinWidth(hsig2,perNGeV)
                        normByBinWidth(hData,perNGeV)
                else: poissonErrors(gaeData)
                # Yes, there are easier ways using the TH1's but
                # it would be rough to swap objects lower down

                bkgHT = bkghists[bkgProcList[0]+catStr].Clone()
                for proc in bkgProcList:
                        if proc==bkgProcList[0]: continue
                        try: 
                                bkgHT.Add(bkghists[proc+catStr])
                        except: pass
                gaeBkgHT = TGraphAsymmErrors(bkgHT.Clone("gaeBkgHT"))

                #yvals = gaeBkgHT.GetY()
                #print('bkgHT = ',bkgHT.GetBinContent(25),'+/-',bkgHT.GetBinError(25))
                #print('gaeBkgHT = ',yvals[24],'+',gaeBkgHT.GetErrorYhigh(24),'-',gaeBkgHT.GetErrorYlow(24))

                if doAllSys:
                        for proc in bkgProcList:
                                if isCategorized:
                                        systematicList = systListFullPlots.copy()
                                        if isRebinned: #TEMP: update this later
                                                try:
                                                        systematicList.remove('muR')
                                                        systematicList.remove('muF')
                                                        systematicList.remove('muRFcorrd')
                                                        systematicList.append('muRFcorrdNewQCD')
                                                        systematicList.append('muRFcorrdNewEWK')
                                                        systematicList.append('muRFcorrdNewST')
                                                        systematicList.append('muRFcorrdNewTTX')
                                                        systematicList.append('muRFcorrdNewTT')
                                                        systematicList.append('muRFcorrdNewWJT')
                                                        systematicList.append('pdfNew')
                                                except:
                                                        print("Unable to remove muR, muF, muRFcorrd and append New")
                                        else: # proxy rebinned by plotting only muRFcorrd
                                                try:
                                                        systematicList.remove('muR')
                                                        systematicList.remove('muF')
                                                except:
                                                        pass
                                else:
                                        systematicList = systListShortPlots
                                for syst in systematicList:
                                        for ud in shiftlist:
                                                try:
                                                        systHists[proc+catStr+syst+ud] = RFile1.Get(f'{histPrefix}__{proc}__{syst}{ud}').Clone()
                                                        if doNormByBinWidth: 
                                                                normByBinWidth(systHists[proc+catStr+syst+ud],perNGeV)
                                                except:
                                                        print(f'FAILED to open {histPrefix}__{proc}__{syst}{ud}')
                                                        pass

                totBkgTemp1[catStr] = TGraphAsymmErrors(bkgHT.Clone(bkgHT.GetName()+'shapeOnly'))
                totBkgTemp2[catStr] = TGraphAsymmErrors(bkgHT.Clone(bkgHT.GetName()+'shapePlusNorm'))
                totBkgTemp3[catStr] = TGraphAsymmErrors(bkgHT.Clone(bkgHT.GetName()+'All'))

                for ibin in range(1,bkghists[bkgProcList[0]+catStr].GetNbinsX()+1):
                        #print('--------------- bin',ibin,'--------------')
                        errorUp = 0.
                        errorDn = 0.
                        errorStatUp = gaeBkgHT.GetErrorYhigh(ibin-1)**2
                        errorStatDn = gaeBkgHT.GetErrorYlow(ibin-1)**2
                        errorNorm = (lumiSys**2)*(bkgHT.GetBinContent(ibin)**2)
                        if doAllSys:
                                for syst in systematicList:
                                        for proc in bkgProcList:
                                                try:
                                                        #if ibin == 1:
                                                        #        print('for',syst,'in',proc,'found central bin',bkghists[proc+catStr].GetBinContent(ibin),'and up bin',systHists[proc+catStr+syst+shiftlist[0]].GetBinContent(ibin),'and down bin',systHists[proc+catStr+syst+shiftlist[1]].GetBinContent(ibin))
                                                        errorPlus = systHists[proc+catStr+syst+shiftlist[0]].GetBinContent(ibin)-bkghists[proc+catStr].GetBinContent(ibin)
                                                        errorMinus = bkghists[proc+catStr].GetBinContent(ibin)-systHists[proc+catStr+syst+shiftlist[1]].GetBinContent(ibin)
                                                        #if ibin == 1:
                                                        #        print('for',syst,'in',proc,'found errorPlus =',errorPlus,'and errorMinus =',errorMinus)
                                                        if errorPlus > 0:
                                                                errorUp += errorPlus**2
                                                        else: 
                                                                errorDn += errorPlus**2
                                                        if errorMinus > 0: 
                                                                errorDn += errorMinus**2
                                                        else: 
                                                                errorUp += errorMinus**2
                                                except: pass

                        totBkgTemp1[catStr].SetPointEYhigh(ibin-1,math.sqrt(errorUp))
                        totBkgTemp1[catStr].SetPointEYlow(ibin-1, math.sqrt(errorDn))
                        totBkgTemp2[catStr].SetPointEYhigh(ibin-1,math.sqrt(errorUp+errorNorm))
                        totBkgTemp2[catStr].SetPointEYlow(ibin-1, math.sqrt(errorDn+errorNorm))
                        totBkgTemp3[catStr].SetPointEYhigh(ibin-1,math.sqrt(errorUp+errorNorm+errorStatUp))
                        totBkgTemp3[catStr].SetPointEYlow(ibin-1, math.sqrt(errorDn+errorNorm+errorStatDn))

                bkgHTgerr = totBkgTemp3[catStr].Clone()

                scaleFact1 = int(bkgHT.GetMaximum()/hsig1.GetMaximum()) - int(bkgHT.GetMaximum()/hsig1.GetMaximum()) % 10
                scaleFact2 = int(bkgHT.GetMaximum()/hsig2.GetMaximum()) - int(bkgHT.GetMaximum()/hsig2.GetMaximum()) % 10
                if scaleFact1==0: scaleFact1=int(bkgHT.GetMaximum()/hsig1.GetMaximum())
                if scaleFact2==0: scaleFact2=int(bkgHT.GetMaximum()/hsig2.GetMaximum())
                if scaleFact1==0: scaleFact1=1
                if scaleFact2==0: scaleFact2=1
                if sigScaleFact>0:
                        scaleFact1=sigScaleFact
                        scaleFact2=sigScaleFact
                if not scaleSignals:
                        scaleFact1=1
                        scaleFact2=1
                hsig1.Scale(scaleFact1)
                hsig2.Scale(scaleFact2)

                ############################################################
                ############## Making Plots of e+jets, mu+jets and e/mu+jets 
                ############################################################

                stackbkgHT = THStack("stackbkgHT","")
                for proc in bkgProcList:
                        stackbkgHT.Add(bkghists[proc+catStr])

                sig1Color= kBlack
                sig2Color= kBlack

                for proc in bkgProcList:
                        bkghists[proc+catStr].SetLineColor(bkgHistColors[proc])
                        bkghists[proc+catStr].SetFillColor(bkgHistColors[proc])
                        bkghists[proc+catStr].SetLineWidth(2)
                hsig1.SetLineColor(sig1Color)
                hsig1.SetFillStyle(0)
                hsig1.SetLineWidth(3)
                hsig2.SetLineColor(sig2Color)
                hsig2.SetLineStyle(7)#5)
                hsig2.SetFillStyle(0)
                hsig2.SetLineWidth(3)

                gaeData.SetMarkerStyle(20)
                gaeData.SetMarkerSize(1.2)
                gaeData.SetLineWidth(2)
                gaeData.SetMarkerColor(kBlack)
                gaeData.SetLineColor(kBlack)

                bkgHTgerr.SetFillStyle(3004)
                bkgHTgerr.SetFillColor(kBlack)

                gStyle.SetOptStat(0)
                c1 = TCanvas("c1","c1",1200,1000) # used to be 1200 and 1000, but the y-axis labels might overlap
                gStyle.SetErrorX(0.5)
                yDiv=0.25
                if blind == True: yDiv=0.01
                # for some reason the markers at 0 don't show with this setting:
                uMargin = 0.00001
                if blind == True: uMargin = 0.12
                rMargin=.04
                # overlap the pads a little to hide the error bar gap:
                uPad={}
                if yLog and not blind: 
                        uPad=TPad("uPad","",0,yDiv-0.009,1,1) #for actual plots
                else: 
                        uPad=TPad("uPad","",0,yDiv,1,1) #for actual plots
                uPad.SetTopMargin(0.08)
                uPad.SetBottomMargin(uMargin)
                uPad.SetRightMargin(rMargin)
                uPad.SetLeftMargin(0.15) #used to be 0.105. y axis label overlaps with title
                uPad.Draw()
                if blind == False:
                        lPad=TPad("lPad","",0,0,1,yDiv) #for sigma runner
                        lPad.SetTopMargin(0)
                        lPad.SetBottomMargin(.4)
                        lPad.SetRightMargin(rMargin)
                        lPad.SetLeftMargin(0.15) #used to be 0.105. y axis label overlaps with title
                        lPad.SetGridy()
                        lPad.Draw()
                if not doNormByBinWidth: hData.SetMaximum(1.1*max(hData.GetMaximum(),bkgHT.GetMaximum()))
                hData.SetMinimum(0.015)
                hData.SetTitle("")
                # this is super important now!! gaeData has badly defined (negative) maximum
                gaeData.SetMaximum(1.1*max(hData.GetMaximum(),bkgHT.GetMaximum()))
                #gaeData.SetMaximum(65)     # Manual Set Upper Bound of y-axis on plot
                if 'Charge' in iPlot or iPlot == 'Nleps' or iPlot == 'lepID':
                        gaeData.SetMaximum(1.5*max(hData.GetMaximum(),bkgHT.GetMaximum()))
                gaeData.SetMinimum(0.015)
                gaeData.SetTitle("")
                if doNormByBinWidth:
                        if perNGeV <= 1:
                                gaeData.GetYaxis().SetTitle("< Events / "+str(perNGeV)+" >")
                        else: 
                                gaeData.GetYaxis().SetTitle("< Events / "+str(perNGeV)+" GeV >")
                else: gaeData.GetYaxis().SetTitle("Events / bin")
                formatUpperHist(gaeData,hData)
                uPad.cd()
                gaeData.SetTitle("")
                if not blind:
                        gaeData.Draw("apz")
                if blind: 
                        hsig1.SetMinimum(0.015)
                        if doNormByBinWidth:
                                if perNGeV <= 1: 
                                        hsig1.GetYaxis().SetTitle("< Events / "+str(perNGeV)+" >")
                                else: hsig1.GetYaxis().SetTitle("< Events / "+str(perNGeV)+" GeV >")
                        else: hsig1.GetYaxis().SetTitle("Events / bin")
                        hsig1.SetMaximum(1.5*hData.GetMaximum())
                        formatUpperHist(hsig1,hsig1)
                        hsig1.Draw("HIST")
                if doNormByBinWidth:
                        if iPlot == 'DnnTprime' or (iPlot == 'HTNtag' and perNGeV < 10): 
                                hData.GetYaxis().SetTitle("< Events / "+str(perNGeV)+" >")
                        else: 
                                hData.GetYaxis().SetTitle("< Events / "+str(perNGeV)+" GeV >")
                else: hData.GetYaxis().SetTitle("Events / bin")

                stackbkgHT.Draw("SAME HIST")
                hsig1.Draw("SAME HIST")
                hsig2.Draw("SAME HIST")
                if not blind: gaeData.Draw("PZ") #redraw data so its not hidden
                uPad.RedrawAxis()
                bkgHTgerr.Draw("SAME E2")

                chLatex = TLatex()
                chLatex.SetNDC()
                chLatex.SetTextSize(0.05)
                if blind: chLatex.SetTextSize(0.04)
                chLatex.SetTextAlign(21) # align center
                flvString = ''
                tagString = ''
                if isEM=='E': flvString+='e+jets'
                if isEM=='M': flvString+='#mu+jets'
                if isEM=='L':
                        flvString='#geq 3 e/#mu/#tau + 2 b-jets'
                        if region == '4lep':
                                flvString='#geq 4 e/#mu/#tau + 2 b-jets'
                        
                tagString = ''
                regionString = ''
                if isCategorized:
                        tagString = tag
                        regionString = 'region '+region
                if tagString.endswith(', '): tagString = tagString[:-2]		
                if not yLog:
                        chLatex.DrawLatex(0.7, 0.54, flvString)
                        chLatex.DrawLatex(0.7, 0.48, tagString)
                        chLatex.DrawLatex(0.7, 0.42, regionString)
                else:
                        chLatex.DrawLatex(0.3, 0.85, flvString)
                        chLatex.DrawLatex(0.3, 0.79, tagString)
                        chLatex.DrawLatex(0.3, 0.73, regionString)

                leg = TLegend(0.45,0.62,0.95,0.89)
                leg.SetShadowColor(0)
                leg.SetFillColor(0)
                leg.SetFillStyle(0)
                leg.SetLineColor(0)
                leg.SetLineStyle(0)
                leg.SetBorderSize(0) 
                leg.SetNColumns(2)
                
                leg.SetTextFont(62)#42)
                ## FIX ME LATER
                scaleFact1Str = ' x'+str(scaleFact1)
                scaleFact2Str = ' x'+str(scaleFact2)
                if not scaleSignals:
                        scaleFact1Str = ''
                        scaleFact2Str = ''
                if not blind:
                        leg.AddEntry(gaeData,"Data","pel")  #left
                        leg.AddEntry(bkghists['np'+catStr],"Nonprompt","f") #left
                        leg.AddEntry(hsig1,sig1leg+scaleFact1Str,"l")  #left
                        leg.AddEntry(bkghists['ttx'+catStr],"t#bar{t}+X","f") #right
                        leg.AddEntry(hsig2,sig2leg+scaleFact2Str,"l") #left
                        leg.AddEntry(bkghists['conv'+catStr],"Photon","f") #right
                        leg.AddEntry(bkgHTgerr,"Bkg. uncert.","f") #left
                        leg.AddEntry(bkghists['ewk'+catStr],"VV(V)","f") #right
                        #leg.AddEntry(0, "", "") #left
                else:
                        print('IMPLEMENT BLINDED LEGEND IN PLOTHISTS!')
                        exit(1)

                leg.Draw("same")

                prelimTex=TLatex()
                prelimTex.SetNDC()
                prelimTex.SetTextAlign(31) # align right
                prelimTex.SetTextFont(42)
                prelimTex.SetTextSize(0.05)
                if blind: prelimTex.SetTextSize(0.05)
                prelimTex.SetLineWidth(2)
                prelimTex.DrawLatex(0.95,0.94,str(lumi)+" fb^{-1} (13.6 TeV)")

                prelimTex2=TLatex()
                prelimTex2.SetNDC()
                prelimTex2.SetTextFont(61)
                prelimTex2.SetLineWidth(2)
                prelimTex2.SetTextSize(0.08)

                #if blind: prelimTex2.SetTextSize(0.08)
                #prelimTex2.DrawLatex(0.12,0.93,"CMS")


                prelimTex3=TLatex()
                prelimTex3.SetNDC()
                prelimTex3.SetTextAlign(11)

                #prelimTex3.SetTextFont(52)
                prelimTex3.SetTextFont(42)
                prelimTex3.SetTextSize(0.05)
                if blind: prelimTex3.SetTextSize(0.05)
                prelimTex3.SetLineWidth(2)
                # if not blind:
                #         prelimTex3.DrawLatex(0.23,0.945,"Private work (CMS data & simulation)") #"Preliminary")
                # if blind: 
                #         prelimTex3.DrawLatex(0.26,0.945,"Private work (CMS data & simulation)") #"Preliminary")
                prelimTex3.DrawLatex(0.16,0.94,"Private work (CMS data & simulation)") #"Preliminary")


                if blind == False and not doRealPull:
                        lPad.cd()
                        pull=hData.Clone(hData.GetName()+"pull")
                        pull.Divide(hData, bkgHT)
                        for binNo in range(0,hData.GetNbinsX()+2):
                                if bkgHT.GetBinContent(binNo)!=0:
                                        pull.SetBinError(binNo,hData.GetBinError(binNo)/bkgHT.GetBinContent(binNo))
                        pull.SetMaximum(3)
                        pull.SetMinimum(0)
                        pull.SetFillColor(1)
                        pull.SetLineColor(1)
                        pull.SetMarkerStyle(20)

                        formatLowerHist(pull)
                        pull.Draw("E0")

                        BkgOverBkg = pull.Clone("bkgOverbkg")
                        BkgOverBkg.Divide(bkgHT, bkgHT)
                        pullUncBandTot=TGraphAsymmErrors(BkgOverBkg.Clone("pulluncTot"))
                        for binNo in range(0,hData.GetNbinsX()+2):
                                if bkgHT.GetBinContent(binNo)!=0:
                                        pullUncBandTot.SetPointEYhigh(binNo-1,totBkgTemp3[catStr].GetErrorYhigh(binNo-1)/bkgHT.GetBinContent(binNo))
                                        pullUncBandTot.SetPointEYlow(binNo-1,totBkgTemp3[catStr].GetErrorYlow(binNo-1)/bkgHT.GetBinContent(binNo))			
                        if not doOneBand: 
                                pullUncBandTot.SetFillStyle(3001)
                        else: pullUncBandTot.SetFillStyle(3344)
                        pullUncBandTot.SetFillColor(1)
                        pullUncBandTot.SetLineColor(1)
                        pullUncBandTot.SetMarkerSize(0)
                        gStyle.SetHatchesLineWidth(1)
                        pullUncBandTot.Draw("SAME E2")

                        pullUncBandNorm=TGraphAsymmErrors(BkgOverBkg.Clone("pulluncNorm"))
                        for binNo in range(0,hData.GetNbinsX()+2):
                                if bkgHT.GetBinContent(binNo)!=0:
                                        pullUncBandNorm.SetPointEYhigh(binNo-1,totBkgTemp2[catStr].GetErrorYhigh(binNo-1)/bkgHT.GetBinContent(binNo))
                                        pullUncBandNorm.SetPointEYlow(binNo-1,totBkgTemp2[catStr].GetErrorYlow(binNo-1)/bkgHT.GetBinContent(binNo))			

                        pullUncBandNorm.SetFillStyle(3001)
                        pullUncBandNorm.SetFillColor(2)
                        pullUncBandNorm.SetLineColor(2)
                        pullUncBandNorm.SetMarkerSize(0)
                        gStyle.SetHatchesLineWidth(1)
                        if not doOneBand: pullUncBandNorm.Draw("SAME E2")

                        pullUncBandStat=TGraphAsymmErrors(BkgOverBkg.Clone("pulluncStat"))
                        for binNo in range(0,hData.GetNbinsX()+2):
                                if bkgHT.GetBinContent(binNo)!=0:
                                        pullUncBandStat.SetPointEYhigh(binNo-1,totBkgTemp1[catStr].GetErrorYhigh(binNo-1)/bkgHT.GetBinContent(binNo))
                                        pullUncBandStat.SetPointEYlow(binNo-1,totBkgTemp1[catStr].GetErrorYlow(binNo-1)/bkgHT.GetBinContent(binNo))			

                        pullUncBandStat.SetFillStyle(3001)
                        pullUncBandStat.SetFillColor(3)
                        pullUncBandStat.SetLineColor(3)
                        pullUncBandStat.SetMarkerSize(0)
                        gStyle.SetHatchesLineWidth(1)
                        if not doOneBand: pullUncBandStat.Draw("SAME E2")

                        pullLegend=TLegend(0.14,0.87,0.85,0.96)
                        SetOwnership( pullLegend, 0 )   # 0 = release (not keep), 1 = keep
                        pullLegend.SetShadowColor(0)
                        pullLegend.SetNColumns(3)
                        pullLegend.SetFillColor(0)
                        pullLegend.SetFillStyle(0)
                        pullLegend.SetLineColor(0)
                        pullLegend.SetLineStyle(0)
                        pullLegend.SetBorderSize(0)
                        pullLegend.SetTextFont(42)
                        if not doOneBand: 
                                pullLegend.AddEntry(pullUncBandStat , "Bkg. uncert. (shape syst.)" , "f")
                                pullLegend.AddEntry(pullUncBandNorm , "Bkg. uncert. (shape #oplus norm. syst.)" , "f")
                                pullLegend.AddEntry(pullUncBandTot , "Bkg. uncert. (stat. #oplus all syst.)" , "f")
                        else: 
                                if doAllSys: 
                                        pullLegend.AddEntry(pullUncBandTot , "Bkg. uncert. (stat. #oplus syst.)" , "f")
                                else: 
                                        pullLegend.AddEntry(pullUncBandTot , "Bkg. uncert. (stat. #oplus lumi)" , "f")
                        pullLegend.Draw("SAME")
                        pull.Draw("SAME E0")
                        lPad.RedrawAxis()

                if blind == False and doRealPull:
                        formatUpperHist(hData,hData)
                        lPad.cd()
                        pull=hData.Clone(hData.GetName()+"pull")
                        for binNo in range(1,hData.GetNbinsX()+1):
                                # case for data < MC:
                                dataerror = gaeData.GetErrorYhigh(binNo-1)
                                MCerror = totBkgTemp3[catStr].GetErrorYlow(binNo-1)
                                # case for data > MC: 
                                if(hData.GetBinContent(binNo) > bkgHT.GetBinContent(binNo)):
                                        dataerror = gaeData.GetErrorYlow(binNo-1)
                                        MCerror = totBkgTemp3[catStr].GetErrorYhigh(binNo-1)
                                pull.SetBinContent(binNo,(hData.GetBinContent(binNo)-bkgHT.GetBinContent(binNo))/math.sqrt(MCerror**2+dataerror**2))
                        pull.SetMaximum(3)
                        pull.SetMinimum(-3)
                        pull.SetFillColor(kGray+2)
                        pull.SetLineColor(kGray+2)
                        formatLowerHist(pull)
                        pull.Draw("HIST")

                #c1.Write()
                savePrefix = templateDir+templateDir.split('/')[-2]+'plots/'
                if not os.path.exists(savePrefix): os.system('mkdir '+savePrefix)
                savePrefix+=histPrefix+isRebinned.replace('_rebinned_stat1p1','')+saveKey
                if year != 'all': savePrefix=savePrefix.replace(lumiInTemplates,year)
                if doRealPull: savePrefix+='_pull'
                if doNormByBinWidth: savePrefix+='_NBBW'
                if yLog: savePrefix+='_logy'
                if blind: savePrefix+='_blind'

                if doOneBand:
                        if plotNorm:
                                c1.SaveAs(f"{savePrefix}totBand_norm.pdf")
                                c1.SaveAs(f"{savePrefix}totBand_norm.png")
                        else:
                                c1.SaveAs(f"{savePrefix}totBand.pdf")
                                c1.SaveAs(f"{savePrefix}totBand.png")
                                #c1.SaveAs(savePrefix+"totBand.eps")
                                #c1.SaveAs(savePrefix+"totBand.root")
                                #c1.SaveAs(savePrefix+"totBand.C")
                else:
                        if plotNorm:
                                c1.SaveAs(f"{savePrefix}_norm.pdf")
                                c1.SaveAs(f"{savePrefix}_norm.png")
                        else:
                                c1.SaveAs(f"{savePrefix}.pdf")
                                c1.SaveAs(f"{savePrefix}.png")
                                #c1.SaveAs(savePrefix+".eps")
                                #c1.SaveAs(savePrefix+".root")
                                #c1.SaveAs(savePrefix+".C")
                for proc in bkgProcList:
                        try: 
                                del bkghists[proc+catStr]
                        except: pass


RFile1.Close()

print("--- %s minutes ---" % (round(time.time() - start_time, 2)/60))
