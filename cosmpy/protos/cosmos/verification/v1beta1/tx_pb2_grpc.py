# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from cosmos.verification.v1beta1 import tx_pb2 as cosmos_dot_verification_dot_v1beta1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the sign Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SignData = channel.unary_unary(
                '/cosmos.verification.v1beta1.Msg/SignData',
                request_serializer=cosmos_dot_verification_dot_v1beta1_dot_tx__pb2.MsgSignData.SerializeToString,
                response_deserializer=cosmos_dot_verification_dot_v1beta1_dot_tx__pb2.MsgSignDataResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the sign Msg service.
    """

    def SignData(self, request, context):
        """Send defines a method for sending coins from one account to another account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SignData': grpc.unary_unary_rpc_method_handler(
                    servicer.SignData,
                    request_deserializer=cosmos_dot_verification_dot_v1beta1_dot_tx__pb2.MsgSignData.FromString,
                    response_serializer=cosmos_dot_verification_dot_v1beta1_dot_tx__pb2.MsgSignDataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cosmos.verification.v1beta1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the sign Msg service.
    """

    @staticmethod
    def SignData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.verification.v1beta1.Msg/SignData',
            cosmos_dot_verification_dot_v1beta1_dot_tx__pb2.MsgSignData.SerializeToString,
            cosmos_dot_verification_dot_v1beta1_dot_tx__pb2.MsgSignDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
