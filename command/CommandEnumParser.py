#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from .TelloCommandInterface import TelloCommandInterface
from .CommandType import CommandType
from enum import Enum


class CommandEnumParser(TelloCommandInterface, Enum):

    __command: str
    __parameters: list
    __command_type: CommandType

    def __init__(self, command: str, parameters: list, commandType: CommandType) -> None:
        super().__init__()
        self.__command = command
        self.__parameters = parameters
        self.__command_type = commandType

    def getCommand(self) -> str:
        return self.__command

    def getParameters(self) -> list:
        return self.__parameters

    def hasParameters(self) -> bool:
        return self.__parameters is not []

    def getType(self) -> CommandType:
        return self.__command_type

    def _format(self, attribute: str, arguments: dict[str, str]) -> str:
        for parameter in self.getParameters():
            attribute = attribute.replace("{"+parameter+"}", arguments[parameter])
        return attribute
