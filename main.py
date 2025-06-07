from os import path
from domain.dataset_csv import DatasetCSV

# Ruta de csv 
csv_path = path.join(path.dirname(__file__), "files/ipc-chaco-historico.csv")

# Cargar y Transformar 
csv = DatasetCSV(csv_path)
csv.cargar_datos
# Guardar en base de datos

