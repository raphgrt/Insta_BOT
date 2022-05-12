from password import * # Mes mots de passes
from typing import Dict
from Anniversaire import Anniversaire
from instagrapi import Client
from instagrapi.types import UserShort
from time import sleep
from json import load,decoder,dumps
import os

#Const :

ACCOUNT_SETTINGS = './ig_settings.json'
MP_INFO_DICT = './Les_MPS.json'
BIRTHDAY_PATH = './Anniversaires.json'
MESSAGE_HISTORY = './Message_History.json'
DEFAULT_MESSAGE = "Bonjour, je suis un BOT Autonome fais  !help   pour en savoir plus !"
COMMAND_PREFIX = '!'


class LeBot():
    client = None
    def __init__(self) -> None:
        super().__init__()
        self.client = Client()
        self.les_followers = 0
        self.birthday_events = Anniversaire(BIRTHDAY_PATH)
        #Récupère les paramètres si ils éxistent et se connecte
        if os.path.exists(ACCOUNT_PASSWORD):
            self.client.load_settings(ACCOUNT_SETTINGS)
            self.client.login(ACCOUNT_USERNAME,ACCOUNT_PASSWORD)
        else:
            self.client.login(ACCOUNT_USERNAME,ACCOUNT_PASSWORD)
            self.client.dump_settings(ACCOUNT_SETTINGS)
        
        # Données:
        self.message_liste = []
        self.message_nonlus = []
        self.MP_infos = self.__Read_data(MP_INFO_DICT)
        self.historique_message = self.__Read_data(MESSAGE_HISTORY)
        
    def __Read_data(self,data) -> dict:
        """Ouvre et enregistre le contenant Json dans le dico
        """
        try:
            with open(data) as file:
                return load(file)
        except decoder.JSONDecodeError:
            return {}
    
    def __Write_data(self,data) -> None:
        with open(data,'w') as file:
            file.write(dumps(self.MP_infos))
    
    def __Save_messages(self,identifiant,message) -> None:
        if identifiant in self.historique_message:
            self.historique_message[identifiant].append(message)
        else:
            self.historique_message[identifiant] = message
        self.__Write_data(self.historique_message)
    
    def __Save_Dico_ID(self,identifiant,message):
        pass
    
    def Commands(self):
        pass
    
    def Get_followers(self, quantite:int = 0) -> Dict[int, UserShort]:
        return self.client.user_following(self.client.user_id, amount=quantite)
    
    def Get_News_Messages(self) ->None :
        self.message_liste = self.client.direct_threads() # Récupère tout les messages
        self.message_nonlus = self.client.direct_threads(selected_filter='unread') #Récupère les messages non lus seulement
        
        #Transformer le merdier d'informations de l'api pour garder les valeurs intéressantes
        if len(self.message_nonlus) != 0:
            for utilisateurs_diff in self.message_nonlus:
                les_infos_messages = utilisateurs_diff.messages[0]
                
                # Enregistrer les ID dans le dico pour gagner en rapidité
                if not(les_infos_messages.id) in self.MP_infos:
                    self.MP_infos[les_infos_messages.id] = utilisateurs_diff.users[0].username
                message_recu = (self.MP_infos[les_infos_messages.id],les_infos_messages.text)
                print(message_recu)
                
                #Réponde aux commandes
                if message_recu[0].startswith('!'):
                    if message_recu[0] == '!anniversaire':
                        # Envoyer un message pour savoir la date
                        self.Send_Message('Envoie moi ta date au format JJ/MM/AAAA')
                        # Tester la date
                        # Répondre en fonction
                        #reponse = self.birthday_events.Donner_une_reponse()
                        ...
                #Repondre aux MP
                elif message_recu[0] == 'Salut':
                    self.Send_Message('Hey !',les_infos_messages)
                #Repondre betement
                else:
                    self.Send_Message(DEFAULT_MESSAGE,les_infos_messages)
        #Enregistrer les datas dans le JSON
        self.__Write_data(MP_INFO_DICT)
    
    def Send_Message(self,message,destination):
        self.client.direct_send(text=message,thread_ids=[destination.thread_id])

    
    def Birthday_set(self,identite):
        #if Anniversaire.__Date_Format()
        ...
    
    def update(self):
        self.Get_followers()
        self.Get_News_Messages()


if __name__ == '__main__':
    bot = LeBot()
    
    while True:
        bot.update()
        sleep(600)
        
