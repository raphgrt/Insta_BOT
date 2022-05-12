from datetime import date as LOCALDATE
from json import dumps,load,decoder
from os import path


class Anniversaire:
    
    def __init__(self, path="Anniversaires.json") -> None:
        self.path = path
        self.dico_personnes = self.__Read_data()

    
    def __Read_data(self) -> dict:
        """Ouvre et enregistre le contenant Json dans le dico
        """
        try:
            with open(self.path) as file:
                return load(file)
        except decoder.JSONDecodeError:
            return {}


    def __UserID_check(self,UserID) -> bool:
        return True if UserID in self.dico_personnes else False
    
    def __Ajouter_utilisateur(self,USER_ID, DATE) -> None:
        self.dico_personnes[USER_ID] = DATE
        # Mettre à jour le fichier JSON et le Dico
        with open(self.path,'w') as file:
            file.write(dumps(self.dico_personnes))
        
    def Donner_une_reponse(self,USER_ID,DATE):
        date_valide = Anniversaire.__Date_Format(DATE)
        if type(date_valide) == str:
            return (date_valide)
        elif self.__UserID_check(USER_ID):
            return 'Tu es déjà dans la base de donnée !'
        else:
            self.__Ajouter_utilisateur(USER_ID,DATE)
            return ('Tu à été enregistrée')
    
    def __repr__(self) -> str:
        return str(self.dico_personnes)

    
    @staticmethod
    def __Date_Format(date:str)->bool:
        """Vérifie une date en entrée 

        Args:
            date ([str]): Date 
        """
        local_date = LOCALDATE.today()
        try:
            if len(date) == 10:
                liste_element = date.split('/')
            try:
                jour = int(liste_element[0])
                Mois = int(liste_element[1])
                Annee = int(liste_element[2])
                assert jour<32 or jour>0, "Day Problem"
                assert Mois >=0 or Mois <12, "Month problem"      
                assert Annee < local_date.year, "Years problem" 
            except TypeError:
                texte_erreur = "TypeError : Can't convert on interable number !"
                return texte_erreur
            except IndexError:
                texte_erreur = 'IndexError : Date Format error ! DD/MM/YYYY required'
                return texte_erreur
            except ValueError:
                texte_erreur = "ValueError : Can't convert in integer !"
                return texte_erreur
            except:
                texte_erreur ="You probably made a mistake, start again"
                return texte_erreur
        except TypeError:
            texte_erreur = 'TypeError : date input is a string value'
            return texte_erreur
        except UnboundLocalError:
            texte_erreur = 'Il faut une DD/MM/YYYY date !'
            return texte_erreur
        else:
            return True

if __name__ == '__main__':
    Les_Anniversaires = Anniversaire()
    Les_Anniversaires.Donner_une_reponse('Raphaël','02/09/2004')
    Les_Anniversaires.Donner_une_reponse('Jean','02/09/2004')
    #Programmation défensive
    assert(Les_Anniversaires.Donner_une_reponse('Raphaël','02/09/2004')) != str, "Doit renvoyer un str car déja dans la Base de donnée"
    assert(Les_Anniversaires.Donner_une_reponse('Raphaël','50/09/2004')) != str, "Doit renvoyer un str car Le jour est invalide"
    assert(Les_Anniversaires.Donner_une_reponse('Raphaël','02/50/2004')) != str, "Doit renvoyer un str car Le mois est invalide"
    assert(Les_Anniversaires.Donner_une_reponse('Raphaël','02/09/aaaa')) != str, "Doit renvoyer un str car l'année est invalide"
    assert(Les_Anniversaires.Donner_une_reponse('Raphaël','##/##/####')) != str, "Doit renvoyer un str car la date ne marche pas"
    assert(Les_Anniversaires.Donner_une_reponse('Raphaël','########')) != str, "Doit renvoyer un str car la date ne marche pas"
    #assert(Anniversaire('./Existe_pas.json')), "Le fichier JSON ne devrait pas exister"
    