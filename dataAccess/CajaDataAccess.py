import mysql.connector
from functions.db import Database
from models.caja import Caja as CajaModel
from models.caja import CajaInDB
from datetime import date
from models.caja import Cajaxxx

class CajaDataAccess:
    def log_error(self, db, error):
        error_message = str(error)
        try:
            db.connect()
            query = "INSERT INTO logs (message, created_at) VALUES (%s, NOW())"
            db.cursor.execute(query, (error_message,))
            db.connection.commit()   
            log_id = db.cursor.lastrowid
            return log_id
        except mysql.connector.Error as e:
            print(f"Error logging to database: {e}")
            return None
        finally:
            db.disconnect()

    def caja_exists(self, codigo: str):
        db = Database()
        try:
            db.connect()
            query = "SELECT COUNT(*) FROM cajas WHERE code = %s AND is_delete IS NULL"
            result = db.execute_query(query, (codigo,))
            return result[0]['COUNT(*)'] > 0
        except mysql.connector.Error as e:
            print("Error-checking caja existence:", e)
            return False
        finally:
            db.disconnect()

    def caja_exists_by_id(self, caja_id: int):
        db = Database()
        try:
            db.connect()
            query = "SELECT COUNT(*) FROM cajas WHERE id = %s AND is_delete IS NULL"
            result = db.execute_query(query, (caja_id,))
            return result[0]['COUNT(*)'] > 0
        except mysql.connector.Error as e:
            print("Error-checking caja existence by id:", e)
            return False
        finally:
            db.disconnect()

    def create_caja(self, caja: CajaModel):
        db = Database()
        codigo = caja.code
        try:
            query = "INSERT INTO cajas (code, createDate, createUser, is_delete,amount) VALUES (%s, NOW(), %s, NULL,%s)"
            db.execute_query(query, (codigo, caja.createUser,caja.amount))
            db.connection.commit()
            return db.cursor.lastrowid, None, None
        except mysql.connector.Error as e:
            log_id = self.log_error(db, e)
            return None, log_id, 500
        finally:
            db.disconnect()

    def update_caja(self, caja_id: int, caja: CajaModel):
        query = "UPDATE cajas SET code = %s, updateDate = NOW(), updateUser = %s WHERE id = %s AND is_delete IS NULL"
        values = (caja.code, caja.updateUser, caja_id)
        try:
            db = Database()
            db.execute_query(query, values)
            db.connection.commit()
            return caja_id, None, 200
        except mysql.connector.Error as e:
            log_id = self.log_error(db, e)
            return None, log_id, 500
        finally:
            db.disconnect()

    def get_all_cajas(self):
        db = Database()
        try:
            db.connect()
            query = """
                SELECT 
                    c.id, 
                    c.code, 
                    c.createDate, 
                    (SELECT name  FROM users WHERE username = c.createUser) AS createUser, 
                    c.updateDate, 
                    c.updateUser, 
                    c.deleteDate, 
                    c.deleteUser, 
                    c.is_delete,
                    CASE
                        WHEN c.amount != 0 THEN c.amount
                        ELSE COUNT(cf.id)
                    END AS amount
                FROM 
                    cajas c
                LEFT JOIN
                    carpetas cf ON c.id = cf.caja_id
                WHERE 
                    c.is_delete IS NULL 
                GROUP BY 
                    c.id, 
                    c.code, 
                    c.createDate,
                    c.createUser, 
                    c.updateDate, 
                    c.updateUser, 
                    c.deleteDate, 
                    c.deleteUser, 
                    c.is_delete,
                    c.amount
                ORDER BY 
                    c.id DESC
            """
            result = db.execute_query(query)
            cajas = []
            if result:
                for caja_data in result:
                    # Asegúrate de que el modelo CajaInDB pueda manejar el campo 'total' correctamente
                    caja = CajaInDB(**caja_data)
                    cajas.append(caja)
                return cajas, None, None
            return [], None, 404
        except mysql.connector.Error as e:
            log_id = self.log_error(db, e)
            return None, log_id, 500
        finally:
            db.disconnect()

    def get_caja_by_id(self, caja_id: int):
        db = Database()
        try:
            db.connect()
            query = "SELECT * FROM cajas WHERE id = %s AND is_delete IS NULL"
            result = db.execute_query(query, (caja_id,))
            if result:
                caja_data = result[0]
                return CajaInDB(**caja_data), None, 200
            return None, None, 404
        except mysql.connector.Error as e:
            log_id = self.log_error(db, e)
            return None, log_id, 500
        finally:
            db.disconnect()

    def delete_caja(self, caja_id: int, user: str):
        db = Database()
        try:
            db.connect()
            query = "UPDATE cajas SET is_delete = TRUE, deleteDate = NOW(), deleteUser = %s WHERE id = %s AND is_delete IS NULL"
            db.execute_query(query,   (user,caja_id,)) 
            db.connection.commit()
            return None, 200, "Caja borrada"
        except mysql.connector.Error as e:
            log_id = self.log_error(db, e)
            return log_id, 500, "Error al borrar caja"
        finally:
            db.disconnect()

    def get_cajas_by_fecha(self, fecha_inicio: date, fecha_fin: date):
        db = Database()
        try:
            db.connect()
            query = """
                SELECT 
                    c.id, 
                    c.code, 
                    c.createDate, 
                    (SELECT name  FROM users WHERE username = c.createUser) AS createUser, 
                    c.updateDate, 
                    c.updateUser, 
                    c.deleteDate,  
                    c.deleteUser, 
                    c.is_delete,
                    CASE
                        WHEN c.amount != 0 THEN c.amount
                        ELSE COUNT(cf.id)
                    END AS amount
                FROM 
                    cajas c
                LEFT JOIN
                    carpetas cf ON c.id = cf.caja_id  AND cf.is_delete IS NULL
                    
                WHERE 
                    c.createDate >= %s AND c.createDate < DATE_ADD(%s, INTERVAL 1 DAY)
                    AND c.is_delete IS NULL
                     
                    
                GROUP BY 
                    c.id, c.code, c.createDate, c.createUser,  c.updateDate, c.updateUser, c.deleteDate, c.deleteUser, c.is_delete
            """
            result = db.execute_query(query, (fecha_inicio, fecha_fin))
            cajas = []
            if result:
                for caja_data in result:
                    caja = Cajaxxx(**caja_data)
                    cajas.append(caja)
                return cajas
        except mysql.connector.Error as e: 
            self.log_error(db, e)
            return []
        finally:
            db.disconnect()