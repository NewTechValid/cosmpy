# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/vesting/v1beta1/vesting.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pycosm.protos.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pycosm.protos.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pycosm.protos.cosmos.auth.v1beta1 import auth_pb2 as cosmos_dot_auth_dot_v1beta1_dot_auth__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/vesting/v1beta1/vesting.proto',
  package='cosmos.vesting.v1beta1',
  syntax='proto3',
  serialized_options=b'Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$cosmos/vesting/v1beta1/vesting.proto\x12\x16\x63osmos.vesting.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/auth/v1beta1/auth.proto\"\x89\x04\n\x12\x42\x61seVestingAccount\x12<\n\x0c\x62\x61se_account\x18\x01 \x01(\x0b\x32 .cosmos.auth.v1beta1.BaseAccountB\x04\xd0\xde\x1f\x01\x12\x80\x01\n\x10original_vesting\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBK\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x17yaml:\"original_vesting\"\x12|\n\x0e\x64\x65legated_free\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBI\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x15yaml:\"delegated_free\"\x12\x82\x01\n\x11\x64\x65legated_vesting\x18\x04 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBL\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x18yaml:\"delegated_vesting\"\x12%\n\x08\x65nd_time\x18\x05 \x01(\x03\x42\x13\xf2\xde\x1f\x0fyaml:\"end_time\":\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"\x9f\x01\n\x18\x43ontinuousVestingAccount\x12N\n\x14\x62\x61se_vesting_account\x18\x01 \x01(\x0b\x32*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01\x12)\n\nstart_time\x18\x02 \x01(\x03\x42\x15\xf2\xde\x1f\x11yaml:\"start_time\":\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"q\n\x15\x44\x65layedVestingAccount\x12N\n\x14\x62\x61se_vesting_account\x18\x01 \x01(\x0b\x32*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"{\n\x06Period\x12\x0e\n\x06length\x18\x01 \x01(\x03\x12[\n\x06\x61mount\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x04\x98\xa0\x1f\x00\"\xf6\x01\n\x16PeriodicVestingAccount\x12N\n\x14\x62\x61se_vesting_account\x18\x01 \x01(\x0b\x32*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01\x12)\n\nstart_time\x18\x02 \x01(\x03\x42\x15\xf2\xde\x1f\x11yaml:\"start_time\"\x12W\n\x0fvesting_periods\x18\x03 \x03(\x0b\x32\x1e.cosmos.vesting.v1beta1.PeriodB\x1e\xf2\xde\x1f\x16yaml:\"vesting_periods\"\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00\x42\x33Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,cosmos_dot_auth_dot_v1beta1_dot_auth__pb2.DESCRIPTOR,])




_BASEVESTINGACCOUNT = _descriptor.Descriptor(
  name='BaseVestingAccount',
  full_name='cosmos.vesting.v1beta1.BaseVestingAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_account', full_name='cosmos.vesting.v1beta1.BaseVestingAccount.base_account', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\320\336\037\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='original_vesting', full_name='cosmos.vesting.v1beta1.BaseVestingAccount.original_vesting', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\362\336\037\027yaml:\"original_vesting\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delegated_free', full_name='cosmos.vesting.v1beta1.BaseVestingAccount.delegated_free', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\362\336\037\025yaml:\"delegated_free\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delegated_vesting', full_name='cosmos.vesting.v1beta1.BaseVestingAccount.delegated_vesting', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\362\336\037\030yaml:\"delegated_vesting\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='cosmos.vesting.v1beta1.BaseVestingAccount.end_time', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\017yaml:\"end_time\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000\230\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=672,
)


_CONTINUOUSVESTINGACCOUNT = _descriptor.Descriptor(
  name='ContinuousVestingAccount',
  full_name='cosmos.vesting.v1beta1.ContinuousVestingAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_vesting_account', full_name='cosmos.vesting.v1beta1.ContinuousVestingAccount.base_vesting_account', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\320\336\037\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='cosmos.vesting.v1beta1.ContinuousVestingAccount.start_time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\021yaml:\"start_time\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000\230\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=675,
  serialized_end=834,
)


_DELAYEDVESTINGACCOUNT = _descriptor.Descriptor(
  name='DelayedVestingAccount',
  full_name='cosmos.vesting.v1beta1.DelayedVestingAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_vesting_account', full_name='cosmos.vesting.v1beta1.DelayedVestingAccount.base_vesting_account', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\320\336\037\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000\230\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=836,
  serialized_end=949,
)


_PERIOD = _descriptor.Descriptor(
  name='Period',
  full_name='cosmos.vesting.v1beta1.Period',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='length', full_name='cosmos.vesting.v1beta1.Period.length', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='cosmos.vesting.v1beta1.Period.amount', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\230\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=951,
  serialized_end=1074,
)


_PERIODICVESTINGACCOUNT = _descriptor.Descriptor(
  name='PeriodicVestingAccount',
  full_name='cosmos.vesting.v1beta1.PeriodicVestingAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_vesting_account', full_name='cosmos.vesting.v1beta1.PeriodicVestingAccount.base_vesting_account', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\320\336\037\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='cosmos.vesting.v1beta1.PeriodicVestingAccount.start_time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\021yaml:\"start_time\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vesting_periods', full_name='cosmos.vesting.v1beta1.PeriodicVestingAccount.vesting_periods', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\026yaml:\"vesting_periods\"\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000\230\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1077,
  serialized_end=1323,
)

_BASEVESTINGACCOUNT.fields_by_name['base_account'].message_type = cosmos_dot_auth_dot_v1beta1_dot_auth__pb2._BASEACCOUNT
_BASEVESTINGACCOUNT.fields_by_name['original_vesting'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_BASEVESTINGACCOUNT.fields_by_name['delegated_free'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_BASEVESTINGACCOUNT.fields_by_name['delegated_vesting'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_CONTINUOUSVESTINGACCOUNT.fields_by_name['base_vesting_account'].message_type = _BASEVESTINGACCOUNT
_DELAYEDVESTINGACCOUNT.fields_by_name['base_vesting_account'].message_type = _BASEVESTINGACCOUNT
_PERIOD.fields_by_name['amount'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_PERIODICVESTINGACCOUNT.fields_by_name['base_vesting_account'].message_type = _BASEVESTINGACCOUNT
_PERIODICVESTINGACCOUNT.fields_by_name['vesting_periods'].message_type = _PERIOD
DESCRIPTOR.message_types_by_name['BaseVestingAccount'] = _BASEVESTINGACCOUNT
DESCRIPTOR.message_types_by_name['ContinuousVestingAccount'] = _CONTINUOUSVESTINGACCOUNT
DESCRIPTOR.message_types_by_name['DelayedVestingAccount'] = _DELAYEDVESTINGACCOUNT
DESCRIPTOR.message_types_by_name['Period'] = _PERIOD
DESCRIPTOR.message_types_by_name['PeriodicVestingAccount'] = _PERIODICVESTINGACCOUNT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BaseVestingAccount = _reflection.GeneratedProtocolMessageType('BaseVestingAccount', (_message.Message,), {
  'DESCRIPTOR' : _BASEVESTINGACCOUNT,
  '__module__' : 'cosmos.vesting.v1beta1.vesting_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.vesting.v1beta1.BaseVestingAccount)
  })
_sym_db.RegisterMessage(BaseVestingAccount)

ContinuousVestingAccount = _reflection.GeneratedProtocolMessageType('ContinuousVestingAccount', (_message.Message,), {
  'DESCRIPTOR' : _CONTINUOUSVESTINGACCOUNT,
  '__module__' : 'cosmos.vesting.v1beta1.vesting_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.vesting.v1beta1.ContinuousVestingAccount)
  })
_sym_db.RegisterMessage(ContinuousVestingAccount)

DelayedVestingAccount = _reflection.GeneratedProtocolMessageType('DelayedVestingAccount', (_message.Message,), {
  'DESCRIPTOR' : _DELAYEDVESTINGACCOUNT,
  '__module__' : 'cosmos.vesting.v1beta1.vesting_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.vesting.v1beta1.DelayedVestingAccount)
  })
_sym_db.RegisterMessage(DelayedVestingAccount)

Period = _reflection.GeneratedProtocolMessageType('Period', (_message.Message,), {
  'DESCRIPTOR' : _PERIOD,
  '__module__' : 'cosmos.vesting.v1beta1.vesting_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.vesting.v1beta1.Period)
  })
_sym_db.RegisterMessage(Period)

PeriodicVestingAccount = _reflection.GeneratedProtocolMessageType('PeriodicVestingAccount', (_message.Message,), {
  'DESCRIPTOR' : _PERIODICVESTINGACCOUNT,
  '__module__' : 'cosmos.vesting.v1beta1.vesting_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.vesting.v1beta1.PeriodicVestingAccount)
  })
_sym_db.RegisterMessage(PeriodicVestingAccount)


DESCRIPTOR._options = None
_BASEVESTINGACCOUNT.fields_by_name['base_account']._options = None
_BASEVESTINGACCOUNT.fields_by_name['original_vesting']._options = None
_BASEVESTINGACCOUNT.fields_by_name['delegated_free']._options = None
_BASEVESTINGACCOUNT.fields_by_name['delegated_vesting']._options = None
_BASEVESTINGACCOUNT.fields_by_name['end_time']._options = None
_BASEVESTINGACCOUNT._options = None
_CONTINUOUSVESTINGACCOUNT.fields_by_name['base_vesting_account']._options = None
_CONTINUOUSVESTINGACCOUNT.fields_by_name['start_time']._options = None
_CONTINUOUSVESTINGACCOUNT._options = None
_DELAYEDVESTINGACCOUNT.fields_by_name['base_vesting_account']._options = None
_DELAYEDVESTINGACCOUNT._options = None
_PERIOD.fields_by_name['amount']._options = None
_PERIOD._options = None
_PERIODICVESTINGACCOUNT.fields_by_name['base_vesting_account']._options = None
_PERIODICVESTINGACCOUNT.fields_by_name['start_time']._options = None
_PERIODICVESTINGACCOUNT.fields_by_name['vesting_periods']._options = None
_PERIODICVESTINGACCOUNT._options = None
# @@protoc_insertion_point(module_scope)
