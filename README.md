# mc_production

Generate ZPrimeToQQ to MC samples. 

### GENSIM
```
cmsDriver.py Configuration/GenProduction/python/ZpToQQ_fragment.py \
  --python_filename ZpToQQ_m500_GENSIM_cfi.py \
  --eventcontent RAWSIM \
  --customise Configuration/DataProcessing/Utils.addMonitoring \
  --datatier GEN-SIM \
  --fileout file:output_GENSIM.root \
  --conditions 140X_mcRun3_2024_realistic_v26 \
  --beamspot Realistic25ns13p6TeVEarly2023Collision \
  --step GEN,SIM \
  --geometry DB:Extended \
  --era Run3_2024 \
  --no_exec \
  --mc \
  -n 50000
```

```
crab submit -c ZpToQQ_crab_GENSIM.py
```

### GENSIM -> DIGI 


```
cmsDriver.py  --python_filename ZpToQQ_m500_DIGI_cfi.py \
 --eventcontent RAWSIM \
 --pileup 2024_25ns_RunIII2024Summer24_PoissonOOTPU \
 --customise Configuration/DataProcessing/Utils.addMonitoring \
 --datatier GEN-SIM-RAW \
 --fileout output_DIGI.root \
 --pileup_input dbs:/Neutrino_E-10_gun/RunIIISummer24PrePremix-Premixlib2024_140X_mcRun3_2024_realistic_v26-v1/PREMIX \
 --conditions 140X_mcRun3_2024_realistic_v26 \
 --step DIGI,L1,DIGI2RAW,HLT:2024v14 \
 --geometry DB:Extended \
 --filein file:output_GENSIM.root \
 --era Run3_2024 \
 --no_exec \
 --mc \
 -n 50000
```

```
crab submit -c ZpToQQ_crab_DIGI.py
```
