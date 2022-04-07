#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from socket import socket
from abc import ABC, abstractmethod


class ConnectionInterface(ABC):

    @abstractmethod
    def getConnection(self) -> socket:
        pass
