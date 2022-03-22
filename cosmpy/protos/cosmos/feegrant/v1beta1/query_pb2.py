# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/feegrant/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.feegrant.v1beta1 import feegrant_pb2 as cosmos_dot_feegrant_dot_v1beta1_dot_feegrant__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/feegrant/v1beta1/query.proto',
  package='cosmos.feegrant.v1beta1',
  syntax='proto3',
  serialized_options=b'Z\'github.com/cosmos/cosmos-sdk/x/feegrant',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#cosmos/feegrant/v1beta1/query.proto\x12\x17\x63osmos.feegrant.v1beta1\x1a&cosmos/feegrant/v1beta1/feegrant.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1cgoogle/api/annotations.proto\"9\n\x15QueryAllowanceRequest\x12\x0f\n\x07granter\x18\x01 \x01(\t\x12\x0f\n\x07grantee\x18\x02 \x01(\t\"K\n\x16QueryAllowanceResponse\x12\x31\n\tallowance\x18\x01 \x01(\x0b\x32\x1e.cosmos.feegrant.v1beta1.Grant\"e\n\x16QueryAllowancesRequest\x12\x0f\n\x07grantee\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x8a\x01\n\x17QueryAllowancesResponse\x12\x32\n\nallowances\x18\x01 \x03(\x0b\x32\x1e.cosmos.feegrant.v1beta1.Grant\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse2\xdf\x02\n\x05Query\x12\xac\x01\n\tAllowance\x12..cosmos.feegrant.v1beta1.QueryAllowanceRequest\x1a/.cosmos.feegrant.v1beta1.QueryAllowanceResponse\">\x82\xd3\xe4\x93\x02\x38\x12\x36/cosmos/feegrant/v1beta1/allowance/{granter}/{grantee}\x12\xa6\x01\n\nAllowances\x12/.cosmos.feegrant.v1beta1.QueryAllowancesRequest\x1a\x30.cosmos.feegrant.v1beta1.QueryAllowancesResponse\"5\x82\xd3\xe4\x93\x02/\x12-/cosmos/feegrant/v1beta1/allowances/{grantee}B)Z\'github.com/cosmos/cosmos-sdk/x/feegrantb\x06proto3'
  ,
  dependencies=[cosmos_dot_feegrant_dot_v1beta1_dot_feegrant__pb2.DESCRIPTOR,cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_QUERYALLOWANCEREQUEST = _descriptor.Descriptor(
  name='QueryAllowanceRequest',
  full_name='cosmos.feegrant.v1beta1.QueryAllowanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='granter', full_name='cosmos.feegrant.v1beta1.QueryAllowanceRequest.granter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grantee', full_name='cosmos.feegrant.v1beta1.QueryAllowanceRequest.grantee', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=178,
  serialized_end=235,
)


_QUERYALLOWANCERESPONSE = _descriptor.Descriptor(
  name='QueryAllowanceResponse',
  full_name='cosmos.feegrant.v1beta1.QueryAllowanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='allowance', full_name='cosmos.feegrant.v1beta1.QueryAllowanceResponse.allowance', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=237,
  serialized_end=312,
)


_QUERYALLOWANCESREQUEST = _descriptor.Descriptor(
  name='QueryAllowancesRequest',
  full_name='cosmos.feegrant.v1beta1.QueryAllowancesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='grantee', full_name='cosmos.feegrant.v1beta1.QueryAllowancesRequest.grantee', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.feegrant.v1beta1.QueryAllowancesRequest.pagination', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=314,
  serialized_end=415,
)


_QUERYALLOWANCESRESPONSE = _descriptor.Descriptor(
  name='QueryAllowancesResponse',
  full_name='cosmos.feegrant.v1beta1.QueryAllowancesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='allowances', full_name='cosmos.feegrant.v1beta1.QueryAllowancesResponse.allowances', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='cosmos.feegrant.v1beta1.QueryAllowancesResponse.pagination', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=418,
  serialized_end=556,
)

_QUERYALLOWANCERESPONSE.fields_by_name['allowance'].message_type = cosmos_dot_feegrant_dot_v1beta1_dot_feegrant__pb2._GRANT
_QUERYALLOWANCESREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYALLOWANCESRESPONSE.fields_by_name['allowances'].message_type = cosmos_dot_feegrant_dot_v1beta1_dot_feegrant__pb2._GRANT
_QUERYALLOWANCESRESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
DESCRIPTOR.message_types_by_name['QueryAllowanceRequest'] = _QUERYALLOWANCEREQUEST
DESCRIPTOR.message_types_by_name['QueryAllowanceResponse'] = _QUERYALLOWANCERESPONSE
DESCRIPTOR.message_types_by_name['QueryAllowancesRequest'] = _QUERYALLOWANCESREQUEST
DESCRIPTOR.message_types_by_name['QueryAllowancesResponse'] = _QUERYALLOWANCESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryAllowanceRequest = _reflection.GeneratedProtocolMessageType('QueryAllowanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYALLOWANCEREQUEST,
  '__module__' : 'cosmos.feegrant.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.feegrant.v1beta1.QueryAllowanceRequest)
  })
_sym_db.RegisterMessage(QueryAllowanceRequest)

QueryAllowanceResponse = _reflection.GeneratedProtocolMessageType('QueryAllowanceResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYALLOWANCERESPONSE,
  '__module__' : 'cosmos.feegrant.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.feegrant.v1beta1.QueryAllowanceResponse)
  })
_sym_db.RegisterMessage(QueryAllowanceResponse)

QueryAllowancesRequest = _reflection.GeneratedProtocolMessageType('QueryAllowancesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYALLOWANCESREQUEST,
  '__module__' : 'cosmos.feegrant.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.feegrant.v1beta1.QueryAllowancesRequest)
  })
_sym_db.RegisterMessage(QueryAllowancesRequest)

QueryAllowancesResponse = _reflection.GeneratedProtocolMessageType('QueryAllowancesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYALLOWANCESRESPONSE,
  '__module__' : 'cosmos.feegrant.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.feegrant.v1beta1.QueryAllowancesResponse)
  })
_sym_db.RegisterMessage(QueryAllowancesResponse)


DESCRIPTOR._options = None

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='cosmos.feegrant.v1beta1.Query',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=559,
  serialized_end=910,
  methods=[
  _descriptor.MethodDescriptor(
    name='Allowance',
    full_name='cosmos.feegrant.v1beta1.Query.Allowance',
    index=0,
    containing_service=None,
    input_type=_QUERYALLOWANCEREQUEST,
    output_type=_QUERYALLOWANCERESPONSE,
    serialized_options=b'\202\323\344\223\0028\0226/cosmos/feegrant/v1beta1/allowance/{granter}/{grantee}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Allowances',
    full_name='cosmos.feegrant.v1beta1.Query.Allowances',
    index=1,
    containing_service=None,
    input_type=_QUERYALLOWANCESREQUEST,
    output_type=_QUERYALLOWANCESRESPONSE,
    serialized_options=b'\202\323\344\223\002/\022-/cosmos/feegrant/v1beta1/allowances/{grantee}',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)
