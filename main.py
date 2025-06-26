from os import path
from domain.dataset_csv import DatasetCSV
from domain.dataset_excel import DatasetExcel
from data.data_saver import DataSaver

# Ruta de archivos
csv_path = path.join(path.dirname(__file__), "files/produccion-de-carne-bovina.csv")
excel_path = path.join(path.dirname(__file__), "files/Datos_de_servicio.xlsx")

# Cargar y transformar
csv = DatasetCSV(csv_path)
csv.cargar_datos()
csv.mostrar_resumen()
csv.proceso_datos()

#excel= DatasetExcel(excel_path)
#excel.cargar_datos()
#excel.limpiar_datos()
#excel.mostrar_resumen()


# guardar en base de datos
db = DataSaver()
db = db.guardar_dataframe(csv.datos, "produccion")
#db = db.guardar_dataframe(excel.datos, "datos")