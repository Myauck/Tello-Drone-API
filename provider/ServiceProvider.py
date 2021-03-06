#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from .ProviderInterface import ProviderInterface


class ServiceProvider(ProviderInterface):

    __statements: dict[str, bool]

    def __init__(self) -> None:
        self.__statements = {}

    def exists(self, statementName: str) -> bool:
        return self.__statements.__contains__(statementName)

    def get(self, statementName: str) -> bool:
        if self.exists(statementName):
            return self.__statements[statementName]

    def set(self, statementName, status: bool) -> None:
        if not self.exists(statementName):
            self.__statements[statementName] = status
