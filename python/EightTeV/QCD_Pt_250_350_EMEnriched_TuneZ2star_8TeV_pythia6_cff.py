import FWCore.ParameterSet.Config as cms

source = cms.Source("EmptySource")

from Configuration.Generator.PythiaUEZ2starSettings_cfi import *
generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(0.131),
    crossSection = cms.untracked.double(4.25e3),
    comEnergy = cms.double(8000.0),  # center of mass energy in GeV
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring('MSEL=1               ! QCD high pT processes',
                                        'CKIN(3)=250.          ! minimum pt hat for hard interactions',
                                        'CKIN(4)=350.          ! maximum pt hat for hard interactions'
                                        ),
        parameterSets = cms.vstring('pythiaUESettings', 
                                    'processParameters')
        )
)

genParticlesForFilter = cms.EDProducer("GenParticleProducer",
    saveBarCodes = cms.untracked.bool(True),
    src = cms.InputTag("generator"),
    abortOnUnknownPDGCode = cms.untracked.bool(True)
)

bctoefilter = cms.EDFilter("BCToEFilter",
                           filterAlgoPSet = cms.PSet(eTThreshold = cms.double(10),
                                                     genParSource = cms.InputTag("genParticlesForFilter")
                                                     )
                           )

emenrichingfilter = cms.EDFilter("EMEnrichingFilter",
                                 filterAlgoPSet = cms.PSet(isoGenParETMin=cms.double(20.),
                                                           isoGenParConeSize=cms.double(0.1),
                                                           clusterThreshold=cms.double(20.),
                                                           isoConeSize=cms.double(0.2),
                                                           hOverEMax=cms.double(0.5),
                                                           tkIsoMax=cms.double(5.),
                                                           caloIsoMax=cms.double(10.),
                                                           requireTrackMatch=cms.bool(False),
                                                           genParSource = cms.InputTag("genParticlesForFilter")
                                                           )
                                 )
    


# enter below the configuration metadata (only a description is needed, the rest is filled in by cvs)
configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.2 $'),
    name = cms.untracked.string('$Source: /local/reps/CMSSW/CMSSW/Configuration/GenProduction/python/EightTeV/QCD_Pt_250_350_EMEnriched_TuneZ2star_8TeV_pythia6_cff.py,v $'),
    annotation = cms.untracked.string('em-enriching filtered QCD pthat 80-170, 8 TeV')
)

# add your filters to this sequence
ProductionFilterSequence = cms.Sequence(generator * (genParticlesForFilter + ~bctoefilter + emenrichingfilter))

