# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: history_orders.proto
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
    'history_orders.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14history_orders.proto\x12\rmetatrader.v1\x1a\x0c\x63ommon.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x96\x01\n\x14HistoryOrdersRequest\x12\x30\n\x0btime_filter\x18\x01 \x01(\x0b\x32\x19.metatrader.v1.TimeFilterH\x00\x12\x10\n\x06ticket\x18\x02 \x01(\x04H\x00\x12\x12\n\x08position\x18\x03 \x01(\x04H\x00\x12\x12\n\x05group\x18\x04 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06\x66ilterB\x08\n\x06_group\"?\n\x19HistoryOrdersTotalRequest\x12\x11\n\tdate_from\x18\x01 \x01(\x03\x12\x0f\n\x07\x64\x61te_to\x18\x02 \x01(\x03\"_\n\x1aHistoryOrdersTotalResponse\x12\r\n\x05total\x18\x01 \x01(\x05\x12(\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x14.metatrader.v1.ErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"x\n\x15HistoryOrdersResponse\x12+\n\x06orders\x18\x01 \x03(\x0b\x32\x1b.metatrader.v1.HistoryOrder\x12(\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x14.metatrader.v1.ErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"\x9d\x04\n\x0cHistoryOrder\x12\x0e\n\x06ticket\x18\x01 \x01(\x04\x12.\n\ntime_setup\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0etime_setup_msc\x18\x03 \x01(\x03\x12-\n\ttime_done\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rtime_done_msc\x18\x05 \x01(\x03\x12\x33\n\x0ftime_expiration\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04type\x18\x07 \x01(\x05\x12\x11\n\ttype_time\x18\x08 \x01(\x05\x12\x14\n\x0ctype_filling\x18\t \x01(\x05\x12\r\n\x05state\x18\n \x01(\x05\x12\r\n\x05magic\x18\x0b \x01(\r\x12\x13\n\x0bposition_id\x18\x0c \x01(\x04\x12\x16\n\x0evolume_initial\x18\r \x01(\x01\x12\x16\n\x0evolume_current\x18\x0e \x01(\x01\x12\x12\n\nprice_open\x18\x0f \x01(\x01\x12\x11\n\tstop_loss\x18\x10 \x01(\x01\x12\x13\n\x0btake_profit\x18\x11 \x01(\x01\x12\x15\n\rprice_current\x18\x12 \x01(\x01\x12\x17\n\x0fprice_stoplimit\x18\x13 \x01(\x01\x12\x0e\n\x06symbol\x18\x14 \x01(\t\x12\x0f\n\x07\x63omment\x18\x15 \x01(\t\x12\x13\n\x0b\x65xternal_id\x18\x16 \x01(\t2\xe3\x01\n\x14HistoryOrdersService\x12]\n\x10GetHistoryOrders\x12#.metatrader.v1.HistoryOrdersRequest\x1a$.metatrader.v1.HistoryOrdersResponse\x12l\n\x15GetHistoryOrdersTotal\x12(.metatrader.v1.HistoryOrdersTotalRequest\x1a).metatrader.v1.HistoryOrdersTotalResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'history_orders_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_HISTORYORDERSREQUEST']._serialized_start=87
  _globals['_HISTORYORDERSREQUEST']._serialized_end=237
  _globals['_HISTORYORDERSTOTALREQUEST']._serialized_start=239
  _globals['_HISTORYORDERSTOTALREQUEST']._serialized_end=302
  _globals['_HISTORYORDERSTOTALRESPONSE']._serialized_start=304
  _globals['_HISTORYORDERSTOTALRESPONSE']._serialized_end=399
  _globals['_HISTORYORDERSRESPONSE']._serialized_start=401
  _globals['_HISTORYORDERSRESPONSE']._serialized_end=521
  _globals['_HISTORYORDER']._serialized_start=524
  _globals['_HISTORYORDER']._serialized_end=1065
  _globals['_HISTORYORDERSSERVICE']._serialized_start=1068
  _globals['_HISTORYORDERSSERVICE']._serialized_end=1295
# @@protoc_insertion_point(module_scope)
