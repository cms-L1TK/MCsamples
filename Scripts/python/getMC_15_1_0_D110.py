
#######################################################################
# Make _cfi.py files, each corresponding to one of the datasets       #
# in the CMSSW_15_1_0_pre5 RelVal samples used by L1TrkAlgo.          #
#                                                                     #
# The list of these datasets is hard-coded below, as is the name of   #
# the directory dirName to which they will be written.                #
# The directory will be created if not yet existing.                  #
#                                                                     #
# Run from linux with:                                                #
#   python3 getMC_15_1_0_D110.py                                      #
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
dirName = "../../RelVal_1510_D110/python/"

# Names of datasets to be processed.
dataList = [
  '/RelValTTbar_14TeV_TuneCP5/CMSSW_15_1_0_pre5-150X_mcRun4_realistic_v1_RV269_Run4D110_noPU-v1/GEN-SIM-DIGI-RAW',
  '/RelValDoubleEFlatPt1To100/CMSSW_15_1_0_pre5-150X_mcRun4_realistic_v1_RV269_Run4D110_noPU-v1/GEN-SIM-DIGI-RAW',
  '/RelValDoubleEFlatPt1p5To8/CMSSW_15_1_0_pre5-150X_mcRun4_realistic_v1_RV269_Run4D110_noPU-v1/GEN-SIM-DIGI-RAW',
  '/RelValDoubleMuFlatPt1To100/CMSSW_15_1_0_pre5-150X_mcRun4_realistic_v1_RV269_Run4D110_noPU-v1/GEN-SIM-DIGI-RAW',
  '/RelValDoubleMuFlatPt1p5To8/CMSSW_15_1_0_pre5-150X_mcRun4_realistic_v1_RV269_Run4D110_noPU-v1/GEN-SIM-DIGI-RAW',
  '/RelValDoubleEFlatPt1To100Dxy100GunProducer/CMSSW_15_1_0_pre5-150X_mcRun4_realistic_v1_RV269_Run4D110_noPU-v1/GEN-SIM-DIGI-RAW',
  '/RelValDoubleEFlatPt1p5To8Dxy100GunProducer/CMSSW_15_1_0_pre5-150X_mcRun4_realistic_v1_RV269_Run4D110_noPU-v1/GEN-SIM-DIGI-RAW',
  '/RelValDoubleMuFlatPt1To100Dxy100GunProducer/CMSSW_15_1_0_pre5-150X_mcRun4_realistic_v1_RV269_Run4D110_noPU-v1/GEN-SIM-DIGI-RAW',
  '/RelValDoubleMuFlatPt1p5To8Dxy100GunProducer/CMSSW_15_1_0_pre5-150X_mcRun4_realistic_v1_RV269_Run4D110_noPU-v1/GEN-SIM-DIGI-RAW',
  '/RelValTTbar_14TeV_TuneCP5/CMSSW_15_1_0_pre5-PU_150X_mcRun4_realistic_v1_RV269_Run4D110_PU-v2/GEN-SIM-DIGI-RAW',
  '/RelValDoubleEFlatPt1To100/CMSSW_15_1_0_pre5-PU_150X_mcRun4_realistic_v1_RV269_Run4D110_PU-v2/GEN-SIM-DIGI-RAW',
  '/RelValDoubleEFlatPt1p5To8/CMSSW_15_1_0_pre5-PU_150X_mcRun4_realistic_v1_RV269_Run4D110_PU-v1/GEN-SIM-DIGI-RAW',
  '/RelValDoubleMuFlatPt1To100/CMSSW_15_1_0_pre5-PU_150X_mcRun4_realistic_v1_RV269_Run4D110_PU-v2/GEN-SIM-DIGI-RAW',
  '/RelValDoubleMuFlatPt1p5To8/CMSSW_15_1_0_pre5-PU_150X_mcRun4_realistic_v1_RV269_Run4D110_PU-v2/GEN-SIM-DIGI-RAW',
  '/RelValDoubleEFlatPt1To100Dxy100GunProducer/CMSSW_15_1_0_pre5-PU_150X_mcRun4_realistic_v1_RV269_Run4D110_PU-v2/GEN-SIM-DIGI-RAW',
  '/RelValDoubleEFlatPt1p5To8Dxy100GunProducer/CMSSW_15_1_0_pre5-PU_150X_mcRun4_realistic_v1_RV269_Run4D110_PU-v2/GEN-SIM-DIGI-RAW',
  '/RelValDoubleMuFlatPt1To100Dxy100GunProducer/CMSSW_15_1_0_pre5-PU_150X_mcRun4_realistic_v1_RV269_Run4D110_PU-v1/GEN-SIM-DIGI-RAW',
  '/RelValDoubleMuFlatPt1p5To8Dxy100GunProducer/CMSSW_15_1_0_pre5-PU_150X_mcRun4_realistic_v1_RV269_Run4D110_PU-v1/GEN-SIM-DIGI-RAW'
]

makeDataCfiFiles(dirName, dataList);
