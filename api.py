#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

import provider as ModProv
import communication as ModCom
import command as ModCmd

from socket import error
from time import time
from uuid import uuid4 as uuid

from ConnectionApi import Connection


debug: bool = False


class API(ModProv.AbstractProviders):

    ControlCommand: ModCmd.ControlCommand
    TelemetryCommand: ModCmd.TelemetryCommand

    __connections: Connection

    __responses: list[ModCom.Request]

    __timeout: int
    __buffer: int
    __authorizer_reponse_reciever: bool
    __debug: bool

    def __init__(self, RECIEVE_TIMEOUT: int, RECIEVE_BUFFER: int, AUTOMATISE_RESPONSE_RECIEVER: bool, DEBUG: bool):

        self.__timeout = RECIEVE_TIMEOUT
        self.__buffer = RECIEVE_BUFFER
        self.__authorizer_reponse_reciever = AUTOMATISE_RESPONSE_RECIEVER
        self.__debug = DEBUG

        super().__init__(ModProv.ServiceProvider(), ModProv.ThreadProvider())

        self.__connections = Connection(self.getServices(), self.getThreads(), self.__debug)

        self.__responses = []

    def getConnections(self) -> Connection:
        return self.__connections


class Command(ModProv.AbstractProviders):

    def sendCommand(self, command: ModCmd.TelloCommandInterface, parameters: dict[str, str] = None) -> str:
        if isinstance(command, (ModCmd.ControlCommand, ModCmd.TelemetryCommand)):
            return self.__sendCommand(command, command.getType(), parameters)

    def sendRawCommand(self, command: str) -> str:
        command = self.__send(command)
        self.getServices().set("response_ask", False)
        return command

    def __sendCommand(self, command: [ModCmd.ControlCommand, ModCmd.TelemetryCommand],
                      command_type: ModCmd.CommandType, parameters: dict[str, str]) -> str:

        self.getServices().set("response_ask", True)

        if command_type == ModCmd.CommandType.CONTROL:
            command = self.__send(command.FormatCommand(parameters))
        elif command_type == ModCmd.CommandType.INFORMATION:
            command = self.__send(command.getCommand())

        self.getServices().set("response_ask", False)
        return command

    def __send(self, command: str) -> str:
        # Ajoute une requête dans la liste des réponses
        self.__add_response(command)

        # Envoie la commande au drone
        self.__drone.send(command)

        # Vérifie si le système de récupération de réponses est automatique
        if self.__authorizer_reponse_reciever:
            if self.recievedResponse():
                return self.getResponses()[-1].getResponse()
            else:
                return ""
        return command
class ResponseAPI(ModProv.AbstractProviders):

    RESPONSE_RECIEVER_LOOP = "response_reciever_thread"
    CLIENT_CONNECTION_SERVICE = "client_connection"

    __responses: dict[str, ModCom.Response]
    __last_id: str

    __debug: bool

    def __init__(self, services: ModProv.ServiceProvider, threads: ModProv.ThreadProvider, DEBUG: bool = True):
        super().__init__(services=services, threads=threads)

        self.getServices().set(self.DRONE_CONNECTION_SERVICE, False)
        self.getServices().set(self.CLIENT_CONNECTION_SERVICE, False)

        self.__debug = DEBUG

    def getResponses(self) -> list[ModCom.Response]:
        return self.__responses.values()

    def recievedResponse(self) -> bool:
        timeout = False
        start = time()

        # Tant que la réponse n'a pas été récupérée
        while not self.getResponses()[-1].hasResponse():

            # Si le temps écoulé est dépassé
            if time() - start > self.__timeout:
                timeout = True
                break

        # Renvoi s'il n'y a pas eu de timeout
        return not timeout

    def __add_response(self, command: str):
        response_waiter = ModCom.Response(command)
        self.__responses.append(response_waiter)

    def __thread_receiver(self):
        while True:
            if self.getServices().get("response_ask"):
                try:
                    response, addr = self.getConnections().getDrone().recieve(self.__buffer)
                    self.getResponses()[-1].setResponse(response)
                except error:
                    print("Impossible de recevoir la réponse")

