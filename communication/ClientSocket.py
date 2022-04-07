#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone
from typing import Tuple

from .AbstractSocket import AbstractSocket
from .ProtocolType import ProtocolType


class ClientSocket(AbstractSocket):

    __client_address: tuple[str, int]
    __binded: bool

    def __init__(self, client_address: tuple[str, int]):
        super().__init__(ProtocolType.SOCKET_UDP)
        self.__client_address = client_address
        self.__binded = False

    def isBinded(self) -> bool:
        return self.__binded

    def bind(self) -> bool:
        if not self.isBinded():
            super().getSocket().bind(self.__client_address)
            self.__binded = True
        return self.isBinded()

    def unbind(self):
        if self.isBinded():
            super().getSocket().close()
            self.__binded = False
        return self.isBinded()
    
    def getClientAdress(self) -> tuple[str, int]:
        return self.__client_address
