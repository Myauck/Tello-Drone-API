#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from abc import ABC
from .ServiceProvider import ServiceProvider
from .ThreadProvider import ThreadProvider

class AbstractProviders(ABC):

    __services: ServiceProvider
    __threads: ThreadProvider

    def __init__(self, services: ServiceProvider, threads: ThreadProvider):
        self.__services = services
        self.__threads = threads

    def getServices(self) -> ServiceProvider:
        return self.__services

    def getThreads(self) -> ThreadProvider:
        return self.__threads
