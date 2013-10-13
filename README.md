GemDigiValidation
=================

a test repository for GEM Digi MC validaton, consumes API 

cmsrel CMSSW_6_2_0_SLHC1
cd CMSSW_6_2_0_SLHC1/src/
cmsenv
git-clone https://github.com/mileva/GemDigiValidation.git
mkdir Validation
cp -r GemDigiValidation/Validation/MuonGEMDigis/ Validation/
rm -rf GemDigiValidation
scram b
cmsRun Validation/MuonGEMDigis/gemDigiValid.py
root -l gemDigiValidPlots.root
