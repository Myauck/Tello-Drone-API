#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from .AbstractSocket import AbstractSocket
from .ProtocolType import ProtocolType


class ClientConnection(AbstractSocket):

    __binded: bool

    def __init__(self, client_address: tuple[str, int]):
        super().__init__(client_address, ProtocolType.SOCKET_UDP)
        super().getConnection().bind(self._address)

    def binded(self) -> bool:
        return self.__binded

    def bind(self) -> None:
        if not self.binded():
            self.__binded = True

    def unbind(self) -> None:
        if self.binded():
            super().getConnection().close()
            self.__binded = False
