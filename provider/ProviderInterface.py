#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from abc import ABC, abstractmethod


class ProviderInterface(ABC):

    @abstractmethod
    def exists(self, name: str) -> bool:
        pass

    @abstractmethod
    def get(self, name: str):
        pass

    @abstractmethod
    def set(self, name: str, value) -> bool:
        pass
