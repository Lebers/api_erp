# functions/data_access.py
import mysql.connector
from functions.db import Database
from models.user import User as userModel
from models.user import UserInDB  

class LogDataAccess:
    def log_error(self, error_message: str):
        db = Database()
        try:
            query = "INSERT INTO logs (message, created_at) VALUES (%s, NOW())"
            db.execute_query(query, (error_message,))
            db.connection.commit()
            return db.cursor.lastrowid  # Retorna el ID del log insertado
        except mysql.connector.Error as e:
            print("Error al registrar en logs:", e)
            return None
        finally:
            db.disconnect()

class ModuloInventario_DataAccess:

    def log_error(self, db, error):
        error_message = str(error)
        try:
            db.connect()
            query = "INSERT INTO logs (message, created_at) VALUES (%s, NOW())"
            db.cursor.execute(query, (error_message,))
            db.connection.commit()  # Asegúrate de hacer commit de la transacción
            log_id = db.cursor.lastrowid
            return log_id
        except mysql.connector.Error as e:
            print(f"Error logging to database: {e}")
            return None
        finally:
            db.disconnect()

    def get_user_by_username(self, username: str):
        db = Database()
        try:
            user_records = db.execute_query("SELECT * FROM users WHERE is_delete is null and username = %s", (username,))
            return user_records[0] if user_records else None, None
        except mysql.connector.Error as e:
            log_id = self.log_error(db, e)
            return None, log_id,500
        finally:
            db.disconnect()


    def create_user(self, user: userModel):
        db = Database()
        name = user.name
        username = user.username
        password = user.password
        try:
            # Suponiendo que tienes un campo 'createDate' que debe ser llenado
            query = "INSERT INTO users (name,username, password, createDate) VALUES (%s,%s, %s, NOW())"
            db.execute_query(query, (name,username, password))
            db.connection.commit()
            return db.cursor.lastrowid, None, None
        except mysql.connector.Error as e:
            log_id = self.log_error(e)  # Asegúrate de que log_error devuelve el log_id
            return None, log_id, 500  # Devolver None para user_id, el log_id y status 500
        finally:
            db.disconnect()
    
    def user_exists(self, username: str):
        db = Database()
        try:
            db.connect()
            query = "SELECT COUNT(*) FROM users WHERE username = %s and is_delete is null"
            result = db.execute_query(query, (username,))
            return result[0]['COUNT(*)'] > 0
        except mysql.connector.Error as e:
            print("Error-checking user existence:", e)
            return False
        finally:
            db.disconnect()
    
    def get_all_logs(self):
        db = Database()
        try:
            db.connect()
            query = "SELECT * FROM logs order by id desc"
            logs = db.execute_query(query)
            logs_data = []
            for log in logs:
                log['created_at'] = log['created_at'].isoformat() if log['created_at'] else None
                logs_data.append(log)
            return logs_data
        finally:
            db.disconnect()
    
    def update_user(self, user_id: int, user: userModel):
        query = "UPDATE users SET name = %s, username = %s, password = %s, updateDate=NOW()  WHERE id = %s"
        values = (user.name, user.username, user.password, user_id)
        try:
            db = Database()
            db.execute_query(query, values)
            db.connection.commit()
        except mysql.connector.Error as e:
            print(f"Error updating user: {e}")
            return None
        finally:
            db.disconnect()

    def get_all_users(self):
        db = Database()
        try:
            db.connect()
            query = "SELECT id, username, name, createDate, updateDate FROM users where is_delete is null"
            result = db.execute_query(query)
            users = []
            if result:
                for user_data in result:
                    users.append(UserInDB(**user_data))
                return users, None, None   
            return [], None, 404   
        except mysql.connector.Error as e:
            log_id = self.log_error(e)  
            return None, log_id, 500   
        finally:
            db.disconnect()


    def get_user_by_id(self, user_id: int):
        db = Database()
        try:
            db.connect()
            query = "SELECT id, username, name, createDate,updateDate FROM users WHERE id = %s and is_delete is null"
            result = db.execute_query(query, (user_id,))
            if result:
                user_data = result[0]
                return UserInDB(**user_data),None,None
            return None,None,409
        except mysql.connector.Error as e:
            log_id = self.log_error(e)  # Asegúrate de que log_error devuelve el log_id
            return None, log_id, 500  # Devolver None para user_id, el log_id y status 500
        finally:
            db.disconnect()

 
    def delete_user(self, user_id: int):
        db = Database()
        try:
            db.connect()
            query = "UPDATE users SET is_delete = %s, deleteDate = NOW() WHERE id = %s"
            db.execute_query(query, (True, user_id))
            db.connection.commit()

            return None, 200, "Usuario borrado"
        except mysql.connector.Error as e:
            log_id = self.log_error(db, e)
            return log_id, 500, "Error al realizar el borrado lógico del usuario"
        finally:
            db.disconnect()