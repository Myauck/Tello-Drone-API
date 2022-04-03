#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

import socket
from .socketType import SocketType


class AbstractSocket:

    _socket: socket.socket
    _host: str
    _port: int

    def __init__(self, host: str, port: int, socketType: SocketType):
        self._host = host
        self._port = port
        self.__defineSocket(socketType)

    def connect(self):
        self._socket.connect((self._host, self._port))

    def disconnect(self):
        self._socket.close()

    def getHost(self) -> str:
        return self._host

    def getPort(self) -> int:
        return self._port

    def getAddress(self) -> tuple[str, int]:
        return self._host, self._port

    def __defineSocket(self, socketType: SocketType):
        if socketType == SocketType.SOCKET_UDP:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.SOL_UDP)
        elif socketType == SocketType.SOCKET_TCP:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.SOL_TCP)