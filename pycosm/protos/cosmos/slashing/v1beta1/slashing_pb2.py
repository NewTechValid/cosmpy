# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/slashing/v1beta1/slashing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pycosm.protos.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/slashing/v1beta1/slashing.proto',
  package='cosmos.slashing.v1beta1',
  syntax='proto3',
  serialized_options=b'Z-github.com/cosmos/cosmos-sdk/x/slashing/types\250\342\036\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&cosmos/slashing/v1beta1/slashing.proto\x12\x17\x63osmos.slashing.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb7\x02\n\x14ValidatorSigningInfo\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12-\n\x0cstart_height\x18\x02 \x01(\x03\x42\x17\xf2\xde\x1f\x13yaml:\"start_height\"\x12-\n\x0cindex_offset\x18\x03 \x01(\x03\x42\x17\xf2\xde\x1f\x13yaml:\"index_offset\"\x12Q\n\x0cjailed_until\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x1f\xf2\xde\x1f\x13yaml:\"jailed_until\"\x90\xdf\x1f\x01\xc8\xde\x1f\x00\x12\x12\n\ntombstoned\x18\x05 \x01(\x08\x12?\n\x15missed_blocks_counter\x18\x06 \x01(\x03\x42 \xf2\xde\x1f\x1cyaml:\"missed_blocks_counter\":\x08\xe8\xa0\x1f\x01\x98\xa0\x1f\x00\"\x88\x04\n\x06Params\x12=\n\x14signed_blocks_window\x18\x01 \x01(\x03\x42\x1f\xf2\xde\x1f\x1byaml:\"signed_blocks_window\"\x12m\n\x15min_signed_per_window\x18\x02 \x01(\x0c\x42N\xf2\xde\x1f\x1cyaml:\"min_signed_per_window\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x64\n\x16\x64owntime_jail_duration\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB)\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x1dyaml:\"downtime_jail_duration\"\x12w\n\x1aslash_fraction_double_sign\x18\x04 \x01(\x0c\x42S\xf2\xde\x1f!yaml:\"slash_fraction_double_sign\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12q\n\x17slash_fraction_downtime\x18\x05 \x01(\x0c\x42P\xf2\xde\x1f\x1eyaml:\"slash_fraction_downtime\"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x42\x33Z-github.com/cosmos/cosmos-sdk/x/slashing/types\xa8\xe2\x1e\x01\x62\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_VALIDATORSIGNINGINFO = _descriptor.Descriptor(
  name='ValidatorSigningInfo',
  full_name='cosmos.slashing.v1beta1.ValidatorSigningInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='cosmos.slashing.v1beta1.ValidatorSigningInfo.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_height', full_name='cosmos.slashing.v1beta1.ValidatorSigningInfo.start_height', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\023yaml:\"start_height\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index_offset', full_name='cosmos.slashing.v1beta1.ValidatorSigningInfo.index_offset', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\023yaml:\"index_offset\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='jailed_until', full_name='cosmos.slashing.v1beta1.ValidatorSigningInfo.jailed_until', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\023yaml:\"jailed_until\"\220\337\037\001\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tombstoned', full_name='cosmos.slashing.v1beta1.ValidatorSigningInfo.tombstoned', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='missed_blocks_counter', full_name='cosmos.slashing.v1beta1.ValidatorSigningInfo.missed_blocks_counter', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\034yaml:\"missed_blocks_counter\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\001\230\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=466,
)


_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='cosmos.slashing.v1beta1.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='signed_blocks_window', full_name='cosmos.slashing.v1beta1.Params.signed_blocks_window', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\033yaml:\"signed_blocks_window\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_signed_per_window', full_name='cosmos.slashing.v1beta1.Params.min_signed_per_window', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\034yaml:\"min_signed_per_window\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='downtime_jail_duration', full_name='cosmos.slashing.v1beta1.Params.downtime_jail_duration', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\230\337\037\001\362\336\037\035yaml:\"downtime_jail_duration\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='slash_fraction_double_sign', full_name='cosmos.slashing.v1beta1.Params.slash_fraction_double_sign', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037!yaml:\"slash_fraction_double_sign\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='slash_fraction_downtime', full_name='cosmos.slashing.v1beta1.Params.slash_fraction_downtime', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\036yaml:\"slash_fraction_downtime\"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=469,
  serialized_end=989,
)

_VALIDATORSIGNINGINFO.fields_by_name['jailed_until'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PARAMS.fields_by_name['downtime_jail_duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['ValidatorSigningInfo'] = _VALIDATORSIGNINGINFO
DESCRIPTOR.message_types_by_name['Params'] = _PARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ValidatorSigningInfo = _reflection.GeneratedProtocolMessageType('ValidatorSigningInfo', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATORSIGNINGINFO,
  '__module__' : 'cosmos.slashing.v1beta1.slashing_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.slashing.v1beta1.ValidatorSigningInfo)
  })
_sym_db.RegisterMessage(ValidatorSigningInfo)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'cosmos.slashing.v1beta1.slashing_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.slashing.v1beta1.Params)
  })
_sym_db.RegisterMessage(Params)


DESCRIPTOR._options = None
_VALIDATORSIGNINGINFO.fields_by_name['start_height']._options = None
_VALIDATORSIGNINGINFO.fields_by_name['index_offset']._options = None
_VALIDATORSIGNINGINFO.fields_by_name['jailed_until']._options = None
_VALIDATORSIGNINGINFO.fields_by_name['missed_blocks_counter']._options = None
_VALIDATORSIGNINGINFO._options = None
_PARAMS.fields_by_name['signed_blocks_window']._options = None
_PARAMS.fields_by_name['min_signed_per_window']._options = None
_PARAMS.fields_by_name['downtime_jail_duration']._options = None
_PARAMS.fields_by_name['slash_fraction_double_sign']._options = None
_PARAMS.fields_by_name['slash_fraction_downtime']._options = None
# @@protoc_insertion_point(module_scope)
