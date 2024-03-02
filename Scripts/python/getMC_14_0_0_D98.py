
#######################################################################
# Make _cfi.py files, each corresponding to one of the datasets       #
# in the CMSSW_14_0_0_pre2 RelVal samples used by L1TrkAlgo.          #
#                                                                     #
# The list of these datasets is hard-coded below, as is the name of   #
# the directory dirName to which they will be written.                #
# The directory will be created if not yet existing.                  #
#                                                                     #
# Run from linux with:                                                #
#   python getMC_14_0_0_D98.py                                        #
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
dirName = "../../RelVal_1400_D98/python/"

# Names of datasets to be processed.
dataList = [
# D98 geometry
'/RelValTTbar_14TeV/CMSSW_14_0_0_pre2-133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/GEN-SIM-DIGI-RAW',
'/RelValTTbar_14TeV/CMSSW_14_0_0_pre2-PU_133X_mcRun4_realistic_v1_STD_2026D98_PU140_RV229-v1/GEN-SIM-DIGI-RAW',		'/RelValTTbar_14TeV/CMSSW_14_0_0_pre2-PU_133X_mcRun4_realistic_v1_STD_2026D98_PU200_RV229-v1/GEN-SIM-DIGI-RAW',	'/RelValSingleEFlatPt2To100/CMSSW_14_0_0_pre2-133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/GEN-SIM-DIGI-RAW',
'/RelValSingleEFlatPt1p5To8/CMSSW_14_0_0_pre2-133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/GEN-SIM-DIGI-RAW',	'/RelValSingleMuFlatPt2To100/CMSSW_14_0_0_pre2-133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/GEN-SIM-DIGI-RAW',	'/RelValSingleMuFlatPt1p5To8/CMSSW_14_0_0_pre2-133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/GEN-SIM-DIGI-RAW',
'/RelValDisplacedSingleMuFlatPt2To100/CMSSW_14_0_0_pre2-133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/GEN-SIM-DIGI-RAW',	'/RelValDisplacedSingleMuFlatPt1p5To8/CMSSW_14_0_0_pre2-133X_mcRun4_realistic_v1_STD_2026D98_noPU_RV229-v1/GEN-SIM-DIGI-RAW'
]

makeDataCfiFiles(dirName, dataList);
