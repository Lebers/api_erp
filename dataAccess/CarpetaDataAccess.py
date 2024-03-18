# dataAccess/CarpetaDataAccess.py
import mysql.connector
from functions.db import Database
from models.carpeta import Carpeta as CarpetaModel, CarpetaInDB
from typing import List, Tuple
from datetime import date


class CarpetaDataAccess:
    def carpeta_exists(self, codigo: str):
        db = Database()
        try:
            db.connect()
            query = "SELECT COUNT(*) FROM carpetas WHERE code = %s AND is_delete IS NULL"
            result = db.execute_query(query, (codigo,))
            return result[0]['COUNT(*)'] > 0
        finally:
            db.disconnect()

    def carpeta_exists_by_id(self, carpeta_id: int):
        db = Database()
        try:
            db.connect()
            query = "SELECT COUNT(*) FROM carpetas WHERE id = %s AND is_delete IS NULL"
            result = db.execute_query(query, (carpeta_id,))
            return result[0]['COUNT(*)'] > 0
        finally:
            db.disconnect()

    def create_carpeta(self, carpeta: CarpetaModel):
        db = Database()
        try:
            db.connect()
            if self.carpeta_exists(carpeta.code):
                return None, None, 400, "Carpeta code already exists"
            query = "INSERT INTO carpetas (caja_id, code, createDate, createUser, is_delete) VALUES (%s, %s, NOW(), %s, NULL)"
            db.execute_query(query, (carpeta.caja_id, carpeta.code, carpeta.createUser))
            db.connection.commit()
            return db.cursor.lastrowid, None, 200, "Carpeta created"
        finally:
            db.disconnect()

    def update_carpeta(self, carpeta_id: int, carpeta: CarpetaModel):
        db = Database()
        try:
            db.connect()
            if not self.carpeta_exists_by_id(carpeta_id):
                return None, None, 404, "Carpeta ID does not exist"
            query = "UPDATE carpetas SET caja_id = %s, code = %s, updateDate = NOW(), updateUser = %s WHERE id = %s AND is_delete IS NULL"
            db.execute_query(query, (carpeta.caja_id, carpeta.code, carpeta.updateUser, carpeta_id))
            db.connection.commit()
            return carpeta_id, None, 200, "Carpeta updated"
        finally:
            db.disconnect()

    def get_carpeta_by_id(self, carpeta_id: int):
        db = Database()
        try:
            db.connect()
            query = "SELECT * FROM carpetas WHERE id = %s AND is_delete IS NULL"
            result = db.execute_query(query, (carpeta_id,))
            if result:
                return CarpetaInDB(**result[0]), None, 200, "Carpeta retrieved"
            return None, None, 404, "Carpeta not found"
        finally:
            db.disconnect()

    def get_all_carpetas(self):
        db = Database()
        try:
            db.connect()
            query = "SELECT * FROM carpetas WHERE is_delete IS NULL"
            result = db.execute_query(query)
            carpetas = [CarpetaInDB(**row) for row in result]
            return carpetas, None, 200, "Carpetas retrieved"
        finally:
            db.disconnect()

    def delete_carpeta(self, carpeta_id: int,user:str):
        db = Database()
        try:
            db.connect()
            query = "UPDATE carpetas SET is_delete = TRUE, deleteDate = NOW(), deleteUser = %s WHERE id = %s"
            db.execute_query(query,   (user,carpeta_id,)) 
            db.connection.commit()
            return None, 200, "Carpeta deleted"
        finally:
            db.disconnect()

    def carpeta_exists_by_code(self, code: str):
        db = Database()
        try:
            db.connect()
            query = "SELECT COUNT(*) FROM carpetas WHERE code = %s AND is_delete IS NULL"
            result = db.execute_query(query, (code,))
            return result[0]['COUNT(*)'] > 0 if result and 'COUNT(*)' in result[0] else False

        except mysql.connector.Error as e:
            print("Error checking carpeta existence by code:", e)
            return False
        finally:
            db.disconnect()

    def get_all_carpetas_by_caja_id(self, caja_id: int):
        db = Database()
        try:
            db.connect()
            query = "SELECT * FROM carpetas WHERE caja_id = %s AND is_delete IS NULL"
            result = db.execute_query(query, (caja_id,))
            carpetas = [CarpetaInDB(**row) for row in result]
            if not carpetas:
                return carpetas, 0, 200, "No hay carpetas asociadas a esta caja"
            return carpetas, 0, 200, "Carpetas retrieved by caja ID"
        except mysql.connector.Error as e:
            print("Error retrieving carpetas by caja ID:", e)
            return [], 500, "Internal server error"
        finally:
            db.disconnect()

    def get_total_carpetas_by_caja_id(self, caja_id: int) -> int:
        db = Database()
        try:
            db.connect()
            query = "SELECT COUNT(*) FROM carpetas WHERE caja_id = %s AND is_delete IS NULL"
            result = db.execute_query(query, (caja_id,))
            return result[0]['COUNT(*)'] if result else 0
        finally:
            db.disconnect()

    def get_carpetas_by_fecha(self, fecha_inicio: date, fecha_fin: date):
        db = Database()
        try:
            db.connect()
            query = """
                SELECT * FROM carpetas
                WHERE createDate BETWEEN %s AND %s
                AND is_delete IS NULL
            """
            result = db.execute_query(query, (fecha_inicio, fecha_fin))
            carpetas = [CarpetaInDB(**data) for data in result]
            return carpetas
        except mysql.connector.Error as e:
            self.log_error(db, e)
            return []
        finally:
            db.disconnect()


