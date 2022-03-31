from enum import Enum
from .telloCommandInterface import TelloCommandInterface

class EnumConfigurator(TelloCommandInterface, Enum):

    __command: str
    __parameters: list
    __editable: bool
    __hasResponse: bool

    def __init__(self, command: str, parameters: list, editable: bool, hasResponse: bool):
        self.__command = command
        self.__parameters = parameters
        self.__editable = editable
        self.__hasResponse = hasResponse
        pass

    def _parseCommand(self, commandname):
        if isinstance(commandname, self):
            return commandname.value
        return self.__getitem__(commandname.upper()).value

    def getCommand(self) -> str:
        return self.__command

    def getParameters(self) -> list:
        return self.__parameters

    def isEditable(self) -> bool:
        return self.__editable

    def hasResponse(self) -> bool:
        return self.__hasResponse
