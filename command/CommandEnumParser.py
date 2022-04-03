#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from .telloCommandInterface import TelloCommandInterface
from .commandType import CommandType
from enum import Enum


def getDefaultValue(argument, default_value):
    if argument is not None:
        return argument
    return default_value


def getEnumValue(enum: Enum, command_name: object):
    if isinstance(command_name, type(enum)):
        return command_name.value
    elif isinstance(command_name, str):
        if hasattr(enum, command_name.upper()):
            return getattr(enum, command_name.upper())


class TelloEnumPaser(TelloCommandInterface, Enum):

    __command: str
    __parameters: list
    __editable: bool
    __hasResponse: bool
    __type: CommandType

    def __init__(self, command: str, parameters: list, editable: bool, hasResponse: bool,
                 commandType: CommandType) -> None:
        super().__init__()
        self.__command = command
        self.__parameters = parameters
        self.__editable = editable
        self.__hasResponse = hasResponse
        self.__type = commandType

    def getCommand(self) -> str:
        return self.__command

    def getParameters(self) -> list:
        return self.__parameters

    def isEditable(self) -> bool:
        return self.__editable

    def hasResponse(self) -> bool:
        return self.__hasResponse

    def getType(self) -> CommandType:
        return self.__type
