#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from enum import unique
from .CommandEnumParser import *


@unique
class TelemetryCommand(CommandEnumParser):

    # Permet de récupérer la vitesse actuelle du drone (exprimée en cm/s)
    SPEED = ("speed?", "cm/s")

    # Permet de récupérer le pourcentage de batterie restant
    BATTERY = ("battery?", "%")

    # Permet de récupérer le temps de fonctionnement du moteur depuis son lancement
    TIME = ("time?", "sec")

    # Permet de récupérer la qualité du signal réseau envoyé au drone
    WIFI = ("wifi?", "dB")

    # Permet de récupérer la hauteur de vol du drone
    HEIGHT = ("height?", "cm")

    # Permet de récupérer la température du drone
    TEMPERATURE = ("temp?", "°C")

    # Récupère l'altitude du drone
    ATTITUDE = ("attitude?", "cm")

    # Récupère la pression atmosphérique actuelle
    BAROMETER = ("baro?", "Pa")

    # ................
    ACCELERATION = ("acceleration?", "cm/s")

    # Distance entre le capteur et le sol
    TOF = ("tof?", "mm")

    # Permet d'obtenir le numéro de série du drone
    SERIAL_NUMBER = ("sn?", "")

    # Permet d'obtenir l'identifiant de connection du socket du drone
    SDK = ("sdk?", "")

    __unit: str

    def __init__(self, command: str, unit: str):
        self.__unit = unit
        super().__init__(command, [], CommandType.INFORMATION)

    def getUnit(self) -> str:
        return self.__unit

    def getUnitResponse(self, response: str) -> str:
        return response + " " + self.getUnit()
