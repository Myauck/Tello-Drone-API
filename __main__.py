#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from api import API

api = API(5, 1024, True, True)

api.bind("", 9000)
api.connect("192.168.10.1", 8889)

while True:

    try:
        inp = input(">>> ")

        if not inp:
            break

        response = api.sendRawCommand(inp)

        print(response)

    except KeyboardInterrupt:
        print("Fermeture de la session")
        exit()
