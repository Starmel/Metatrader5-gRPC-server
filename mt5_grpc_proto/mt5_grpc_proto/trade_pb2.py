# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: trade.proto
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
    'trade.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0btrade.proto\x12\rmetatrader.v1\x1a\x0c\x63ommon.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xed\x03\n\x0cTradeRequest\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\x05\x12\r\n\x05magic\x18\x02 \x01(\x05\x12\x12\n\x05order\x18\x03 \x01(\x03H\x00\x88\x01\x01\x12\x13\n\x06symbol\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x0e\n\x06volume\x18\x05 \x01(\x01\x12\x12\n\x05price\x18\x06 \x01(\x01H\x02\x88\x01\x01\x12\x16\n\tstoplimit\x18\x07 \x01(\x01H\x03\x88\x01\x01\x12\x0f\n\x02sl\x18\x08 \x01(\x01H\x04\x88\x01\x01\x12\x0f\n\x02tp\x18\t \x01(\x01H\x05\x88\x01\x01\x12\x11\n\tdeviation\x18\n \x01(\x05\x12\x0c\n\x04type\x18\x0b \x01(\x05\x12\x14\n\x0ctype_filling\x18\x0c \x01(\x05\x12\x11\n\ttype_time\x18\r \x01(\x05\x12\x33\n\nexpiration\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x06\x88\x01\x01\x12\x14\n\x07\x63omment\x18\x0f \x01(\tH\x07\x88\x01\x01\x12\x15\n\x08position\x18\x10 \x01(\x03H\x08\x88\x01\x01\x12\x18\n\x0bposition_by\x18\x11 \x01(\x03H\t\x88\x01\x01\x42\x08\n\x06_orderB\t\n\x07_symbolB\x08\n\x06_priceB\x0c\n\n_stoplimitB\x05\n\x03_slB\x05\n\x03_tpB\r\n\x0b_expirationB\n\n\x08_commentB\x0b\n\t_positionB\x0e\n\x0c_position_by\"\xe1\x01\n\x0bTradeResult\x12\x0f\n\x07retcode\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x65\x61l\x18\x02 \x01(\x03\x12\r\n\x05order\x18\x03 \x01(\x03\x12\x0e\n\x06volume\x18\x04 \x01(\x01\x12\r\n\x05price\x18\x05 \x01(\x01\x12\x0b\n\x03\x62id\x18\x06 \x01(\x01\x12\x0b\n\x03\x61sk\x18\x07 \x01(\x01\x12\x0f\n\x07\x63omment\x18\x08 \x01(\t\x12\x12\n\nrequest_id\x18\t \x01(\x03\x12\x18\n\x10retcode_external\x18\n \x01(\x05\x12,\n\x07request\x18\x0b \x01(\x0b\x32\x1b.metatrader.v1.TradeRequest\"F\n\x10OrderSendRequest\x12\x32\n\rtrade_request\x18\x01 \x01(\x0b\x32\x1b.metatrader.v1.TradeRequest\"j\n\x11OrderSendResponse\x12\x30\n\x0ctrade_result\x18\x01 \x01(\x0b\x32\x1a.metatrader.v1.TradeResult\x12#\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x14.metatrader.v1.Error2b\n\x10OrderSendService\x12N\n\tSendOrder\x12\x1f.metatrader.v1.OrderSendRequest\x1a .metatrader.v1.OrderSendResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'trade_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TRADEREQUEST']._serialized_start=78
  _globals['_TRADEREQUEST']._serialized_end=571
  _globals['_TRADERESULT']._serialized_start=574
  _globals['_TRADERESULT']._serialized_end=799
  _globals['_ORDERSENDREQUEST']._serialized_start=801
  _globals['_ORDERSENDREQUEST']._serialized_end=871
  _globals['_ORDERSENDRESPONSE']._serialized_start=873
  _globals['_ORDERSENDRESPONSE']._serialized_end=979
  _globals['_ORDERSENDSERVICE']._serialized_start=981
  _globals['_ORDERSENDSERVICE']._serialized_end=1079
# @@protoc_insertion_point(module_scope)