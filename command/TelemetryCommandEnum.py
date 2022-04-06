#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from enum import unique
from .CommandEnumParser import *


@unique
class TelemetryCommand(CommandEnumParser):

    # 1: COMMANDE       2: UNITE

    # Permet de récupérer la vitesse actuelle du drone (exprimée en cm/s)
    SPEED = ("speed?", "{unit} cm/s")

    # Permet de récupérer le pourcentage de batterie restant
    BATTERY = ("battery?", "{unit} %")

    # Permet de récupérer le temps de fonctionnement du moteur depuis son lancement
    TIME = ("time?", "{unit} sec")

    # Permet de récupérer la qualité du signal réseau envoyé au drone
    WIFI = ("wifi?", "{unit} dB")

    # Permet d'obtenir l'identifiant de connection du socket du drone
    SDK = "sdk?"

    # Permet d'obtenir le numéro de série du drone
    SERIAL_NUMBER = "sn"

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
    TOF = "tof?"

    __unit: str

    def __init__(self, *args):
        unit = self._getDefault(args[1], "{unit}")
        super().__init__(args[0], unit, False, True, CommandType.GETTER)

    def getUnit(self, value) -> str:
        return self.__unit.replace("{unit}", value)
