#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

from . import DroneCommandSocket, AbstractSocket, Response, ServiceProvider, ThreadProvider

responses: list[Response]

def recieveInfoService():
    while True:
        try:
            response, tello = self.__connection.recv(self.__BUFFER_SIZE_RECIEVER)
            responses[-1].add(response)
        except socket.error:
            print("Erreur de réception de la réponse")


"""

def getConnection(self) -> socket.socket:
    return self.getSocket()

# Lisaison d'un socket UDP au client
super().__init__(tello_address[0], tello_address[1], ProtocolType.SOCKET_UDP)
self.getSocket().bind(self.__local_address)
        
        
        # Initialise les processus
        self.__init_thread("recv", self.__service_reponse_reciever)

    def send_command(self, command: str):
        req = command.encode(encoding="utf-8")

        # Envoie la commande dans la liste des requêtes
        resp = Response(command)
        self.responses.append(resp)

        # Envoie la commande au serveur Tello
        self.__connection.sendto(req, self.__tello_address)

        # Vérifie si le client reçoit une réponse du serveur avant une limite de temps
        timeout = False
        start = time()
        while not self.responses[-1].has():
            if time() - start > self.__MAX_TIME_OUT:
                timeout = True
                break

        if timeout:
            print("La connexion a échoué")
        else:
            print(self.responses[-1].get())

    def __init_thread(self, name: str, target):

        # Initialise le processus de réception des réponses quand une commande est envoyé à Tello
        self.threads[name] = Thread(target=target)
        self.threads[name].daemon = True
        self.threads[name].start()

    def __service_reponse_reciever(self):

        while True:
            try:
                response, tello = self.__connection.recv(self.__BUFFER_SIZE_RECIEVER)
                self.responses[-1].add(response)
            except socket.error:
                print("Erreur de réception de la réponse")
"""
