# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: symbol_info_tick.proto
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
    'symbol_info_tick.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16symbol_info_tick.proto\x12\rmetatrader.v1\x1a\x0c\x63ommon.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa8\x01\n\x0eSymbolInfoTick\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03\x62id\x18\x02 \x01(\x01\x12\x0b\n\x03\x61sk\x18\x03 \x01(\x01\x12\x0c\n\x04last\x18\x04 \x01(\x01\x12\x0e\n\x06volume\x18\x05 \x01(\x05\x12\x10\n\x08time_msc\x18\x06 \x01(\x03\x12\r\n\x05\x66lags\x18\x07 \x01(\x05\x12\x13\n\x0bvolume_real\x18\x08 \x01(\x01\"\'\n\x15SymbolInfoTickRequest\x12\x0e\n\x06symbol\x18\x01 \x01(\t\"j\n\x16SymbolInfoTickResponse\x12+\n\x04tick\x18\x01 \x01(\x0b\x32\x1d.metatrader.v1.SymbolInfoTick\x12#\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x14.metatrader.v1.Error2y\n\x15SymbolInfoTickService\x12`\n\x11GetSymbolInfoTick\x12$.metatrader.v1.SymbolInfoTickRequest\x1a%.metatrader.v1.SymbolInfoTickResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'symbol_info_tick_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SYMBOLINFOTICK']._serialized_start=89
  _globals['_SYMBOLINFOTICK']._serialized_end=257
  _globals['_SYMBOLINFOTICKREQUEST']._serialized_start=259
  _globals['_SYMBOLINFOTICKREQUEST']._serialized_end=298
  _globals['_SYMBOLINFOTICKRESPONSE']._serialized_start=300
  _globals['_SYMBOLINFOTICKRESPONSE']._serialized_end=406
  _globals['_SYMBOLINFOTICKSERVICE']._serialized_start=408
  _globals['_SYMBOLINFOTICKSERVICE']._serialized_end=529
# @@protoc_insertion_point(module_scope)
