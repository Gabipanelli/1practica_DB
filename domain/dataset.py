from abc import ABC, abstractmethod

class Dataset(ABC):
    def __init__(self, fuente):
        self.__fuente = fuente
        self.__datos = None

    @property
    def datos(self):
        return self.__datos
    
    @datos.setter
    def datos(self, value):
        #validaciones
        self.datos = value

    @abstractmethod
    def Cargar_datos(self):
        pass

    def Validar_datos(self):
        pass

    def Transformar_datos(self):
        pass

    def mostrar_resumen(self):
        pass

