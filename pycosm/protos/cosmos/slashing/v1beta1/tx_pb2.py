# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/slashing/v1beta1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pycosm.protos.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/slashing/v1beta1/tx.proto',
  package='cosmos.slashing.v1beta1',
  syntax='proto3',
  serialized_options=b'Z-github.com/cosmos/cosmos-sdk/x/slashing/types\250\342\036\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n cosmos/slashing/v1beta1/tx.proto\x12\x17\x63osmos.slashing.v1beta1\x1a\x14gogoproto/gogo.proto\"L\n\tMsgUnjail\x12\x35\n\x0evalidator_addr\x18\x01 \x01(\tB\x1d\xf2\xde\x1f\x0eyaml:\"address\"\xea\xde\x1f\x07\x61\x64\x64ress:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x01\"\x13\n\x11MsgUnjailResponse2_\n\x03Msg\x12X\n\x06Unjail\x12\".cosmos.slashing.v1beta1.MsgUnjail\x1a*.cosmos.slashing.v1beta1.MsgUnjailResponseB3Z-github.com/cosmos/cosmos-sdk/x/slashing/types\xa8\xe2\x1e\x01\x62\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_MSGUNJAIL = _descriptor.Descriptor(
  name='MsgUnjail',
  full_name='cosmos.slashing.v1beta1.MsgUnjail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='validator_addr', full_name='cosmos.slashing.v1beta1.MsgUnjail.validator_addr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\016yaml:\"address\"\352\336\037\007address', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000\230\240\037\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=159,
)


_MSGUNJAILRESPONSE = _descriptor.Descriptor(
  name='MsgUnjailResponse',
  full_name='cosmos.slashing.v1beta1.MsgUnjailResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=161,
  serialized_end=180,
)

DESCRIPTOR.message_types_by_name['MsgUnjail'] = _MSGUNJAIL
DESCRIPTOR.message_types_by_name['MsgUnjailResponse'] = _MSGUNJAILRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgUnjail = _reflection.GeneratedProtocolMessageType('MsgUnjail', (_message.Message,), {
  'DESCRIPTOR' : _MSGUNJAIL,
  '__module__' : 'cosmos.slashing.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.slashing.v1beta1.MsgUnjail)
  })
_sym_db.RegisterMessage(MsgUnjail)

MsgUnjailResponse = _reflection.GeneratedProtocolMessageType('MsgUnjailResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGUNJAILRESPONSE,
  '__module__' : 'cosmos.slashing.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.slashing.v1beta1.MsgUnjailResponse)
  })
_sym_db.RegisterMessage(MsgUnjailResponse)


DESCRIPTOR._options = None
_MSGUNJAIL.fields_by_name['validator_addr']._options = None
_MSGUNJAIL._options = None

_MSG = _descriptor.ServiceDescriptor(
  name='Msg',
  full_name='cosmos.slashing.v1beta1.Msg',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=182,
  serialized_end=277,
  methods=[
  _descriptor.MethodDescriptor(
    name='Unjail',
    full_name='cosmos.slashing.v1beta1.Msg.Unjail',
    index=0,
    containing_service=None,
    input_type=_MSGUNJAIL,
    output_type=_MSGUNJAILRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name['Msg'] = _MSG

# @@protoc_insertion_point(module_scope)
