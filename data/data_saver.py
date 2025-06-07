import sqlite3 
import pandas as pd 

class DataSaver:
    def __init__(self, db_path):
        self.__db_patch = db_path

    def guardar_dataframe(self, df, nombre_tabla):
        if df is None:
            print("No se pudo guardar: datos vacios en {nombre_tabla}")
            return
        
        if not isinstance(df, pd.DataFrame):
            print(f"Se esperaba un DataFrame y se recibió un {type(df)}.")
            return
        
        try:
            conn = sqlite3.connect(self.__db_patch)
            df.to_sql(nombre_tabla, conn, if_exists="replace", index=False)
            conn.close()
            print(f"Datos guardados en tabla: {nombre_tabla}")

        except Exception as e:
            print("Error al guardar datos en DB")