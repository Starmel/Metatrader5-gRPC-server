# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: market_data.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'market_data.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11market_data.proto\x12\rmetatrader.v1\x1a\x0c\x63ommon.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa2\x01\n\x04Rate\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04open\x18\x02 \x01(\x01\x12\x0c\n\x04high\x18\x03 \x01(\x01\x12\x0b\n\x03low\x18\x04 \x01(\x01\x12\r\n\x05\x63lose\x18\x05 \x01(\x01\x12\x13\n\x0btick_volume\x18\x06 \x01(\x03\x12\x0e\n\x06spread\x18\x07 \x01(\x05\x12\x13\n\x0breal_volume\x18\x08 \x01(\x03\"\x9e\x01\n\x04Tick\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03\x62id\x18\x02 \x01(\x01\x12\x0b\n\x03\x61sk\x18\x03 \x01(\x01\x12\x0c\n\x04last\x18\x04 \x01(\x01\x12\x0e\n\x06volume\x18\x05 \x01(\x04\x12\x10\n\x08time_msc\x18\x06 \x01(\x03\x12\r\n\x05\x66lags\x18\x07 \x01(\r\x12\x13\n\x0bvolume_real\x18\x08 \x01(\x01\"w\n\x14\x43opyRatesFromRequest\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x11\n\ttimeframe\x18\x02 \x01(\x05\x12-\n\tdate_from\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05\x63ount\x18\x04 \x01(\x05\"`\n\x15\x43opyRatesFromResponse\x12\"\n\x05rates\x18\x01 \x03(\x0b\x32\x13.metatrader.v1.Rate\x12#\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x14.metatrader.v1.Error\"^\n\x17\x43opyRatesFromPosRequest\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x11\n\ttimeframe\x18\x02 \x01(\x05\x12\x11\n\tstart_pos\x18\x03 \x01(\x05\x12\r\n\x05\x63ount\x18\x04 \x01(\x05\"c\n\x18\x43opyRatesFromPosResponse\x12\"\n\x05rates\x18\x01 \x03(\x0b\x32\x13.metatrader.v1.Rate\x12#\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x14.metatrader.v1.Error\"\x96\x01\n\x15\x43opyRatesRangeRequest\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x11\n\ttimeframe\x18\x02 \x01(\x05\x12-\n\tdate_from\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07\x64\x61te_to\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"a\n\x16\x43opyRatesRangeResponse\x12\"\n\x05rates\x18\x01 \x03(\x0b\x32\x13.metatrader.v1.Rate\x12#\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x14.metatrader.v1.Error\"s\n\x14\x43opyTicksFromRequest\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12-\n\tdate_from\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\x12\r\n\x05\x66lags\x18\x04 \x01(\x05\"`\n\x15\x43opyTicksFromResponse\x12\"\n\x05ticks\x18\x01 \x03(\x0b\x32\x13.metatrader.v1.Tick\x12#\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x14.metatrader.v1.Error\"\x92\x01\n\x15\x43opyTicksRangeRequest\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12-\n\tdate_from\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07\x64\x61te_to\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05\x66lags\x18\x04 \x01(\x05\"a\n\x16\x43opyTicksRangeResponse\x12\"\n\x05ticks\x18\x01 \x03(\x0b\x32\x13.metatrader.v1.Tick\x12#\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x14.metatrader.v1.Error*\xbb\x03\n\tTIMEFRAME\x12\x19\n\x15TIMEFRAME_UNSPECIFIED\x10\x00\x12\x10\n\x0cTIMEFRAME_M1\x10\x01\x12\x10\n\x0cTIMEFRAME_M2\x10\x02\x12\x10\n\x0cTIMEFRAME_M3\x10\x03\x12\x10\n\x0cTIMEFRAME_M4\x10\x04\x12\x10\n\x0cTIMEFRAME_M5\x10\x05\x12\x10\n\x0cTIMEFRAME_M6\x10\x06\x12\x11\n\rTIMEFRAME_M10\x10\n\x12\x11\n\rTIMEFRAME_M12\x10\x0c\x12\x11\n\rTIMEFRAME_M15\x10\x0f\x12\x11\n\rTIMEFRAME_M20\x10\x14\x12\x11\n\rTIMEFRAME_M30\x10\x1e\x12\x12\n\x0cTIMEFRAME_H1\x10\x81\x80\x01\x12\x12\n\x0cTIMEFRAME_H2\x10\x82\x80\x01\x12\x12\n\x0cTIMEFRAME_H3\x10\x83\x80\x01\x12\x12\n\x0cTIMEFRAME_H4\x10\x84\x80\x01\x12\x12\n\x0cTIMEFRAME_H6\x10\x86\x80\x01\x12\x12\n\x0cTIMEFRAME_H8\x10\x88\x80\x01\x12\x13\n\rTIMEFRAME_H12\x10\x8c\x80\x01\x12\x12\n\x0cTIMEFRAME_D1\x10\x98\x80\x01\x12\x12\n\x0cTIMEFRAME_W1\x10\x81\x80\x02\x12\x13\n\rTIMEFRAME_MN1\x10\x81\x80\x03*g\n\nCOPY_TICKS\x12\x1a\n\x16\x43OPY_TICKS_UNSPECIFIED\x10\x00\x12\x12\n\x0e\x43OPY_TICKS_ALL\x10\x01\x12\x13\n\x0f\x43OPY_TICKS_INFO\x10\x02\x12\x14\n\x10\x43OPY_TICKS_TRADE\x10\x04*\x9d\x01\n\tTICK_FLAG\x12\x19\n\x15TICK_FLAG_UNSPECIFIED\x10\x00\x12\x11\n\rTICK_FLAG_BID\x10\x02\x12\x11\n\rTICK_FLAG_ASK\x10\x04\x12\x12\n\x0eTICK_FLAG_LAST\x10\x08\x12\x14\n\x10TICK_FLAG_VOLUME\x10\x10\x12\x11\n\rTICK_FLAG_BUY\x10 \x12\x12\n\x0eTICK_FLAG_SELL\x10@2\xee\x03\n\x11MarketDataService\x12Z\n\rCopyRatesFrom\x12#.metatrader.v1.CopyRatesFromRequest\x1a$.metatrader.v1.CopyRatesFromResponse\x12\x63\n\x10\x43opyRatesFromPos\x12&.metatrader.v1.CopyRatesFromPosRequest\x1a\'.metatrader.v1.CopyRatesFromPosResponse\x12]\n\x0e\x43opyRatesRange\x12$.metatrader.v1.CopyRatesRangeRequest\x1a%.metatrader.v1.CopyRatesRangeResponse\x12Z\n\rCopyTicksFrom\x12#.metatrader.v1.CopyTicksFromRequest\x1a$.metatrader.v1.CopyTicksFromResponse\x12]\n\x0e\x43opyTicksRange\x12$.metatrader.v1.CopyTicksRangeRequest\x1a%.metatrader.v1.CopyTicksRangeResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'market_data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TIMEFRAME']._serialized_start=1541
  _globals['_TIMEFRAME']._serialized_end=1984
  _globals['_COPY_TICKS']._serialized_start=1986
  _globals['_COPY_TICKS']._serialized_end=2089
  _globals['_TICK_FLAG']._serialized_start=2092
  _globals['_TICK_FLAG']._serialized_end=2249
  _globals['_RATE']._serialized_start=84
  _globals['_RATE']._serialized_end=246
  _globals['_TICK']._serialized_start=249
  _globals['_TICK']._serialized_end=407
  _globals['_COPYRATESFROMREQUEST']._serialized_start=409
  _globals['_COPYRATESFROMREQUEST']._serialized_end=528
  _globals['_COPYRATESFROMRESPONSE']._serialized_start=530
  _globals['_COPYRATESFROMRESPONSE']._serialized_end=626
  _globals['_COPYRATESFROMPOSREQUEST']._serialized_start=628
  _globals['_COPYRATESFROMPOSREQUEST']._serialized_end=722
  _globals['_COPYRATESFROMPOSRESPONSE']._serialized_start=724
  _globals['_COPYRATESFROMPOSRESPONSE']._serialized_end=823
  _globals['_COPYRATESRANGEREQUEST']._serialized_start=826
  _globals['_COPYRATESRANGEREQUEST']._serialized_end=976
  _globals['_COPYRATESRANGERESPONSE']._serialized_start=978
  _globals['_COPYRATESRANGERESPONSE']._serialized_end=1075
  _globals['_COPYTICKSFROMREQUEST']._serialized_start=1077
  _globals['_COPYTICKSFROMREQUEST']._serialized_end=1192
  _globals['_COPYTICKSFROMRESPONSE']._serialized_start=1194
  _globals['_COPYTICKSFROMRESPONSE']._serialized_end=1290
  _globals['_COPYTICKSRANGEREQUEST']._serialized_start=1293
  _globals['_COPYTICKSRANGEREQUEST']._serialized_end=1439
  _globals['_COPYTICKSRANGERESPONSE']._serialized_start=1441
  _globals['_COPYTICKSRANGERESPONSE']._serialized_end=1538
  _globals['_MARKETDATASERVICE']._serialized_start=2252
  _globals['_MARKETDATASERVICE']._serialized_end=2746
# @@protoc_insertion_point(module_scope)
