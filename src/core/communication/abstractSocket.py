import socket
from enum import Enum

class SocketType(Enum):

    SOCKET_UDP = 0
    SOCKET_TCP = 1

class AbstractSocket():

    _socket: socket.socket 

    _host: str
    _port: int

    def __init__(self, host: str, port: int, type: SocketType):
        self._host = host
        self._port = port
        self._socket = self.__defineSocket(type)

    def __defineSocket(self, type: SocketType):
        if type == SocketType.SOCKET_UDP:
            return socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.SOL_UDP)
        elif type == SocketType.SOCKET_TCP:
            return socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.SOL_TCP)
    
    def connect(self):
        self._socket.connect((self._host, self._port))
    
    def disconnect(self):
        self._socket.close()

    def getHost(self) -> str:
        return self._host

    def getPort(self) -> int:
        return self._port

    def getAddress(self) -> tuple[str, int]:
        return (self._host, self._port)
