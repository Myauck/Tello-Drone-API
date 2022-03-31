from enum import unique
from ...core.command.enumConfigurator import EnumConfigurator

@unique
class ControlCommandEnum(EnumConfigurator):

    # COMMAND_NAME = ( COMMAND_PROMPT, UNFORMATED RESPONSE RETURNED )

    COMMAND = ("command", [])
    TAKEOFF = ("takeoff", [])
    LAND = ("land", [])
    STREAMON = ("steamon", [])
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

    def __init__(self, *args):
        super().__init__(args[0], args[1], True, False)

    def replaceParameters(self, values: dict):
        command = self.getCommand()
        for parameter in self.getParameters():
            command = command.replace("{"+parameter+"}", values[parameter])
        return command