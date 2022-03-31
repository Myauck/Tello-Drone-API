from ...core.communication.abstractSocket import *

class StateSocket(AbstractSocket):

    def __init__(self,  host: str = "192.168.10.1",
                        port: int = 8890,
                        type: SocketType = SocketType.SOCKET_UDP):
        super().__init__(host, port, type)
        pass

    def log(self) -> str:
        return self._socket.recv(1024).decode('utf-8')

