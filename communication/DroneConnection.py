#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from .ConnectionInterface import ConnectionInterface


class DroneConnection:

    __client: ConnectionInterface
    __tello_address: tuple[str, int]

    def __init__(self, client_connection: ConnectionInterface, tello_address: tuple[str, int]):
        self.__client = client_connection
        self.__tello_address = tello_address

    def send(self, command: str) -> bool:
        encoded_message = command.encode('utf-8')
        sent = self.__client.getConnection().sendto(encoded_message, self.__tello_address)
        if sent < len(encoded_message):
            return False
        return True

    def recieve(self, buffer_size: int = 1024) -> str:
        return self.__client.getConnection().recv(buffer_size).decode(encoding="utf-8")
