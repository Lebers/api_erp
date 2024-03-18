# functions/db.py
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def execute_query(self, query, params=None):
        self.connect()  # Asegura que la conexión está abierta
        self.cursor.execute(query, params)
        if query.strip().upper().startswith("SELECT"):
            result = self.cursor.fetchall()
            return result
        self.connection.commit()  # Asegura hacer commit para operaciones de escritura

    def disconnect(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.connection is not None:
            self.connection.close()
