import mysql.connector
try:
    connection = mysql.connector.connect(host="localhost",user="siri",password="Shrivatsa@307",database="STUDENTS",auth_plugin="my_sql_native_password")
    cur = connection.cursor()

    create="CREATE TABLE IF NOT EXISTS MCA (USN VARCHAR(10) PRIMARY KEY, Name VARCHAR(50), Semester INT, Marks INT );"
    cur.execute(create)
    connection.commit()

    insert=""" INSERT INTO MCA (USN, Name, Semester, Marks ) VALUES(%s,%s,%s,%s); """
    print("Enter Student details")
    student_info=(input("Enter USN:"),input("Enter Name:"),int(input("Enter sem:")),float(input("Enter marks:")) )
    cur.execute(insert,student_info)
    connection.commit()

    def display_details():
        select="SELECT * FROM MCA"

        cur.execute(select)
        results=cur.fetchall()
        connection.commit()
        for data in results:
            print(data)

    display_details()

    print("Update operation")
    update="UPDATE MCA SET Marks=%s WHERE USN=%s;"
    student_info=(float(input("enter new marks:")),input("Enter USN of student to update"))
    cur.execute(update,student_info)
    connection.commit()
    print("Udate Successful")

    display_details()

    delete="DELETE FROM MCA WHERE USN = %s ;"
    target=(input("Enter USN to delete: "),)
    cur.execute(delete,target)
    connection.commit()
    print("Deletion successful")

    display_details()

except Exception as e:
    print("Error:",e)

