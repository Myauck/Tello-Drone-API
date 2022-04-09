#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

import provider as ModProv
import communication as ModCom


class ConnectionAPI(ModProv.AbstractProviders):

    DRONE_CONNECTION_SERVICE = "drone_connection"
    CLIENT_CONNECTION_SERVICE = "client_connection"

    __client: ModCom.ClientConnection
    __drone: ModCom.DroneConnection

    __debug: bool

    def __init__(self, services: ModProv.ServiceProvider, threads: ModProv.ThreadProvider, DEBUG: bool = True):
        super().__init__(services=services, threads=threads)

        self.getServices().set(self.DRONE_CONNECTION_SERVICE, False)
        self.getServices().set(self.CLIENT_CONNECTION_SERVICE, False)

        self.__debug = DEBUG

    def getClient(self) -> ModCom.ClientConnection:

        # Si le client existe
        if self.getServices().get(self.CLIENT_CONNECTION_SERVICE):
            return self.__client
        else:
            if self.__debug:
                print("Le client n'est pas instancié")

    def getDrone(self) -> ModCom.DroneConnection:

        # Si le drone est connecté
        if self.getServices().get(self.DRONE_CONNECTION_SERVICE):
            return self.__drone
        else:
            if self.__debug:
                print("Le drone n'est pas instancié")

    def bindAddress(self, host: str, port: int) -> None:

        # Si le client n'est pas connecté
        if not self.getServices().get(self.CLIENT_CONNECTION_SERVICE):

            self.__client = ModCom.ClientConnection((host, port))
            self.__client.getConnection().settimeout(15)
            if self.__debug:
                print("Client initialisé")
            self.getServices().set(self.CLIENT_CONNECTION_SERVICE, True)

        # Si le client est déjà connecté
        else:
            if self.__debug:
                print("Le client a déjà été instancié")

    def linkToDrone(self, host: str, port: int) -> None:

        # Si le drone n'est pas connecté
        if not self.getServices().get(self.DRONE_CONNECTION_SERVICE):

            self.__drone = ModCom.DroneConnection(self.__client, (host, port))
            if self.__debug:
                print("Drone a été relié au client avec succès")
            self.getServices().set(self.DRONE_CONNECTION_SERVICE, True)

        # Si le drone est connecté
        else:
            if self.__debug:
                print("Le drone a besoin d'être connecté au client")

    def setTimeout(self, TIMEOUT: int = 15) -> None:

        # Permet de définir une limite de temps pour la récupération des réponses du socket client
        self.__client.getConnection().settimeout(TIMEOUT)
