# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: symbols.proto
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
    'symbols.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rsymbols.proto\x12\rmetatrader.v1\x1a\x0c\x63ommon.proto\"\x15\n\x13SymbolsTotalRequest\"J\n\x14SymbolsTotalResponse\x12\r\n\x05total\x18\x01 \x01(\x05\x12#\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x14.metatrader.v1.Error\"\"\n\x11SymbolsGetRequest\x12\r\n\x05group\x18\x01 \x01(\t\"J\n\x12SymbolsGetResponse\x12\x0f\n\x07symbols\x18\x01 \x03(\t\x12#\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x14.metatrader.v1.Error\"5\n\x13SymbolSelectRequest\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x0e\n\x06\x65nable\x18\x02 \x01(\x08\"L\n\x14SymbolSelectResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12#\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x14.metatrader.v1.Error2\x9e\x02\n\x0eSymbolsService\x12\\\n\x0fGetSymbolsTotal\x12\".metatrader.v1.SymbolsTotalRequest\x1a#.metatrader.v1.SymbolsTotalResponse\"\x00\x12S\n\nGetSymbols\x12 .metatrader.v1.SymbolsGetRequest\x1a!.metatrader.v1.SymbolsGetResponse\"\x00\x12Y\n\x0cSelectSymbol\x12\".metatrader.v1.SymbolSelectRequest\x1a#.metatrader.v1.SymbolSelectResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'symbols_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SYMBOLSTOTALREQUEST']._serialized_start=46
  _globals['_SYMBOLSTOTALREQUEST']._serialized_end=67
  _globals['_SYMBOLSTOTALRESPONSE']._serialized_start=69
  _globals['_SYMBOLSTOTALRESPONSE']._serialized_end=143
  _globals['_SYMBOLSGETREQUEST']._serialized_start=145
  _globals['_SYMBOLSGETREQUEST']._serialized_end=179
  _globals['_SYMBOLSGETRESPONSE']._serialized_start=181
  _globals['_SYMBOLSGETRESPONSE']._serialized_end=255
  _globals['_SYMBOLSELECTREQUEST']._serialized_start=257
  _globals['_SYMBOLSELECTREQUEST']._serialized_end=310
  _globals['_SYMBOLSELECTRESPONSE']._serialized_start=312
  _globals['_SYMBOLSELECTRESPONSE']._serialized_end=388
  _globals['_SYMBOLSSERVICE']._serialized_start=391
  _globals['_SYMBOLSSERVICE']._serialized_end=677
# @@protoc_insertion_point(module_scope)
