#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from abc import ABC, abstractmethod


class ProviderInterface(ABC):

    @abstractmethod
    def exists(self) -> bool:
        pass

    @abstractmethod
    def get(self) -> any:
        pass

    @abstractmethod
    def set(self, value: any) -> None:
        pass
