#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from threading import Thread
from .ProviderInterface import ProviderInterface


class ThreadProvider(ProviderInterface):

    __threads: dict[str, Thread]

    def __init__(self) -> None:
        self.__threads = {}

    def exists(self, threadName: str) -> bool:
        return self.__threads.__contains__(threadName)

    def get(self, threadName: str) -> Thread:
        if self.exists(threadName):
            return self.__threads[threadName]

    def set(self, threadName: str, function: callable) -> bool:
        if self.exists(threadName):
            return False
        self.__threads[threadName] = Thread(target=function)
        return True
    
    def stop(self, threadName: str) -> bool:
        if self.exists(threadName):
            del self.__threads[threadName]
            return True
        return False
