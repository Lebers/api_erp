import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error
from datetime import datetime

# Carga las variables de entorno del archivo .env
load_dotenv()

def obtener_esquema_db():
    try:
        conexion = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.execute("SHOW TABLES")
            tablas = cursor.fetchall()
            
            esquema = ""
            for tabla in tablas:
                esquema += f"Tabla: {tabla[0]}\n"
                cursor.execute(f"SHOW CREATE TABLE {tabla[0]}")
                create_table_stmt = cursor.fetchone()
                esquema += f"{create_table_stmt[1]};\n\n"
            
            return esquema
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión a MySQL cerrada")

def encontrar_ultimo_archivo(directorio):
    archivos = [os.path.join(directorio, f) for f in os.listdir(directorio)]
    archivos = [f for f in archivos if os.path.isfile(f)]
    archivos.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    return archivos[0] if archivos else None

def comparar_esquemas(esquema_actual, archivo_comparacion):
    with open(archivo_comparacion, 'r') as file:
        esquema_anterior = file.read()

    if esquema_actual == esquema_anterior:
        print("Los esquemas son iguales.")
    else:
        print("Los esquemas son diferentes.")

directorio = 'db/backups'
esquema_actual = obtener_esquema_db()
archivo_comparacion = encontrar_ultimo_archivo(directorio)

if archivo_comparacion:
    print(f"Comparando con el archivo más reciente: {archivo_comparacion}")
    comparar_esquemas(esquema_actual, archivo_comparacion)
else:
    print("No se encontró archivo de esquema anterior para comparar.")
