import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error
from datetime import datetime

# Carga las variables de entorno del archivo .env
load_dotenv()

def ejecutar_migraciones(directorio, host, user, password, database):
    conexion = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conexion.cursor(buffered=True)

    # Crear las tablas de control de migraciones si no existen, con campos LONGTEXT para SQL y mensajes de error
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sys_migration_control (
            filename VARCHAR(255),
            applied_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            sql_text LONGTEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sys_failed_migrations (
            filename VARCHAR(255),
            error_message LONGTEXT,
            failed_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conexion.commit()

    archivos_migracion = [f for f in sorted(os.listdir(directorio)) if os.path.isfile(os.path.join(directorio, f))]

    for archivo in archivos_migracion:
        ruta_archivo = os.path.join(directorio, archivo)
        print(f"Procesando migración: {archivo}")

        with open(ruta_archivo, 'r') as file:
            script_sql = file.read()

        try:
            for result in cursor.execute(script_sql, multi=True):
                if result.with_rows:
                    result.fetchall()
            conexion.commit()

            cursor.execute("INSERT INTO sys_migration_control (filename, sql_text) VALUES (%s, %s)", (archivo, script_sql))
            conexion.commit()
            print(f"Migración {archivo} ejecutada con éxito.")

            processed_filename = archivo + "_" + datetime.now().strftime("%Y%m%d%H%M%S")
            os.rename(ruta_archivo, os.path.join(directorio, "processed", processed_filename))

        except Error as e:
            print(f"Error al aplicar {archivo}: {e}")
            cursor.execute("INSERT INTO sys_failed_migrations (filename, error_message) VALUES (%s, %s)", (archivo, str(e)))
            conexion.commit()

            failed_filename = archivo + "_" + datetime.now().strftime("%Y%m%d%H%M%S")
            os.rename(ruta_archivo, os.path.join(directorio, "failed", failed_filename))

    cursor.close()
    conexion.close()

def main():
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_NAME')
    directorio_migraciones = 'db/migrations'

    # Crear subdirectorios para migraciones procesadas y con fallos si no existen
    for sub_dir in ['processed', 'failed']:
        os.makedirs(os.path.join(directorio_migraciones, sub_dir), exist_ok=True)

    ejecutar_migraciones(directorio_migraciones, host, user, password, database)

if __name__ == "__main__":
    main()
    