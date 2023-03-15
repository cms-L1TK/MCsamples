
#######################################################################
# Make _cfi.py files, each corresponding to one of the datasets       #
# in the CMSSW_12_6_0_pre4 RelVal samples used by L1TrkAlgo.          #
#                                                                     #
# The list of these datasets is hard-coded below, as is the name of   #
# the directory dirName to which they will be written.                #
# The directory will be created if not yet existing.                  #
#                                                                     #
# Run from linux with:                                                #
#   python getMC_12_6_0_D88.py                                        #
#                                                                     #
# N.B. You must have a valid GRID proxy to use this script            #
#      and must have done cmsenv !                                    #
#######################################################################

from makeDataCfiFiles import *
import os

if (not os.path.exists("getCMSdata_cfi.py")):
    print("ERROR: You must run this script from the directory containing it!")
    exit(1)

# Name of output directory (will be created if not existing)
dirName = "../../RelVal_1260_D88/python/"

# Names of datasets to be processed.
dataList = [
# D88 geometry
'/RelValTTbar_14TeV/CMSSW_12_6_0_pre4-125X_mcRun4_realistic_v2_2026D88noPU-v1/GEN-SIM-DIGI-RAW',
'/RelValTTbar_14TeV/CMSSW_12_6_0-PU_125X_mcRun4_realistic_v5_2026D88PU140RV183v2-v1/GEN-SIM-DIGI-RAW',
'/RelValTTbar_14TeV/CMSSW_12_6_0-PU_125X_mcRun4_realistic_v5_2026D88PU200RV183v2-v1/GEN-SIM-DIGI-RAW',
'/RelValSingleElPt2p0to100p0/CMSSW_12_6_0-125X_mcRun4_realistic_v5_2026D88noPURV183-v1/GEN-SIM-DIGI-RAW',
'/RelValSingleElPt1p5to8p0/CMSSW_12_6_0-125X_mcRun4_realistic_v5_2026D88noPURV183-v1/GEN-SIM-DIGI-RAW',
'/RelValSingleMuPt2p0to100p0/CMSSW_12_6_0-125X_mcRun4_realistic_v5_2026D88noPURV183-v1/GEN-SIM-DIGI-RAW',
'/RelValSingleMuPt1p5to8p0/CMSSW_12_6_0-125X_mcRun4_realistic_v5_2026D88noPURV183-v1/GEN-SIM-DIGI-RAW',
'/RelValSingleMuDisplacedPt2p0to100p0/CMSSW_12_6_0-125X_mcRun4_realistic_v5_2026D88noPURV183-v1/GEN-SIM-DIGI-RAW',
'/RelValSingleMuDisplacedPt1p5to8p0/CMSSW_12_6_0-125X_mcRun4_realistic_v5_2026D88noPURV183-v1/GEN-SIM-DIGI-RAW'
]

makeDataCfiFiles(dirName, dataList);
