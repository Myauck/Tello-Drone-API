#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from cv2 import VideoCapture


class DroneVideoSocket:

    __tello_address: tuple[str, int]
    __capture = VideoCapture

    def __init__(self, tello_address: tuple[str, int] = ("192.168.10.1", 11111)):
        self.__tello_address = tello_address

        self.__capture = VideoCapture("udp://{}".format(":".join(self.__tello_address)), )

    def getVideoCapture(self):
        return self.__capture

    