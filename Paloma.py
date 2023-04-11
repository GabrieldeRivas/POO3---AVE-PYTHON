from Logger import Logger
from Ave import Ave

class Paloma(Ave):
    def __init__(self, nombre):
        super().__init__(nombre)

    def defecar(self):
        if self.hayEnergiaPara(1):
            self.energia -= 1
            Logger.showInfo(self.nombre + " defecó.")
        else:
            Logger.showError(self.nombre + " no tiene suficiente energía para poder defecar.")
    