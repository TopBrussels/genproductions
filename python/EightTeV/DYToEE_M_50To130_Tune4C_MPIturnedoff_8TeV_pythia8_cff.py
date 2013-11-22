import FWCore.ParameterSet.Config as cms

generator = cms.EDFilter("Pythia8GeneratorFilter",
   crossSection = cms.untracked.double(897),
   maxEventsToPrint = cms.untracked.int32(0),
   pythiaPylistVerbosity = cms.untracked.int32(1),
   filterEfficiency = cms.untracked.double(1.0),
   pythiaHepMCVerbosity = cms.untracked.bool(False),
   comEnergy = cms.double(8000.0),
   PythiaParameters = cms.PSet(
       processParameters = cms.vstring(
           'Tune:pp 5',
       
           'Main:timesAllowErrors = 10000',
           'WeakSingleBoson:ffbar2gmZ = on', # turn on Z production
           'ParticleDecays:limitTau0 = on',
           'ParticleDecays:tau0Max = 10.',

           'PartonLevel:MI = off',
           'SecondHard:generate = off',
           'SecondHard:TwoJets = off',
           'PhaseSpace:sameForSecond = off',
           #'PhaseSpace:pTHatMinSecond = 15',

           'PhaseSpace:mHatMin = 50',
           'PhaseSpace:mHatMax = 130',
           '23:onMode = off',  #turn off all Z decays
           '23:onIfAny = 11'   # turn ON Z->ee
       ),
       parameterSets = cms.vstring('processParameters')
   )
)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.2 $'),
    name = cms.untracked.string('$Source: /local/reps/CMSSW/CMSSW/Configuration/GenProduction/python/EightTeV/DYToEE_M_50To130_Tune4C_MPIturnedoff_8TeV_pythia8_cff.py,v $'),
    annotation = cms.untracked.string('PYTHIA8 Z/gamma* to ee, 50 < M(e+e-) < 130 GeV at sqrt(s) = 8TeV, Tune 4C MPI turned off')
)
