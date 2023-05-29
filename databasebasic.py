import mysql.connector
try:
    connection_object = mysql.connector.connect(user='SIRI',password='Shrivatsa@307',database='EMPLOYEES',auth_plugin="mysql_native_password")

    cursor_object = connection_object.cursor()

    create_table_query = """CREATE TABLE IF NOT EXISTS infosys (id INT PRIMARY KEY, name VARCHAR (40), age INT, email VARCHAR(50))"""

    cursor_object.execute(create_table_query)

    insert_query=""" INSERT INTO infosys (id, name, age, email) VALUES (%s ,%s, %s, %s) """

    employee_data=(1,'Harish', 27, 'harish@gmail.com')

    cursor_object.execute(insert_query,employee_data)

    connection_object.commit()

    select_query=""" SELECT * FROM  infosys  """

    cursor_object.execute(select_query)
    result=cursor_object.fetchall()
    for entries in result:
        print(entries)

    cursor_object.close()
    connection_object.close()
except Exception as e:
    print("Error",e)
