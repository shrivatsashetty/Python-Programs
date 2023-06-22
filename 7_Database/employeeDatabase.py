import mysql.connector as sql
class Database:
    def __init__(self):
        self.db = sql.connect(
            host="localhost",
            user="1rv21mc052",
            password="1rv21mc052",
            database="employee",
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.db.cursor()
    

emp = Database()

    