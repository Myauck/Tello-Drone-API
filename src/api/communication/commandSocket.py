from ...core.communication.abstractSocket import *
from src.core.command.telloCommandInterface import TelloCommandInterface

class CommandSocket(AbstractSocket):

    __buffer_size: int

    def __init__(self,  host: str = "192.168.10.1",
                        port: int = 8889,
                        type: SocketType = SocketType.SOCKET_UDP,
                        buffer_size: int = 1024):

        super().__init__(host, port, type)
        self.__buffer_size = buffer_size
        pass

    def send(self, command: TelloCommandInterface):
        encodedMessage = command.getCommand().encode('utf-8')
        sent = self._socket.send(encodedMessage)
        if sent < len(encodedMessage):
            raise Exception("Le message n'a pas correctement été envoyé")

    def receive(self) -> str:
        return self._socket.recv(self.getBuffer()).decode('utf-8')

    def getBuffer(self) -> int:
        return self.__buffer_size
