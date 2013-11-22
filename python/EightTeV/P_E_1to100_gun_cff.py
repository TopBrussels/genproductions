import FWCore.ParameterSet.Config as cms

generator = cms.EDProducer('FlatRandomEGunProducer',
	PGunParameters = cms.PSet(
		PartID = cms.vint32(2212),
		MinPhi = cms.double(-3.14159265359), ## in radians
		MaxPhi = cms.double(3.14159265359),
		MinEta = cms.double(-2.5),
		MaxEta = cms.double(2.5),
		MinE = cms.double(1   ),
		MaxE = cms.double(100 ),
	),
	Verbosity = cms.untracked.int32(0),
	psethack = cms.string('single p E 1   -100 '),
	AddAntiParticle = cms.bool(False),
)

configurationMetadata = cms.untracked.PSet(
	version = cms.untracked.string('\$Revision: 1.1 $'),
	name = cms.untracked.string('\$Source: /local/reps/CMSSW/CMSSW/Configuration/GenProduction/python/EightTeV/P_E_1to100_gun_cff.py,v $'),
	annotation = cms.untracked.string('Summer2012 sample with GUN: Flat random proton gun, E = 1 .. 100 GeV, no tune')
)
