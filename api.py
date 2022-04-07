#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from . import *
from socket import error as socketError


class TelloAPI:

    __serviceProvider: ServiceProvider
    __threadProvider: ThreadProvider

    __responses: list[Response]
    __client: ClientSocket
    __drone: DroneConnection

    __videoCapturer: DroneVideoSocket

    def __init__(self):
        self.__client = ClientSocket(("0.0.0.0", 9000))
        self.__drone = DroneConnection(self.__client, ("0.0.0.0", 8889))

        self.__serviceProvider.set("commandsdk", False)
        self.__threadProvider.set("command_response_reciever", self.__thread_reciever)

    def getDroneAttribute(self, telemetryCommand: TelemetryCommand):
        self.__sendCommand(telemetryCommand.getCommand())

    def sendDroneCommand(self, controlCommand: ControlCommand, parameters: dict[str, str] = None):
        if controlCommand.hasParameters():
            self.__sendCommand(controlCommand.replaceParameters(parameters))
        else:
            self.__sendCommand(controlCommand.getCommand())

    def __sendCommand(self, command: str):
        if self.__serviceProvider.get("commandsdk"):
            self.__drone.send(command)
        else:
            print("Vous devez déjà entrer dans le service \"command\" du drone")

    def getLastResponse(self) -> str:
        return self.__responses[-1].get()

    def __thread_reciever(self):
        while True:
            try:
                response = self.__drone.recieve()
                self.__responses.append(response)
            except socketError:
                print("Erreur de réception de la réponse")

    def getClient(self):
        return self.__client

    def getDrone(self) -> DroneConnection:
        return self.__drone

    def getStream(self) -> DroneVideoSocket:
        return self.__videoCapturer

    def getResponses(self) -> list[Response]:
        return self.__responses

    def getServices(self) -> ServiceProvider:
        return self.__serviceProvider

    def getThreads(self) -> ThreadProvider:
        return self.__threadProvider
