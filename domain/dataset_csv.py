import pandas as pd
from domain.dataset import Dataset


class DatasetCSV(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):
        try:
            df = pd.read_csv(self.fuente)
            self.datos = df
            print("El CSV se cargo correctamente")
            if self.validar_datos():
                print("Se encontraron datos validos en CSV")
                self.transformar_datos()
        except Exception as e:
            print(f"Error al cargar CSV: {e}")