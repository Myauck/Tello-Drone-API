#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

import provider as ModProv
import communication as ModCom
import command as ModCmd
from socket import error
from time import time


class API:

    __services: ModProv.ServiceProvider
    __threads: ModProv.ThreadProvider

    __client: ModCom.ClientConnection
    __drone: ModCom.DroneConnection

    __responses: list[ModCom.Response]

    __timeout: int
    __buffer: int
    __authorizer_reponse_reciever: bool

    def __init__(self, RECIEVE_TIMEOUT: int, RECIEVE_BUFFER: int, AUTOMATISE_RESPONSE_RECIEVER: bool):
        self.__services = ModProv.ServiceProvider()
        self.__threads = ModProv.ThreadProvider()

        self.__timeout = RECIEVE_TIMEOUT
        self.__buffer = RECIEVE_BUFFER
        self.__authorizer_reponse_reciever = AUTOMATISE_RESPONSE_RECIEVER

        self.__init__thread_reciever()

    def getServices(self) -> ModProv.ServiceProvider:
        return self.__services

    def getThread(self) -> ModProv.ThreadProvider:
        return self.__threads

    def connect(self, host: str, port: int) -> None:
        self.__drone = ModCom.DroneConnection(self.__client, (host, port))

    def bind(self, host: str, port: int) -> None:
        self.__client = ModCom.ClientConnection((host, port))
        self.__client.getConnection().settimeout(self.__timeout)

    def sendCommand(self, command: ModCmd.TelloCommandInterface, parameters: dict[str, str] = None) -> str:
        if isinstance(command, (ModCmd.ControlCommand, ModCmd.TelemetryCommand)):
            return self.__sendCommand(command, command.getType(), parameters)

    def sendRawCommand(self, command: str) -> str:
        return self.__send(command)

    def __sendCommand(self, command: [ModCmd.ControlCommand, ModCmd.TelemetryCommand],
                      command_type: ModCmd.CommandType, parameters: dict[str, str]) -> str:

        if command_type == ModCmd.CommandType.CONTROL:
            return self.__send(command.FormatCommand(parameters))
        elif command_type == ModCmd.CommandType.INFORMATION:
            return self.__send(command.getCommand())

    def __send(self, command: str) -> str:

        self.__add_response(command)

        self.__drone.send(command)

        if self.__authorizer_reponse_reciever:
            return self.Response_loop_reciever().getResponse()
        return command

    def getResponses(self) -> list[ModCom.Response]:
        return self.__responses

    def Response_loop_reciever(self) -> ModCom.Response:
        timeout = False
        start = time()
        while not self.getResponses()[-1].responseExists():
            if time() - start > self.__timeout:
                timeout = True
                break

        if not timeout:
            return self.getResponses()[-1]

    def __add_response(self, command: str):
        response_waiter = ModCom.Response(command)
        self.__responses.append(response_waiter)

    def __init__thread_reciever(self):
        self.getThread().set('response_reciever', self.__thread_receiver)
        self.getThread().get('response_reciever').daemon = True
        self.getThread().get('response_reciever').start()

    def __thread_receiver(self):
        while True:
            try:
                response, _ = self.__drone.recieve(self.__buffer)
                self.getResponses()[-1].setResponse(response)
            except error:
                print("Impossible de recevoir la réponse")
