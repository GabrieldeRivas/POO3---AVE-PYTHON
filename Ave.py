from Logger import Logger
class Ave:
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 2

    def comer(self, gramos):
        self.energia += gramos
        Logger.showInfo(self.nombre + " comió " + str(gramos) + " gramos.")

    def volar(self, kms):
        if self.hayEnergiaPara(kms * 3):
            self.energia -= kms * 3
            Logger.showInfo(self.nombre + " voló " + str(kms) + " kilómetros.")
        else:
            Logger.showError(self.nombre + " no tiene suficiente energía para volar esta distancia.")

    def getEnergia(self):
        return self.energia

    def setEnergia(self, energia):
        self.energia = energia

    def hayEnergiaPara(self, costo):
        return self.energia - costo >= 0