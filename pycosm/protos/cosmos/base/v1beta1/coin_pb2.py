# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/base/v1beta1/coin.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pycosm.protos.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/base/v1beta1/coin.proto',
  package='cosmos.base.v1beta1',
  syntax='proto3',
  serialized_options=b'Z\"github.com/cosmos/cosmos-sdk/types\330\341\036\000\200\342\036\000',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1e\x63osmos/base/v1beta1/coin.proto\x12\x13\x63osmos.base.v1beta1\x1a\x14gogoproto/gogo.proto\"8\n\x04\x43oin\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12\x1b\n\x06\x61mount\x18\x02 \x01(\tB\x0b\xda\xde\x1f\x03Int\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x01\";\n\x07\x44\x65\x63\x43oin\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12\x1b\n\x06\x61mount\x18\x02 \x01(\tB\x0b\xda\xde\x1f\x03\x44\x65\x63\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x01\"$\n\x08IntProto\x12\x18\n\x03int\x18\x01 \x01(\tB\x0b\xda\xde\x1f\x03Int\xc8\xde\x1f\x00\"$\n\x08\x44\x65\x63Proto\x12\x18\n\x03\x64\x65\x63\x18\x01 \x01(\tB\x0b\xda\xde\x1f\x03\x44\x65\x63\xc8\xde\x1f\x00\x42,Z\"github.com/cosmos/cosmos-sdk/types\xd8\xe1\x1e\x00\x80\xe2\x1e\x00\x62\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_COIN = _descriptor.Descriptor(
  name='Coin',
  full_name='cosmos.base.v1beta1.Coin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='denom', full_name='cosmos.base.v1beta1.Coin.denom', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='cosmos.base.v1beta1.Coin.amount', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037\003Int\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=133,
)


_DECCOIN = _descriptor.Descriptor(
  name='DecCoin',
  full_name='cosmos.base.v1beta1.DecCoin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='denom', full_name='cosmos.base.v1beta1.DecCoin.denom', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='cosmos.base.v1beta1.DecCoin.amount', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037\003Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=194,
)


_INTPROTO = _descriptor.Descriptor(
  name='IntProto',
  full_name='cosmos.base.v1beta1.IntProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='int', full_name='cosmos.base.v1beta1.IntProto.int', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037\003Int\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=196,
  serialized_end=232,
)


_DECPROTO = _descriptor.Descriptor(
  name='DecProto',
  full_name='cosmos.base.v1beta1.DecProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dec', full_name='cosmos.base.v1beta1.DecProto.dec', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037\003Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=234,
  serialized_end=270,
)

DESCRIPTOR.message_types_by_name['Coin'] = _COIN
DESCRIPTOR.message_types_by_name['DecCoin'] = _DECCOIN
DESCRIPTOR.message_types_by_name['IntProto'] = _INTPROTO
DESCRIPTOR.message_types_by_name['DecProto'] = _DECPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Coin = _reflection.GeneratedProtocolMessageType('Coin', (_message.Message,), {
  'DESCRIPTOR' : _COIN,
  '__module__' : 'cosmos.base.v1beta1.coin_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.v1beta1.Coin)
  })
_sym_db.RegisterMessage(Coin)

DecCoin = _reflection.GeneratedProtocolMessageType('DecCoin', (_message.Message,), {
  'DESCRIPTOR' : _DECCOIN,
  '__module__' : 'cosmos.base.v1beta1.coin_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.v1beta1.DecCoin)
  })
_sym_db.RegisterMessage(DecCoin)

IntProto = _reflection.GeneratedProtocolMessageType('IntProto', (_message.Message,), {
  'DESCRIPTOR' : _INTPROTO,
  '__module__' : 'cosmos.base.v1beta1.coin_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.v1beta1.IntProto)
  })
_sym_db.RegisterMessage(IntProto)

DecProto = _reflection.GeneratedProtocolMessageType('DecProto', (_message.Message,), {
  'DESCRIPTOR' : _DECPROTO,
  '__module__' : 'cosmos.base.v1beta1.coin_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.base.v1beta1.DecProto)
  })
_sym_db.RegisterMessage(DecProto)


DESCRIPTOR._options = None
_COIN.fields_by_name['amount']._options = None
_COIN._options = None
_DECCOIN.fields_by_name['amount']._options = None
_DECCOIN._options = None
_INTPROTO.fields_by_name['int']._options = None
_DECPROTO.fields_by_name['dec']._options = None
# @@protoc_insertion_point(module_scope)
