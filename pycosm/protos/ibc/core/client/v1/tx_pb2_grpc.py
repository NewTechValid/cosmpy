# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ibc.core.client.v1 import tx_pb2 as ibc_dot_core_dot_client_dot_v1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the ibc/client Msg service."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateClient = channel.unary_unary(
            "/ibc.core.client.v1.Msg/CreateClient",
            request_serializer=ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgCreateClient.SerializeToString,
            response_deserializer=ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgCreateClientResponse.FromString,
        )
        self.UpdateClient = channel.unary_unary(
            "/ibc.core.client.v1.Msg/UpdateClient",
            request_serializer=ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgUpdateClient.SerializeToString,
            response_deserializer=ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgUpdateClientResponse.FromString,
        )
        self.UpgradeClient = channel.unary_unary(
            "/ibc.core.client.v1.Msg/UpgradeClient",
            request_serializer=ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgUpgradeClient.SerializeToString,
            response_deserializer=ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgUpgradeClientResponse.FromString,
        )
        self.SubmitMisbehaviour = channel.unary_unary(
            "/ibc.core.client.v1.Msg/SubmitMisbehaviour",
            request_serializer=ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgSubmitMisbehaviour.SerializeToString,
            response_deserializer=ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgSubmitMisbehaviourResponse.FromString,
        )


class MsgServicer(object):
    """Msg defines the ibc/client Msg service."""

    def CreateClient(self, request, context):
        """CreateClient defines a rpc handler method for MsgCreateClient."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateClient(self, request, context):
        """UpdateClient defines a rpc handler method for MsgUpdateClient."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpgradeClient(self, request, context):
        """UpgradeClient defines a rpc handler method for MsgUpgradeClient."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SubmitMisbehaviour(self, request, context):
        """SubmitMisbehaviour defines a rpc handler method for MsgSubmitMisbehaviour."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "CreateClient": grpc.unary_unary_rpc_method_handler(
            servicer.CreateClient,
            request_deserializer=ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgCreateClient.FromString,
            response_serializer=ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgCreateClientResponse.SerializeToString,
        ),
        "UpdateClient": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateClient,
            request_deserializer=ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgUpdateClient.FromString,
            response_serializer=ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgUpdateClientResponse.SerializeToString,
        ),
        "UpgradeClient": grpc.unary_unary_rpc_method_handler(
            servicer.UpgradeClient,
            request_deserializer=ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgUpgradeClient.FromString,
            response_serializer=ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgUpgradeClientResponse.SerializeToString,
        ),
        "SubmitMisbehaviour": grpc.unary_unary_rpc_method_handler(
            servicer.SubmitMisbehaviour,
            request_deserializer=ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgSubmitMisbehaviour.FromString,
            response_serializer=ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgSubmitMisbehaviourResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "ibc.core.client.v1.Msg", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the ibc/client Msg service."""

    @staticmethod
    def CreateClient(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ibc.core.client.v1.Msg/CreateClient",
            ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgCreateClient.SerializeToString,
            ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgCreateClientResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpdateClient(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ibc.core.client.v1.Msg/UpdateClient",
            ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgUpdateClient.SerializeToString,
            ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgUpdateClientResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpgradeClient(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ibc.core.client.v1.Msg/UpgradeClient",
            ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgUpgradeClient.SerializeToString,
            ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgUpgradeClientResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SubmitMisbehaviour(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/ibc.core.client.v1.Msg/SubmitMisbehaviour",
            ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgSubmitMisbehaviour.SerializeToString,
            ibc_dot_core_dot_client_dot_v1_dot_tx__pb2.MsgSubmitMisbehaviourResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
