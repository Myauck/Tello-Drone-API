#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from enum import unique
from .telloEnumParser import *


@unique
class ControlCommand(TelloEnumPaser):

    # COMMAND_NAME = ( COMMAND_PROMPT, UNFORMATED RESPONSE RETURNED )

    COMMAND = ("command")
    TAKEOFF = ("takeoff")
    LAND = ("land")
    STREAMON = ("streamon")
    STREAMOFF = ("streamoff")
    EMERGENCY = ("emergency")

    UP = ("up {y}", ['y'], True)
    DOWN = ("down {y}", ['y'], True)
    LEFT = ("left {x}", ['x'], True)
    RIGHT = ("right {x}", ['x'], True)
    FORWARD = ("forward {z}", ['z'], True)
    BACKWARD = ("back {z}", ['z'], True)

    ROTATE = ("cw {angle}", ['angle'], True)
    ROTATE_INVERT = ("cww {angle}", ['angle'], True)

    def __init__(self, *args) -> None:
        params = self._getDefault(args[1], [])
        editable = self._getDefault(args[2], False)
        response = self._getDefault(args[3], False)
        super().__init__(args[0], params, editable, response)

    def replaceParameters(self, values: dict):
        command = self.getCommand()
        for parameter in self.getParameters():
            command = command.replace("{" + parameter + "}", values[parameter])
        return command
