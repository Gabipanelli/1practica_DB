import pandas as pd 
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from decouple import config


class DataSaver:
    def __init__(self):
        user = config("DB_USER")
        password = config("DB_PASSWORD")
        host = config("DB_HOST")
        port = config("DB_PORT")
        dabatase = config("DB_NAME")

        url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{dabatase}"
        self.engine = create_engine(url)

    def guardar_dataframe(self, df, nombre_tabla):
        if df is None:
            print("No se pudo guardar: datos vacios en {nombre_tabla}")
            return
        
        if not isinstance(df, pd.DataFrame):
            print(f"Se esperaba un DataFrame y se recibió un {type(df)}.")
            return
        
        try:
           
            df.to_sql(nombre_tabla, con=self.engine, if_exists="replace", index=False)
            print(f"Datos guardados en tabla: {nombre_tabla}")

        except SQLAlchemyError as e:
            print("Error al guardar datos en DB")
            