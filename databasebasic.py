import mysql.connector

try:
    connection_object = mysql.connector.connect(user='siri',password='Shrivatsa@307',database='EMPLOYEES',auth_plugin="mysql_native_password")

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

    choice=input("Enter choice:")
    if (int(choice) == 1):
        update_query="""UPDATE infosys SET age = %s, email=%s WHERE id=%s """
        updated_age=30
        updated_email="harish@example.com"
        emp_id=1
        cursor_object.execute(update_query,(updated_age,updated_email,emp_id))
        connection_object.commit()
        print("update operation sucessfull")
        
        cursor_object.execute(select_query)
        updated_result=cursor_object.fetchall()
        for entries in updated_result:
            print(entries)
    
    elif(int(choice)==2):
        delete_query="delete from infosys where id = %s ; "
        emp_id=1
        cursor_object.execute(delete_query,(emp_id,)) 
        # values must be passed as tuple only, here (emp_id,) is a tuple with single element
        connection_object.commit()
        print("Entry deleted")
    
    elif(int(choice)==3):
        employee_data=(2,'Bharath', 32, 'bharath@gmail.com')
        cursor_object.execute(insert_query,employee_data)
        connection_object.commit()
        cursor_object.execute(select_query)
        updated_result=cursor_object.fetchall()
        print("Insertion sucessfull")
        for entries in updated_result:
            print(entries)

    else:
        pass
    
    cursor_object.close()
    connection_object.close()

except Exception as e:
    print("Error",e)
