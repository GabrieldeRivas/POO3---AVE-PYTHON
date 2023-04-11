from Logger import Logger
from Ave import Ave
import random

class Golondrina(Ave):
    def __init__(self, nombre, costoPesca):
        super().__init__(nombre)
        self.costoPesca = costoPesca

    def logroPescar(self):
        rand = random.uniform(0, 1)
        return rand < 0.1
    
    def pescar(self):
        if self.hayEnergiaPara(self.costoPesca):
            self.energia -= self.costoPesca
            if self.logroPescar():
                self.energia += 10
                Logger.showInfo(self.nombre + " tuvo éxito en la pesca.")
            else:
                Logger.showWarn(self.nombre + " no logró pescar.")
        else:
            Logger.showError(self.nombre + " no tiene suficiente energía para pescar.")
    
