#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from abc import abstractmethod
from .CommandType import CommandType


class TelloCommandInterface:

    @abstractmethod
    def getCommand(self) -> str: pass

    @abstractmethod
    def getParameters(self) -> list: pass

    @abstractmethod
    def hasParameters(self) -> bool: pass

    @abstractmethod
    def hasResponse(self) -> bool: pass

    @abstractmethod
    def getType(self) -> CommandType: pass
