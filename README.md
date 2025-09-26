# Python scripts to simplify MC dataset access from CMSSW

## How to checkout repo 

From your CMSSW_X_Y_Z/src/ directory (after doing "cmsenv" & checking out any C++ code you need first):

* git clone git@github.com:cms-L1TK/MCsamples.git

## How to create a _cfi.py file for each required MC dataset

For common datasets used by the L1TrkAlgo group, these may already exist in MCsamples/RelVal_*/python/*_cfi.py,
where the directory name gives the CMSSW version (and sometimes geometry too).

If your desired dataset is missing:

1) cd MCsamples/Scripts/python/
2) cp getMC_15_1_0_D110.py myNewScript.py
3) Edit myNewScript.py, to specify the dataset names you want & name of output directory to be created for your new _cfi.py files.
4) python3 myNewScript.py  

## How to access MC from your CMSSW job's *_cfg.py file

Add one of the following three options in your *_cfg.py file:

a) Read MC dataset from a specified card file:

from MCsamples.RelVal_1130_D76.PU200_TTbar_14TeV_cfi import *
inputMC = getCMSdataFromCards()

b) Read all .root files from a directory on your local computer:

from MCsamples.Scripts.getCMSlocaldata_cfi import *
dirName = "${HOME}/myDirectory/" 
inputMC=getCMSlocaldata(dirName)

c) Read MC dataset using CMS DB instead of card file.

N.B. Only use this method occassionally, as it overworks the DB.

from MCsamples.Scripts.getCMSdata_cfi import *
dataName="/RelValTTbar_14TeV/CMSSW_11_2_0_pre5-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/GEN-SIM-DIGI-RAW"
inputMC=getCMSdata(dataName)
