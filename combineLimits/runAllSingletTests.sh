#!/bin/bash

# echo "--------------- Working on VR for TT -------------------"

dir=limits_templatesABCDnn_V_Oct2024
mass=1200

echo "Creating initial fit workspace:" 
python -u runInitialFit.py $dir $mass 0 500 

echo "Running nuisance plot: CHECK LINES 382 and 411 FOR RANGES"
python -u diffNuisances.py -g $dir/$BR/cmb/$mass/nuisancepulls.root $dir/$BR/cmb/$mass/fitDiagnostics.root >& $dir/$BR/cmb/$mass/nuisancepulls.txt

echo "Running covariance plot: CHECK LINES 23/24 and 48/49 FOR RANGES"
python -u covariancePlotter.py $dir $mass

# Not included in Kuan-Yu's list
#echo "Submitting toys to condor for R = 0:"
#python -u runCondorToys.py inject $dir $mass 0 500 

echo "Submitting toys to condor for GOF:"
python -u runCondorToys.py gof $dir $mass 500

########### STOP HERE! WAIT FOR CONDOR TO FINISH!! ##############

# echo "Plotting R = 0 injection results:"
# python -u signalInjectionPlotter.py $dir $mass 0

# echo "Plotting GOF results:"
# python -u GoFPlotter.py $dir $mass

# echo "Done!"

# echo "--------------- Working on SR+CR for TT -------------------"

# dir=limits_templatesABCDnn_DV_Oct2024
# mass=1200

#echo "Creating initial fit workspace:"
#python -u runInitialFit.py $dir $mass 0 500 $BR   ## Mask D, unmask V. Then swap later...

#echo "Running impact test: (Note: might crash waiting for proxy password if piped to a log!)"
#python -u runImpacts.py $dir $mass crab $BR 

# echo "Submitting toys to condor for 1200 R = 0:"
# python -u runCondorToys.py inject $dir $mass $BR 0 500 

# echo "---- LIMIT-BASED TOYS (run limits and set values first!) ----"

# echo "Submitting toys to condor for 1200 R = exp0:"
# python -u runCondorToys.py inject $dir $mass $BR 2.72 500 

# mass=1800
# echo "Submitting toys to condor for 1800 R = 0:"
# python -u runCondorToys.py inject $dir $mass $BR 0.0 500 

# echo "Submitting toys to condor for 1800 R = exp0:"
# python -u runCondorToys.py inject $dir $mass $BR 2.29 500


######## STOP HERE! WAIT FOR CRAB/CONDOR TO FINISH! ##########

# echo "Running impact test json-maker:"
# python -u runImpacts.py $dir $mass json $BR

# python -u plotImpacts.py --input $dir/$BR/cmb/1400/impacts.json --output $dir/$BR/cmb/1400/impacts

# echo "Plotting all injection results:"
# mass=1200
# python -u signalInjectionPlotter.py $dir $mass $BR 0
# python -u signalInjectionPlotter.py $dir $mass $BR 2.72

# mass=1800
# python -u signalInjectionPlotter.py $dir $mass $BR 0
# python -u signalInjectionPlotter.py $dir $mass $BR 2.29


# echo "Done!"

