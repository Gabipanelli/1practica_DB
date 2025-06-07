from os import path
from domain.dataset_csv import DatasetCSV
from domain.dataset_excel import DatasetExcel

# Ruta de archivos
csv_path = path.join(path.dirname(__file__), "files/ipc-chaco-historico.csv")
excel_path =path.join(path.dirname(__file__), "files/Datos_de _servicio.xlsx")

# Cargar y transformar
csv = DatasetCSV(csv_path)
csv.cargar_datos()

excel= DatasetExcel(excel_path)
excel.cargar_datos()

# guardar en base de datos