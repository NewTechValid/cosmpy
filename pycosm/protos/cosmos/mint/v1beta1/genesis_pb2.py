# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/mint/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pycosm.protos.cosmos.mint.v1beta1 import (
    mint_pb2 as cosmos_dot_mint_dot_v1beta1_dot_mint__pb2,
)
from pycosm.protos.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="cosmos/mint/v1beta1/genesis.proto",
    package="cosmos.mint.v1beta1",
    syntax="proto3",
    serialized_options=b"Z)github.com/cosmos/cosmos-sdk/x/mint/types",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n!cosmos/mint/v1beta1/genesis.proto\x12\x13\x63osmos.mint.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/mint/v1beta1/mint.proto"t\n\x0cGenesisState\x12\x31\n\x06minter\x18\x01 \x01(\x0b\x32\x1b.cosmos.mint.v1beta1.MinterB\x04\xc8\xde\x1f\x00\x12\x31\n\x06params\x18\x02 \x01(\x0b\x32\x1b.cosmos.mint.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x42+Z)github.com/cosmos/cosmos-sdk/x/mint/typesb\x06proto3',
    dependencies=[
        gogoproto_dot_gogo__pb2.DESCRIPTOR,
        cosmos_dot_mint_dot_v1beta1_dot_mint__pb2.DESCRIPTOR,
    ],
)


_GENESISSTATE = _descriptor.Descriptor(
    name="GenesisState",
    full_name="cosmos.mint.v1beta1.GenesisState",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="minter",
            full_name="cosmos.mint.v1beta1.GenesisState.minter",
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
            name="params",
            full_name="cosmos.mint.v1beta1.GenesisState.params",
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
            serialized_options=b"\310\336\037\000",
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
    serialized_start=112,
    serialized_end=228,
)

_GENESISSTATE.fields_by_name[
    "minter"
].message_type = cosmos_dot_mint_dot_v1beta1_dot_mint__pb2._MINTER
_GENESISSTATE.fields_by_name[
    "params"
].message_type = cosmos_dot_mint_dot_v1beta1_dot_mint__pb2._PARAMS
DESCRIPTOR.message_types_by_name["GenesisState"] = _GENESISSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType(
    "GenesisState",
    (_message.Message,),
    {
        "DESCRIPTOR": _GENESISSTATE,
        "__module__": "cosmos.mint.v1beta1.genesis_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.mint.v1beta1.GenesisState)
    },
)
_sym_db.RegisterMessage(GenesisState)


DESCRIPTOR._options = None
_GENESISSTATE.fields_by_name["minter"]._options = None
_GENESISSTATE.fields_by_name["params"]._options = None
# @@protoc_insertion_point(module_scope)
