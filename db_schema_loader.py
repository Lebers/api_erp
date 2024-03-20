import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# Carga las variables de entorno del archivo .env
load_dotenv()

def ejecutar_script_sql(archivo, host, user, password, database):
    try:
        conexion = mysql.connector.connect(host=host, user=user, password=password, database=database)
        
        with open(archivo, 'r') as file:
            script_sql = file.read()
            # Utilizamos el cursor en modo multi para ejecutar múltiples sentencias
            cursor = conexion.cursor()
            for result in cursor.execute(script_sql, multi=True):
                if result.with_rows:
                    print(result.fetchall())
                else:
                    print(f"{cursor.rowcount} row(s) affected.")
            conexion.commit()
        print(f"Script {archivo} ejecutado con éxito.")
    except Error as e:
        print(f"Error al ejecutar el script SQL: {e}")
    finally:
        if conexion.is_connected():
            conexion.close()

def encontrar_ultimo_archivo(directorio):
    archivos = [os.path.join(directorio, f) for f in os.listdir(directorio)]
    archivos = [f for f in archivos if os.path.isfile(f)]
    archivos.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    return archivos[0] if archivos else None

directorio = 'db/backups'
archivo_a_cargar = encontrar_ultimo_archivo(directorio)

if archivo_a_cargar:
    print(f"Cargando el archivo más reciente: {archivo_a_cargar}")
    ejecutar_script_sql(
        archivo_a_cargar,
        os.getenv('DB_HOST'),
        os.getenv('DB_USER'),
        os.getenv('DB_PASSWORD'),
        os.getenv('DB_NAME')
    )
else:
    print("No se encontró archivo de esquema para cargar.")
