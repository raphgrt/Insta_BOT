import threading
from main import LeBot

class commands(LeBot,threading.Thread):
    def __init__(self) -> None:
        super().__init__()
        self.attribut = '!'
        
    def __Attr_Auto_Detect(self,text:str) ->bool:
        assert type(text) != str, "Type Error : Entrée STR"
        return True if text.startswith(self.attribut) else False
    
    
    def Detect_command(text):
        pass
    
    def Anniversaire(self):
        ...
    
    

if __name__ == '__main__':
    pass