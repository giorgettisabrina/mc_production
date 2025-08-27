import os
import datetime
from CRABClient.UserUtilities import config
config = config()

todaysDate = datetime.date.today().strftime('%Y%m%d')


#key = 'ZpToQQ_m200_DIGI'
#key = 'ZpToQQ_m400_DIGI'
key = 'ZpToQQ_m500_DIGI'
#key = 'ZpToQQ_m800_DIGI'
#key = 'ZpToQQ_m1000_DIGI'
#key = 'ZpToQQ_m1200_DIGI'
#key = 'ZpToQQ_m1500_DIGI'
#key = 'ZpToQQ_m2000_DIGI'


config.General.requestName = key+f'_{todaysDate}'
config.General.transferLogs = True
config.General.workArea = '/afs/cern.ch/user/s/sagiorge/monitoring/'


config.JobType.allowUndistributedCMSSW = True
config.JobType.psetName = f'{os.environ["CMSSW_BASE"]}/src/' + key + '_cfi.py'
config.JobType.pluginName = 'Analysis'
config.JobType.maxMemoryMB = 5000


config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1



#m500
config.Data.userInputFiles = [
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_1.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_10.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_11.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_12.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_13.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_14.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_15.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_16.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_17.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_18.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_19.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_2.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_20.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_21.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_22.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_23.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_24.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_25.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_26.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_27.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_28.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_29.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_3.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_30.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_31.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_32.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_33.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_34.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_35.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_36.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_37.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_38.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_39.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_4.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_40.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_41.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_42.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_43.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_44.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_45.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_46.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_47.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_48.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_49.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_5.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_50.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_6.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_7.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_8.root',
    'root://eosuser.cern.ch//eos/user/s/sagiorge/AXOL1TL/search/mc/ZpToQQ_m500_GENSIM/ZpToQQ_m500_GENSIM_20250825/250825_151425/0000/output_GENSIM_9.root'
]


config.Data.inputDBS = 'phys03'
config.Data.unitsPerJob = 1
config.Data.publication = False
config.Data.outputDatasetTag = key + f'_{todaysDate}'


#config.Site.storageSite = 'T2_CH_CERN'
#config.Data.outLFNDirBase = '/store/group/phys_exotica/axol1tl/MC_ScoutingNano/ZPrimeQQ/'

config.Site.storageSite = 'T3_CH_CERNBOX'
config.Data.outLFNDirBase = '/store/user/sagiorge/AXOL1TL/search/mc'


