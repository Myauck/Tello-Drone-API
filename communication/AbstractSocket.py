#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone
from abc import ABC
import socket
from .ProtocolType import ProtocolType


class AbstractSocket(ABC):

    __socket: socket.socket

    def __init__(self, socketType: ProtocolType):
        self.__defineSocket(socketType)

    def getSocket(self):
        return self.__socket

    def __defineSocket(self, socketType: ProtocolType):
        if socketType == ProtocolType.SOCKET_UDP:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.SOL_UDP)
        elif socketType == ProtocolType.SOCKET_TCP:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.SOL_TCP)
