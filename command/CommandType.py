#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from enum import Enum, unique


@unique
class CommandType(Enum):

    SETTER = 0,
    GETTER = 1,
    CONTROL = 2

    def type(self):
        return self.value
    