from abc import ABC, abstractmethod


class Dataset(ABC):
    def __init__(self, fuente):
        self.__fuente = fuente
        self.__datos = None

    @property
    def datos(self):
        # procesar
        return self.__datos

    @datos.setter
    def datos(self, value):
        # validaciones
        self.__datos = value

    @property
    def fuente(self):
        return self.__fuente

    @abstractmethod
    def cargar_datos(self):
        pass

    def validar_datos(self):
        if self.datos is None:
            raise ValueError("Datos no cargados")

        if self.datos.isnull().sum().sum() > 0:
            print("Se encontraron datos faltantes en el excel")
        if self.datos.duplicated().sum() > 0:
            print("Hay filas duplicadas en archivo")
        return True

    def transformar_datos(self):
        if self.datos is not None :
            self.__datos.columns = self.datos.columns.str.upper().str.replace(" ", "_")
            self.__datos = self.datos.drop_duplicates()
            print("Transformación de datos completada")
        else:
            print("Error al trasnformar datos, asegurarse de tener datos cargados.")

    def mostrar_resumen(self):
        #print(self.datos.head())
        print(self.datos.tail())
        #print(self.datos.describe())