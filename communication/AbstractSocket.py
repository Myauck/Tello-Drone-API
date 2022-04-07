#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

import socket
from abc import ABC
from .ProtocolType import ProtocolType
from .ConnectionInterface import ConnectionInterface


class AbstractSocket(ConnectionInterface, ABC):

    _address: tuple[str, int]
    _socket: socket.socket

    def __init__(self, address: tuple[str, int], socketType: ProtocolType = ProtocolType.SOCKET_UDP):
        self.__defineSocket(socketType)
        self._address = address

    def getConnection(self) -> socket.socket:
        return self._socket

    def getAddress(self) -> tuple[str, int]:
        return self._address

    def __defineSocket(self, socketType: ProtocolType):
        if socketType == ProtocolType.SOCKET_UDP:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.SOL_UDP)
        elif socketType == ProtocolType.SOCKET_TCP:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.SOL_TCP)
