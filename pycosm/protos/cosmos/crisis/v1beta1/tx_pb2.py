# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/crisis/v1beta1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pycosm.protos.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/crisis/v1beta1/tx.proto',
  package='cosmos.crisis.v1beta1',
  syntax='proto3',
  serialized_options=b'Z+github.com/cosmos/cosmos-sdk/x/crisis/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1e\x63osmos/crisis/v1beta1/tx.proto\x12\x15\x63osmos.crisis.v1beta1\x1a\x14gogoproto/gogo.proto\"\xa4\x01\n\x12MsgVerifyInvariant\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12?\n\x15invariant_module_name\x18\x02 \x01(\tB \xf2\xde\x1f\x1cyaml:\"invariant_module_name\"\x12\x33\n\x0finvariant_route\x18\x03 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:\"invariant_route\":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x1c\n\x1aMsgVerifyInvariantResponse2v\n\x03Msg\x12o\n\x0fVerifyInvariant\x12).cosmos.crisis.v1beta1.MsgVerifyInvariant\x1a\x31.cosmos.crisis.v1beta1.MsgVerifyInvariantResponseB-Z+github.com/cosmos/cosmos-sdk/x/crisis/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_MSGVERIFYINVARIANT = _descriptor.Descriptor(
  name='MsgVerifyInvariant',
  full_name='cosmos.crisis.v1beta1.MsgVerifyInvariant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='cosmos.crisis.v1beta1.MsgVerifyInvariant.sender', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='invariant_module_name', full_name='cosmos.crisis.v1beta1.MsgVerifyInvariant.invariant_module_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\034yaml:\"invariant_module_name\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='invariant_route', full_name='cosmos.crisis.v1beta1.MsgVerifyInvariant.invariant_route', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\026yaml:\"invariant_route\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=244,
)


_MSGVERIFYINVARIANTRESPONSE = _descriptor.Descriptor(
  name='MsgVerifyInvariantResponse',
  full_name='cosmos.crisis.v1beta1.MsgVerifyInvariantResponse',
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
  serialized_start=246,
  serialized_end=274,
)

DESCRIPTOR.message_types_by_name['MsgVerifyInvariant'] = _MSGVERIFYINVARIANT
DESCRIPTOR.message_types_by_name['MsgVerifyInvariantResponse'] = _MSGVERIFYINVARIANTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgVerifyInvariant = _reflection.GeneratedProtocolMessageType('MsgVerifyInvariant', (_message.Message,), {
  'DESCRIPTOR' : _MSGVERIFYINVARIANT,
  '__module__' : 'cosmos.crisis.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.crisis.v1beta1.MsgVerifyInvariant)
  })
_sym_db.RegisterMessage(MsgVerifyInvariant)

MsgVerifyInvariantResponse = _reflection.GeneratedProtocolMessageType('MsgVerifyInvariantResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGVERIFYINVARIANTRESPONSE,
  '__module__' : 'cosmos.crisis.v1beta1.tx_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.crisis.v1beta1.MsgVerifyInvariantResponse)
  })
_sym_db.RegisterMessage(MsgVerifyInvariantResponse)


DESCRIPTOR._options = None
_MSGVERIFYINVARIANT.fields_by_name['invariant_module_name']._options = None
_MSGVERIFYINVARIANT.fields_by_name['invariant_route']._options = None
_MSGVERIFYINVARIANT._options = None

_MSG = _descriptor.ServiceDescriptor(
  name='Msg',
  full_name='cosmos.crisis.v1beta1.Msg',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=276,
  serialized_end=394,
  methods=[
  _descriptor.MethodDescriptor(
    name='VerifyInvariant',
    full_name='cosmos.crisis.v1beta1.Msg.VerifyInvariant',
    index=0,
    containing_service=None,
    input_type=_MSGVERIFYINVARIANT,
    output_type=_MSGVERIFYINVARIANTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name['Msg'] = _MSG

# @@protoc_insertion_point(module_scope)
