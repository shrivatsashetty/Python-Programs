import mysql.connector as sql
class Database:
    def __init__(self):
        self.db = sql.connect(
            host="localhost",
            user="root",
            password="root",
            database="employee",
            #auth_plugin='mysql_native_password'
        )
        self.cursor = self.db.cursor()
    

emp = Database()

    