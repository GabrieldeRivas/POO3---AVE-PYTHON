class Logger:
    modo = "INFO"
    
    @classmethod
    def getModo(log):
        return log.modo

    @classmethod
    def setModo(log, nuevoModo):
        if nuevoModo == "INFO" or nuevoModo == "WARN" or nuevoModo == "ERROR":
            log.modo = nuevoModo
        else:
            Logger.showError("El modo no es válido. Los modos posibles son: INFO, WARN y ERROR.")

    @staticmethod
    def showInfo(mensaje):
        if Logger.modo == "INFO":
            print("INFO: " +  mensaje)

    @staticmethod
    def showWarn(mensaje):
        if Logger.modo == "INFO" or Logger.modo == "WARN":
            print("WARN: " + mensaje)

    @staticmethod
    def showError(mensaje):
        print("ERROR: " + mensaje)