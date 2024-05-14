import sqlite3
import requests    

class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS USERS(
        full_name TEXT,
        telegram_id NUMBER unique );
              """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())


    def add_user(self, telegram_id:int, full_name:str):

        sql = """
        INSERT INTO Users(telegram_id, full_name) VALUES(?, ?);
        """
        self.execute(sql, parameters=(telegram_id, full_name), commit=True)


    def select_all_users(self):
        sql = """
        SELECT * FROM Users;
        """
        return self.execute(sql, fetchall=True)


    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE;"
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)


    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE;", commit=True)
    
    def all_users_id(self):
        return self.execute("SELECT telegram_id FROM Users;", fetchall=True)

def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
    
class Sertificate:

    def all_sertificate():
        response = requests.get("https://crm.sifatdev.uz/sertificates/")
        if response.status_code == 200:
            return response.json()
        
    # def get_sertificat():
    def create_certificate(first_name,last_name, middle_name, lavozim, region, tuman, JShShIR, phone_number, course, telegram_id, position):
        url = "https://crm.sifatdev.uz/sertificates/"
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "middle_name": middle_name,
            "lavozim": lavozim,
            "region": region,
            "tuman": tuman,
            "JSHSHR": JShShIR,
            "phone_number": phone_number,
            "course": course,
            "telegram_id": telegram_id,
            "position": position
        }
        response = requests.post(url, json=payload)
        print(response.json())
        
        # Check if the request was successful
        # print(response.status_code)
        if response.status_code == 201:
            return "Muvaffaqiyatli ro'yhatdan o'tdingiz"
        else:
            return f"Siz ro'yhatdan o'tgansiz"



def all_groups_ids():
    response = requests.get("https://crm.sifatdev.uz/groups/")
    ids = [i.get("telegram_id") for i in response.json()]
    return ids

class AuthDatabase:
    def __init__(self, path_to_db="auth.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        
        data = None
        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY,
            phone TEXT UNIQUE,
            password TEXT
        );
        """
        self.execute(sql, commit=True)

    def add_user(self, id: int, password: str, phone: str):
        sql = """
        INSERT INTO Users(id, password, phone) VALUES(?, ?, ?);
        """
        self.execute(sql, parameters=(id, password, phone), commit=True)

    def check(self, id: int, phone: str, password: str):
        sql = """
        SELECT * FROM Users WHERE id = ? AND phone = ? AND password = ?;
        """
        user_data = self.execute(sql, parameters=(id, phone, password), fetchone=True)
        if user_data:
            return True  
        else:
            return False  
