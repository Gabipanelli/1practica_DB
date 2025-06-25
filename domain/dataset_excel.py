import pandas as pd
from domain.dataset import Dataset


class DatasetExcel(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):
        try:
            df = pd.read_excel(self.fuente)
            self.datos = df
            print("Excel cargado ok")
            if self.validar_datos():
                self.transformar_datos()
        except Exception as e:
            print(f"Error cargando Excel: {e}")
    
    def limpiar_datos(self):
        df = pd.read_excel(self.fuente)
        self.datos = df
        df[['Respondido','Resuelto (S/N)']]= df['Respondido - Resuelto (S/N)'].str.split('-', expand=True)
        df.drop(columns=['Duración de la llamada',"Velocidad de respuesta", "Respondido - Resuelto (S/N)"], axis=1, inplace=True)
        df['Resuelto (S/N)'] = df['Resuelto (S/N)'].astype(bool)
        print(self.datos.info())


