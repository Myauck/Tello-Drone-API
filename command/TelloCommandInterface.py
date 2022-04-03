#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from abc import abstractmethod


class TelloCommandInterface:

    @abstractmethod
    def getCommand(self) -> str:
        pass

    @abstractmethod
    def getParameters(self) -> list:
        pass

    @abstractmethod
    def isEditable(self) -> bool:
        pass

    @abstractmethod
    def hasResponse(self) -> bool:
        pass
