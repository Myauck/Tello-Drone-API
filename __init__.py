#  Copyright (c) 2022.
#  Myauck <leogaillet77@gmail.com>
#
#  File made for Tello Drone

import provider as ModProv
import communication as ModCom
import command as ModCmd
from api import API


class TelloAPI(API):

    # Liste des commande de contrôle
    ControlCommand: ModCmd.ControlCommand

    # Liste de commandes télémétriques
    TelemetryCommand: ModCmd.TelemetryCommand

    def __init__(self, RECIEVE_TIMEOUT: int = 15, RECIEVE_BUFFER: int = 1024,
                 AUTOMATISE_RESPONSE_RECIEVER: bool = True):
        """
        Méthode d'initialisation de la classe API pour le drone Tello

        :param RECIEVE_TIMEOUT: Temps (sec) avant le temps écoulé lors de la reception d'une réponse
        :param RECIEVE_BUFFER: Nombre de bits maximum lu lors de la réception de données venant du drône
        :param AUTOMATISE_RESPONSE_RECIEVER: Si le système de réponse est directement utilisé lors d'envoie d'une
        commande
        """
        super().__init__(RECIEVE_TIMEOUT, RECIEVE_BUFFER, AUTOMATISE_RESPONSE_RECIEVER)

    def connect(self, host: str = "192.168.10.1", port: int = 8889) -> None:
        """
        Permet d'effectuer une communication entre le client et le drône

        :param host: Adresse hôte du drone
        :param port: Port du drone
        :return: None
        """
        super().connect(host, port)

    def bind(self, host: str = "0.0.0.0", port: int = 9000) -> None:
        """
        Permet d'affecter un port d'écoute pour recevoir des données provenant du drône

        :param host: Nom d'hôte du client
        :param port: Port d'écoute du client
        :return: None
        """
        super().bind(host, port)

    def sendCommand(self, command: ModCmd.TelloCommandInterface, parameters: dict[str, str] = None) -> str:
        """
        Permet d'envoyer une commande spécifique au drône

        :param command: Commande spécifique au drône
        :param parameters: Dictionnaire de paramètres nécessaire pour exécuter la commande
        :return: Réponse de la commande envoyée
        """
        return super().sendCommand(command, parameters)

    def sendRawCommand(self, command: str) -> str:
        """
        Permet d'envoyer une commande sous forme de chaîne de caractères

        :param command: Commande à envoyer au drône
        :return: Si la commande a été envoyé au drône
        """
        return super().sendRawCommand(command)

    def getResponses(self) -> list[ModCom.Response]:
        """
        Permet de récupérer la liste des réponses reçu de la part du client par le drône

        :return: Liste des réponses
        """
        return super().getResponses()

    def getServices(self) -> ModProv.ServiceProvider:
        """
        Permet de récupérer le système de gestion de services

        :return: Gestionnaire de service
        """
        return super().getServices()

    def getThread(self) -> ModProv.ThreadProvider:
        """
        Permet de récupérer le système de gestion de processus

        :return: Gestionnaire de processus
        """
        return super().getThread()

    def recievedResponse(self) -> bool:
        """
        Permet de récupérer la dernière réponse reçu au moment de l'envoie d'une commande au drône

        :return: Si la réponse a été récupérée
        """
        return super().recievedResponse()
