import asyncio
from main import LeBot

class Les_Commandes:
    def __init__(self) -> None:
        self.attr = '!'
        
    @staticmethod
    async def Commande_Anniversaire():
        print('Anniversaire')
        await asyncio.sleep(2)
    
    @staticmethod
    async def Dire_bonjour():
        print('Bonjour')


async def main():
    
    # New Line Added
    while True:
        f1 = loop.create_task(Les_Commandes.Commande_Anniversaire())
        f2 = loop.create_task(Les_Commandes.Dire_bonjour())
        await asyncio.wait([f1, f2])
  
# to run the above function we'll 
# use Event Loops these are low
# level functions to run async functions
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()