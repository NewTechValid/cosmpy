from abc import ABC
import cosmos.tx.v1beta1.service_pb2 as svc


class RPCInterface(ABC):
    # Simulate simulates executing a transaction for estimating gas usage.
    def Simulate(self, request: svc.SimulateRequest) -> svc.SimulateResponse:
        ...

    # GetTx fetches a tx by hash.
    def GetTx(self, request: svc.GetTxRequest) -> svc.GetTxResponse:
        ...

    # BroadcastTx broadcast transaction.
    def BroadcastTx(self, request: svc.BroadcastTxRequest) -> svc.BroadcastTxResponse:
        ...

    # GetTxsEvent fetches txs by event.
    def GetTxsEvent(self, request: svc.GetTxsEventRequest) -> svc.GetTxsEventResponse:
        ...
