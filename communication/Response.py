#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from time import time


class Response:
    
    __command: str
    __response: str

    __start_time: float
    __duration: float

    def __init__(self, command: str):
        self.__command = command

        self.__start_time = time()
        self.__duration = -1

    def command(self) -> str:
        self.__command

    def add(self, response: str):
        self.__response = str(response)
        # Calcule le temps total nécessaire à l'exécution de la commande
        end_time = time()
        self.__duration = (end_time - self.__start_time)

    def exists(self) -> bool:
        return self.__response is not None

    def get(self) -> str:
        return self.__response

    def duration(self) -> float:
        return self.__duration
