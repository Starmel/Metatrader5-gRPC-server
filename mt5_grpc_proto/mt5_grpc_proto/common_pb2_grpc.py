# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import common_pb2 as common__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in common_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class MetaTraderServiceStub(object):
    """Service definition
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Connect = channel.unary_unary(
                '/metatrader.v1.MetaTraderService/Connect',
                request_serializer=common__pb2.ConnectRequest.SerializeToString,
                response_deserializer=common__pb2.Error.FromString,
                _registered_method=True)
        self.GetLastError = channel.unary_unary(
                '/metatrader.v1.MetaTraderService/GetLastError',
                request_serializer=common__pb2.Empty.SerializeToString,
                response_deserializer=common__pb2.GetLastErrorResponse.FromString,
                _registered_method=True)


class MetaTraderServiceServicer(object):
    """Service definition
    """

    def Connect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLastError(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MetaTraderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Connect': grpc.unary_unary_rpc_method_handler(
                    servicer.Connect,
                    request_deserializer=common__pb2.ConnectRequest.FromString,
                    response_serializer=common__pb2.Error.SerializeToString,
            ),
            'GetLastError': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLastError,
                    request_deserializer=common__pb2.Empty.FromString,
                    response_serializer=common__pb2.GetLastErrorResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'metatrader.v1.MetaTraderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('metatrader.v1.MetaTraderService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class MetaTraderService(object):
    """Service definition
    """

    @staticmethod
    def Connect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/metatrader.v1.MetaTraderService/Connect',
            common__pb2.ConnectRequest.SerializeToString,
            common__pb2.Error.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetLastError(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/metatrader.v1.MetaTraderService/GetLastError',
            common__pb2.Empty.SerializeToString,
            common__pb2.GetLastErrorResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)