#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from time import time


class Response:

    __sent: str
    __response: str
    __start_time: float
    __duration: float

    def __init__(self, sent: str):
        self.__sent = sent
        self.__start_time = time()
        self.__duration = -1

    def whatSent(self) -> str:
        return self.__sent

    def setResponse(self, response: str):
        if not self.responseExists():
            self.__response = str(response)
            self.__duration = time() - self.__start_time

    def responseExists(self) -> bool:
        return self.__response is not None

    def getResponse(self) -> str:
        return self.__response

    def getReceptionTime(self) -> float:
        return self.__duration
