from os import path
from domain.dataset_csv import DatasetCSV
from domain.dataset_excel import DatasetExcel
from data.data_saver import DataSaver

# Ruta de archivos
csv_path = path.join(path.dirname(__file__), "files/ipc-chaco-historico.csv")
excel_path = path.join(path.dirname(__file__), "files/Datos_de_servicio.xlsx")

# Cargar y transformar
csv = DatasetCSV(csv_path)
csv.cargar_datos()
csv.mostrar_resumen()

excel= DatasetExcel(excel_path)
excel.cargar_datos()
excel.limpiar_datos()
excel.mostrar_resumen()


# guardar en base de datos
db = DataSaver()
#db = db.guardar_dataframe(csv.datos, "ipc_chaco_historico")
db = db.guardar_dataframe(excel.datos, "datos")