#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from .AbstractSocket import AbstractSocket


class DroneConnection:

    __client: AbstractSocket
    __buffer_size: int
    __tello_address: tuple[str, int]

    def __init__(self, client_socket: AbstractSocket, tello_address: tuple[str, int],
                 buffer_size: int = 1024):
        self.__client = client_socket
        self.__tello_address = tello_address
        self.changeBufferSize(buffer_size)

    def changeBufferSize(self, buffer_size: int) -> None:
        self.__buffer_size = buffer_size

    def getBufferSize(self) -> int:
        return self.__buffer_size

    def send(self, command: str) -> bool:
        encoded_message = command.encode('utf-8')
        sent = self.__client.getSocket().sendto(encoded_message, self.__tello_address)
        if sent < len(encoded_message):
            return False
        return True

    def recieve(self) -> str:
        return self.__client.getSocket().recv(self.getBufferSize()).decode(encoding="utf-8")

