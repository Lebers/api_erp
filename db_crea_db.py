import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

# Obtener variables de entorno para la configuración de la base de datos
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'moduloInventario')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'moduloInventario')
DB_NAME = 'moduloInventario'  # Base de datos a crear

def create_database():
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.close()
    connection.close()

def connect_to_database():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def execute_queries(queries, connection):
    cursor = connection.cursor()
    for query in queries.split(';'):
        if query.strip():
            cursor.execute(query)
    connection.commit()
    cursor.close()

def main():
    # Crear la base de datos si no existe
    create_database()

    # Conectar a la base de datos
    connection = connect_to_database()

    # SQL para crear tablas y insertar datos iniciales
    sql_commands = """
    CREATE TABLE `cajas` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `code` varchar(255) NOT NULL,
      `createDate` datetime NOT NULL,
      `createUser` varchar(255) DEFAULT NULL,
      `updateDate` datetime DEFAULT NULL,
      `updateUser` varchar(255) DEFAULT NULL,
      `deleteDate` datetime DEFAULT NULL,
      `deleteUser` varchar(255) DEFAULT NULL,
      `is_delete` tinyint(1) DEFAULT '0',
      `amount` int(11) NOT NULL DEFAULT '0',
      PRIMARY KEY (`id`),
      UNIQUE KEY `codigo` (`code`)
    ) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

    CREATE TABLE `carpetas` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `caja_id` int(11) NOT NULL,
      `code` varchar(250) NOT NULL,
      `createDate` datetime DEFAULT CURRENT_TIMESTAMP,
      `createUser` varchar(50) DEFAULT NULL,
      `updateDate` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
      `updateUser` varchar(50) DEFAULT NULL,
      `deleteDate` datetime DEFAULT NULL,
      `deleteUser` varchar(50) DEFAULT NULL,
      `is_delete` tinyint(1) DEFAULT '0',
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

    CREATE TABLE `logs` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `message` longtext NOT NULL,
      `created_at` timestamp NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=MyISAM AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;

    CREATE TABLE `users` (
      `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id auto incrementeble',
      `name` varchar(250) NOT NULL,
      `username` varchar(200) NOT NULL,
      `password` varchar(500) NOT NULL,
      `createDate` timestamp NOT NULL,
      `createUser` varchar(100) DEFAULT NULL,
      `updateDate` timestamp NULL DEFAULT NULL,
      `is_delete` tinyint(1) DEFAULT NULL,
      `deleteDate` timestamp NULL DEFAULT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

    INSERT INTO `users` (name, username, password, createDate)
    VALUES('super usuario', 'root', '$2b$12$e/wiKrh5enwQk306ccXQJOjkVQ.SSGbQb6dGaZQQjdi7CV/zNgeE6', NOW());
    """

    # Ejecutar SQL para crear tablas y insertar el primer usuario
    execute_queries(sql_commands, connection)

    # Cerrar la conexión
    connection.close()

if __name__ == '__main__':
    main()
