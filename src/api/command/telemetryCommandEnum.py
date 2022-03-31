from enum import unique
from ...core.command.enumConfigurator import EnumConfigurator

@unique
class TelemetryCommandEnum(EnumConfigurator):

    # COMMAND_NAME = ( COMMAND_PROMPT, UNFORMATED RESPONSE RETURNED )

    # Permet de récupérer la vitesse actuelle du drone (exprimée en cm/s)
    SPEED = ("speed?", "{unit} cm/s")

    # Permet de récupérer le pourcentage de batterie restant
    BATTERY = ("battery?", "{unit} %")

    # Permet de récupérer le temps de fonctionnement du moteur depuis son lancement
    TIME = ("time?", "{unit} sec")

    # Permet de récupérer la qualité du signal réseau envoyé au drone
    WIFI = ("wifi?", "{unit} dB")

    # Permet d'obtenir l'identifiant de connection du socket du drone
    SDK = ("sdk?")

    # Permet d'obtenir le numéro de série du drone
    SERIAL_NUMBER = ("sn")

    # Permet de récupérer la hauteur actuelle du drone
    HEIGHT = ("height?", "{unit} cm")

    # Permet de récupérer la température du drone
    TEMPERATURE = ("temp?", "{unit} °C")

    # ................
    ATTITUDE = ("attitude?", "{unit} cm")

    # ................
    BAROMETER = ("baro?", "{unit} Pa")

    # ................
    ACCELERATION = ("acceleration?", "{unit} cm/s")

    # ................
    TOF = ("tof?")

    __unit: str

    def __init__(self, *args):
        super().__init__(args[0], [], False, True)
        if len(args) > 1:
            self.__unit = args[1]
        else:
            self.__unit = "{unit}"

    def getUnit(self, value) -> str:
        return self.__unit.replace("{unit}", value)