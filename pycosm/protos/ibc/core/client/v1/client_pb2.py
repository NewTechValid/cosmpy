# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/client/v1/client.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2

from pycosm.protos.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="ibc/core/client/v1/client.proto",
    package="ibc.core.client.v1",
    syntax="proto3",
    serialized_options=b"Z7github.com/cosmos/cosmos-sdk/x/ibc/core/02-client/types",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1fibc/core/client/v1/client.proto\x12\x12ibc.core.client.v1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto"\x85\x01\n\x15IdentifiedClientState\x12\'\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"client_id"\x12\x43\n\x0c\x63lient_state\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyB\x17\xf2\xde\x1f\x13yaml:"client_state""\x96\x01\n\x18\x43onsensusStateWithHeight\x12\x30\n\x06height\x18\x01 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\x12H\n\x0f\x63onsensus_state\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyB\x19\xf2\xde\x1f\x15yaml"consensus_state""\xa9\x01\n\x15\x43lientConsensusStates\x12\'\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"client_id"\x12g\n\x10\x63onsensus_states\x18\x02 \x03(\x0b\x32,.ibc.core.client.v1.ConsensusStateWithHeightB\x1f\xf2\xde\x1f\x17yaml:"consensus_states"\xc8\xde\x1f\x00"\x8f\x01\n\x14\x43lientUpdateProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\'\n\tclient_id\x18\x03 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"client_id"\x12$\n\x06header\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any:\x04\x88\xa0\x1f\x00"|\n\x06Height\x12\x33\n\x0frevision_number\x18\x01 \x01(\x04\x42\x1a\xf2\xde\x1f\x16yaml:"revision_number"\x12\x33\n\x0frevision_height\x18\x02 \x01(\x04\x42\x1a\xf2\xde\x1f\x16yaml:"revision_height":\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00"=\n\x06Params\x12\x33\n\x0f\x61llowed_clients\x18\x01 \x03(\tB\x1a\xf2\xde\x1f\x16yaml:"allowed_clients"B9Z7github.com/cosmos/cosmos-sdk/x/ibc/core/02-client/typesb\x06proto3',
    dependencies=[
        gogoproto_dot_gogo__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_any__pb2.DESCRIPTOR,
    ],
)


_IDENTIFIEDCLIENTSTATE = _descriptor.Descriptor(
    name="IdentifiedClientState",
    full_name="ibc.core.client.v1.IdentifiedClientState",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="client_id",
            full_name="ibc.core.client.v1.IdentifiedClientState.client_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\020yaml:"client_id"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="client_state",
            full_name="ibc.core.client.v1.IdentifiedClientState.client_state",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\023yaml:"client_state"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=105,
    serialized_end=238,
)


_CONSENSUSSTATEWITHHEIGHT = _descriptor.Descriptor(
    name="ConsensusStateWithHeight",
    full_name="ibc.core.client.v1.ConsensusStateWithHeight",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="height",
            full_name="ibc.core.client.v1.ConsensusStateWithHeight.height",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="consensus_state",
            full_name="ibc.core.client.v1.ConsensusStateWithHeight.consensus_state",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\025yaml"consensus_state"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=241,
    serialized_end=391,
)


_CLIENTCONSENSUSSTATES = _descriptor.Descriptor(
    name="ClientConsensusStates",
    full_name="ibc.core.client.v1.ClientConsensusStates",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="client_id",
            full_name="ibc.core.client.v1.ClientConsensusStates.client_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\020yaml:"client_id"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="consensus_states",
            full_name="ibc.core.client.v1.ClientConsensusStates.consensus_states",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\027yaml:"consensus_states"\310\336\037\000',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=394,
    serialized_end=563,
)


_CLIENTUPDATEPROPOSAL = _descriptor.Descriptor(
    name="ClientUpdateProposal",
    full_name="ibc.core.client.v1.ClientUpdateProposal",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="title",
            full_name="ibc.core.client.v1.ClientUpdateProposal.title",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="ibc.core.client.v1.ClientUpdateProposal.description",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="client_id",
            full_name="ibc.core.client.v1.ClientUpdateProposal.client_id",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\020yaml:"client_id"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="header",
            full_name="ibc.core.client.v1.ClientUpdateProposal.header",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\210\240\037\000",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=566,
    serialized_end=709,
)


_HEIGHT = _descriptor.Descriptor(
    name="Height",
    full_name="ibc.core.client.v1.Height",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="revision_number",
            full_name="ibc.core.client.v1.Height.revision_number",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\026yaml:"revision_number"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="revision_height",
            full_name="ibc.core.client.v1.Height.revision_height",
            index=1,
            number=2,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\026yaml:"revision_height"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\210\240\037\000\230\240\037\000",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=711,
    serialized_end=835,
)


_PARAMS = _descriptor.Descriptor(
    name="Params",
    full_name="ibc.core.client.v1.Params",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="allowed_clients",
            full_name="ibc.core.client.v1.Params.allowed_clients",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\026yaml:"allowed_clients"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=837,
    serialized_end=898,
)

_IDENTIFIEDCLIENTSTATE.fields_by_name[
    "client_state"
].message_type = google_dot_protobuf_dot_any__pb2._ANY
_CONSENSUSSTATEWITHHEIGHT.fields_by_name["height"].message_type = _HEIGHT
_CONSENSUSSTATEWITHHEIGHT.fields_by_name[
    "consensus_state"
].message_type = google_dot_protobuf_dot_any__pb2._ANY
_CLIENTCONSENSUSSTATES.fields_by_name[
    "consensus_states"
].message_type = _CONSENSUSSTATEWITHHEIGHT
_CLIENTUPDATEPROPOSAL.fields_by_name[
    "header"
].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name["IdentifiedClientState"] = _IDENTIFIEDCLIENTSTATE
DESCRIPTOR.message_types_by_name["ConsensusStateWithHeight"] = _CONSENSUSSTATEWITHHEIGHT
DESCRIPTOR.message_types_by_name["ClientConsensusStates"] = _CLIENTCONSENSUSSTATES
DESCRIPTOR.message_types_by_name["ClientUpdateProposal"] = _CLIENTUPDATEPROPOSAL
DESCRIPTOR.message_types_by_name["Height"] = _HEIGHT
DESCRIPTOR.message_types_by_name["Params"] = _PARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IdentifiedClientState = _reflection.GeneratedProtocolMessageType(
    "IdentifiedClientState",
    (_message.Message,),
    {
        "DESCRIPTOR": _IDENTIFIEDCLIENTSTATE,
        "__module__": "ibc.core.client.v1.client_pb2"
        # @@protoc_insertion_point(class_scope:ibc.core.client.v1.IdentifiedClientState)
    },
)
_sym_db.RegisterMessage(IdentifiedClientState)

ConsensusStateWithHeight = _reflection.GeneratedProtocolMessageType(
    "ConsensusStateWithHeight",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONSENSUSSTATEWITHHEIGHT,
        "__module__": "ibc.core.client.v1.client_pb2"
        # @@protoc_insertion_point(class_scope:ibc.core.client.v1.ConsensusStateWithHeight)
    },
)
_sym_db.RegisterMessage(ConsensusStateWithHeight)

ClientConsensusStates = _reflection.GeneratedProtocolMessageType(
    "ClientConsensusStates",
    (_message.Message,),
    {
        "DESCRIPTOR": _CLIENTCONSENSUSSTATES,
        "__module__": "ibc.core.client.v1.client_pb2"
        # @@protoc_insertion_point(class_scope:ibc.core.client.v1.ClientConsensusStates)
    },
)
_sym_db.RegisterMessage(ClientConsensusStates)

ClientUpdateProposal = _reflection.GeneratedProtocolMessageType(
    "ClientUpdateProposal",
    (_message.Message,),
    {
        "DESCRIPTOR": _CLIENTUPDATEPROPOSAL,
        "__module__": "ibc.core.client.v1.client_pb2"
        # @@protoc_insertion_point(class_scope:ibc.core.client.v1.ClientUpdateProposal)
    },
)
_sym_db.RegisterMessage(ClientUpdateProposal)

Height = _reflection.GeneratedProtocolMessageType(
    "Height",
    (_message.Message,),
    {
        "DESCRIPTOR": _HEIGHT,
        "__module__": "ibc.core.client.v1.client_pb2"
        # @@protoc_insertion_point(class_scope:ibc.core.client.v1.Height)
    },
)
_sym_db.RegisterMessage(Height)

Params = _reflection.GeneratedProtocolMessageType(
    "Params",
    (_message.Message,),
    {
        "DESCRIPTOR": _PARAMS,
        "__module__": "ibc.core.client.v1.client_pb2"
        # @@protoc_insertion_point(class_scope:ibc.core.client.v1.Params)
    },
)
_sym_db.RegisterMessage(Params)


DESCRIPTOR._options = None
_IDENTIFIEDCLIENTSTATE.fields_by_name["client_id"]._options = None
_IDENTIFIEDCLIENTSTATE.fields_by_name["client_state"]._options = None
_CONSENSUSSTATEWITHHEIGHT.fields_by_name["height"]._options = None
_CONSENSUSSTATEWITHHEIGHT.fields_by_name["consensus_state"]._options = None
_CLIENTCONSENSUSSTATES.fields_by_name["client_id"]._options = None
_CLIENTCONSENSUSSTATES.fields_by_name["consensus_states"]._options = None
_CLIENTUPDATEPROPOSAL.fields_by_name["client_id"]._options = None
_CLIENTUPDATEPROPOSAL._options = None
_HEIGHT.fields_by_name["revision_number"]._options = None
_HEIGHT.fields_by_name["revision_height"]._options = None
_HEIGHT._options = None
_PARAMS.fields_by_name["allowed_clients"]._options = None
# @@protoc_insertion_point(module_scope)
