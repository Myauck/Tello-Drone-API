#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from time import time


class Request:

    __sent: str
    __recv: str
    __recieved: bool
    __start_time: float
    __duration: float

    def __init__(self, sent: str):
        self.__sent = sent
        self.__recieved = False
        self.__start_time = time()
        self.__duration = -1

    def getRequest(self) -> str:
        return self.__sent

    def setResponse(self, response: str) -> None:
        if not self.isResponseExists():
            self.__recv = str(response)
            self.__recieved = True
            self.__duration = time() - self.__start_time

    def getResponse(self) -> str:
        return self.__recv

    def isResponseExists(self) -> bool:
        return self.__recieved

    def executionTime(self) -> float:
        return self.__duration
