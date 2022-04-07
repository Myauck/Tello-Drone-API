#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from enum import unique
from .CommandEnumParser import *


@unique
class ControlCommand(CommandEnumParser):

    # COMMAND_NAME = ( COMMAND_PROMPT, UNFORMATED RESPONSE RETURNED )

    COMMAND = ("command", [])
    TAKEOFF = ("takeoff", [])
    LAND = ("land", [])
    STREAMON = ("streamon", [])
    STREAMOFF = ("streamoff", [])
    EMERGENCY = ("emergency", [])

    UP = ("up {y}", ['y'])
    DOWN = ("down {y}", ['y'])
    LEFT = ("left {x}", ['x'])
    RIGHT = ("right {x}", ['x'])
    FORWARD = ("forward {z}", ['z'])
    BACKWARD = ("back {z}", ['z'])

    ROTATE = ("cw {angle}", ['angle'])
    ROTATE_INVERT = ("cww {angle}", ['angle'])

    def __init__(self, command: str, parameters: list):
        super().__init__(command, parameters, CommandType.CONTROL)

    def FormatCommand(self, arguments: dict[str, str]):
        return self._format(self.getCommand(), arguments)
