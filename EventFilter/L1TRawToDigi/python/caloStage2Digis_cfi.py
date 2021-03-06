import FWCore.ParameterSet.Config as cms

caloStage2Digis = cms.EDProducer(
    "L1TRawToDigi",
    Setup           = cms.string("stage2::CaloSetup"),
    FedIds          = cms.vint32( 1360, 1366 ),
)
