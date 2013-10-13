import FWCore.ParameterSet.Config as cms

process = cms.Process("RPCQualityFromDigi")
process.load("DQMServices.Core.DQM_cfg")

process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")
#process.load("Geometry.CMSCommonData.cmsExtendedGeometryPostLS1XML_cfi")

process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")

#process.load("Geometry.RPCGeometry.rpcGeometry_cfi")
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'PRE_ST62_V8::All'


#process.load("FWCore.MessageService.MessageLogger_cfi")
#process.load("Geometry.CMSCommonData.cmsExtendedGeometryPostLS1XML_cfi")
#process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")
#process.load("Geometry.RPCGeometry.rpcGeometry_cfi")
#process.load("Geometry.CSCGeometry.cscGeometry_cfi")
#process.load("Alignment.CommonAlignmentProducer.FakeAlignmentSource_cfi")


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


readFiles = cms.untracked.vstring()

process.source = cms.Source ("PoolSource",fileNames = readFiles)


readFiles.extend( [

'file:/afs/cern.ch/work/m/mileva/CMSSW_6_2_0/src/SingleMuPt100_DIGI.root'
     ] );


process.dqmSource = cms.EDAnalyzer("DQMSourceExample",
    monitorName = cms.untracked.string('YourSubsystemName'),
    prescaleEvt = cms.untracked.int32(-1)
)

process.qTester = cms.EDFilter("QualityTester")

#load module defaults
process.load("Validation.MuonRPCDigis.validationMuonRPCDigis_cfi")

#Obsolete code commented
#process.rechivalidation = cms.EDAnalyzer("RPCDigiValid",
#    digiLabel = cms.untracked.string('simMuonRPCDigis'),
#    prescaleLS = cms.untracked.int32(1),
#    outputFile = cms.untracked.string('rpcDigiValidPlots.root'),
#    monitorName = cms.untracked.string('YourSubsystemName'),
#    prescaleEvt = cms.untracked.int32(1000)
#)

#Overwriting default values
process.validationMuonRPCDigis.outputFile = cms.untracked.string('rpcDigiValidPlots.root')

process.p = cms.Path(process.dqmSource+process.validationMuonRPCDigis)
process.DQMStore.verbose = 0
process.DQM.collectorHost = ''
