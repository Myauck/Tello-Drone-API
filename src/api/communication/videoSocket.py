from ...core.communication.abstractSocket import *
from cv2 import VideoCapture as video

class VideoSocket(AbstractSocket):

    __capure: video

    def __init__(self,  host: str = "192.168.10.1",
                        port: int = 11111,
                        type: SocketType = SocketType.SOCKET_UDP):

        super().__init__(host, port, type)
        self.__capture = video('udp://' + self.getHost() + ':11111')
        pass

    def getCamera(self) -> video:
        return self.__capture

    def getLastFrame(self) -> tuple:
        return self.__capture.read()[1]
