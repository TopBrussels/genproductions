import FWCore.ParameterSet.Config as cms

from Configuration.Generator.HerwigppDefaults_cfi import *
from Configuration.Generator.HerwigppUE_EE_3C_cfi import *


generator = cms.EDFilter("ThePEGGeneratorFilter",
	herwigDefaultsBlock,
	herwigppUESettingsBlock,
	crossSection = cms.untracked.double(2.870784e+01),
	filterEfficiency = cms.untracked.double(1),

	configFiles = cms.vstring(),
	parameterSets = cms.vstring(
		'herwigppUE_EE_3C_8000GeV',
		'productionParameters',
		'basicSetup',
		'setParticlesStableForDetector',
	),
	productionParameters = cms.vstring(
		'cd /Herwig/MatrixElements/',
		'create Herwig::MEPP2ZJet MEZJet',
		'insert SimpleQCD:MatrixElements[0] MEZJet',
		'set /Herwig/MatrixElements/MEZJet:ZDecay 5',

		'cd /',
		'set /Herwig/Cuts/QCDCuts:MHatMin 0.0*GeV',
		'set /Herwig/Cuts/JetKtCut:MinKT 50  *GeV',
		'set /Herwig/Cuts/JetKtCut:MaxKT 80  *GeV',
	),
)

configurationMetadata = cms.untracked.PSet(
	version = cms.untracked.string('\$Revision: 1.1 $'),
	name = cms.untracked.string('\$Source: /local/reps/CMSSW/CMSSW/Configuration/GenProduction/python/EightTeV/ZJetToEE_Pt_50to80_TuneEE3C_8TeV_herwigpp_cff.py,v $'),
	annotation = cms.untracked.string('Sumer2012 sample with HERWIGPP: Z + Jet production, Z -> ee, pThat = 50 .. 80 GeV, TuneEE3C')
)
