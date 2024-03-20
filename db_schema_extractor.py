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
            
            # Agregar las funciones almacenadas al esquema
            cursor.execute("SHOW FUNCTION STATUS WHERE Db = %s", (os.getenv('DB_NAME'),))
            funciones = cursor.fetchall()
            for funcion in funciones:
                esquema += f"Función: {funcion[1]}\n"
                cursor.execute(f"SHOW CREATE FUNCTION {funcion[1]}")
                create_function_stmt = cursor.fetchone()
                esquema += f"{create_function_stmt[2]};\n\n"

            return esquema
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión a MySQL cerrada")

def guardar_esquema_a_archivo(esquema, directorio):
    if not os.path.exists(directorio):
        os.makedirs(directorio)

    fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"{directorio}/esquema_db_{fecha_hora}.sql"

    with open(nombre_archivo, 'w') as file:
        file.write(esquema)
    print(f"Esquema guardado en: {nombre_archivo}")

esquema = obtener_esquema_db()
guardar_esquema_a_archivo(esquema, 'db/backups')
