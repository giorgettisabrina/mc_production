import os
import datetime
from CRABClient.UserUtilities import config
config = config()

todaysDate = datetime.date.today().strftime('%Y%m%d')

#key = 'ZpToQQ_m200_GENSIM'
#key = 'ZpToQQ_m400_GENSIM'

key = 'ZpToQQ_m500_GENSIM'
#key = 'ZpToQQ_m800_GENSIM'
#key = 'ZpToQQ_m1000_GENSIM'
#key = 'ZpToQQ_m1200_GENSIM'
#key = 'ZpToQQ_m1500_GENSIM'
#key = 'ZpToQQ_m1700_GENSIM'
#key = 'ZpToQQ_m2000_GENSIM'


config.General.requestName = key+f'_{todaysDate}'
config.General.transferLogs = True
config.General.workArea = '/afs/cern.ch/user/s/sagiorge/monitoring/'

config.JobType.allowUndistributedCMSSW = True
config.JobType.psetName = f'{os.environ["CMSSW_BASE"]}/src/' + key + '_cfi.py'
config.JobType.pluginName = 'PrivateMC'
config.JobType.maxMemoryMB = 5000
config.JobType.maxJobRuntimeMin = 2700

config.Data.splitting = 'EventBased'
config.Data.totalUnits = 50_000     # total number of events
config.Data.unitsPerJob = 1_000 
config.Data.publication = False
config.Data.outputDatasetTag = key + f'_{todaysDate}'
config.Data.outputPrimaryDataset = key

#config.Site.storageSite = 'T2_CH_CERN'
#config.Data.outLFNDirBase = '/store/group/phys_exotica/axol1tl/MC_ScoutingNano/ZPrimeQQ/'

config.Site.storageSite = 'T3_CH_CERNBOX'
config.Data.outLFNDirBase = '/store/user/sagiorge/AXOL1TL/search/mc'
#config.Data.outLFNDirBase = '/eos/user/s/sagiorge/AXOL1TL/search/mc/'
#