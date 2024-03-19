import os
import mysql.connector
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Obtener las credenciales y datos de conexión de las variables de entorno
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

# Función para leer las instrucciones SQL de creación de tablas
def read_sql_file(sql_file_path):
    with open(sql_file_path, 'r', encoding='utf-8') as file:
        return file.read().split(';')

# Función para conectar a la base de datos y ejecutar las instrucciones SQL
def create_tables(sql_instructions, db_host, db_user, db_password, db_name):
    try:
        # Conectar a MySQL sin seleccionar una base de datos específica
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password
        )
        cursor = connection.cursor()
        # Crear la base de datos si no existe
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`")
        print(f"Base de datos '{db_name}' verificada o creada exitosamente.")
        connection.commit()

        # Conectar a la base de datos específica
        connection.database = db_name

        # Ejecutar las instrucciones de creación de tablas
        for instruction in sql_instructions:
            if 'CREATE TABLE' in instruction:
                cursor.execute(instruction)
                print(f"Tabla creada exitosamente: {instruction.split(' ')[2]}")
        connection.commit()

        # Insertar los datos en la tabla `users`
        insert_query = """
        INSERT INTO `users` (`id`, `name`, `username`, `password`, `createDate`, `updateDate`, `is_delete`, `deleteDate`) VALUES
        (3, 'root', 'root', '$2b$12$dP972PGDV1q74/Jg0vUO4emSZ3/Lu8cj2WeDs/ZtmC7QnWvIxlGnq', '2024-03-19 07:21:19', NULL, NULL, NULL);
        """
        cursor.execute(insert_query)
        connection.commit()
        print("Datos insertados en la tabla `users` exitosamente.")
        
    except mysql.connector.Error as error:
        print(f"Error al crear las tablas o la base de datos: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a la base de datos cerrada.")

# Ejemplo de uso
sql_file_path = 'scr/moduloinventario.sql'
sql_instructions = read_sql_file(sql_file_path)
create_tables(sql_instructions, db_host, db_user, db_password, db_name)
