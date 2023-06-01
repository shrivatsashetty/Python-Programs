import mysql.connector

class Mydatabase:
 def __init__(self):
  self.db=mysql.connector.connect(host="localhost",user="siri",password="Shrivatsa@307",database="EMPLOYEES",auth_plugin="mysql_native_password")
  self.cur=self.db.cursor()
  self.createTable()

 def  createTable(self):
  query=""" CREATE TABLE IF NOT EXISTS STUDENTS (SAP_ID VARCHAR(10) PRIMARY KEY,
                                                 NAME VARCHAR(20),
                                                 ADDRESS VARCHAR(20),
                                                 MARKS INT(20) ) """ 
  
  
  self.cur.execute(query)
  self.db.commit()
  


 def insertdata(self,sapid,name,add,marks):
  query = "INSERT INTO STUDENTS(SAP_ID,NAME,ADDRESS,MARKS) VALUES(%s,%s,%s,%s)"
  values=(sapid,name,add,marks)
  self.cur.execute(query,values)
  self.db.commit()
  print("data inserted")


 def modifydata(self,sapid,marks):
  query="UPDATE STUDENTS SET MARKS=%s WHERE SAP_ID=%s"
  values=(marks,sapid)
  self.cur.execute(query,values)
  self.db.commit()
  print("data  updated")


 def deletedata(self,sapid):
  query=f"DELETE FROM STUDENTS WHERE SAP_ID='{sapid}'"
  self.cur.execute(query)
  self.db.commit()
  print("data deleted")


 def showdata(self):
  query="SELECT * FROM STUDENTS"
  self.cur.execute(query)
  data=self.cur.fetchall()
  for i in data:
   print(i)


s=Mydatabase()

while True:
 print("1.Insert\n2.Show\n3.Delete\n4.Update\n0.Exit")
 ch=int(input("Enter your choice"))

 if ch==1:
  sapid=input("Enter sapid")
  name=input("Enter name")
  add=input("Enter address")
  marks=int(input("Enter marks"))
  s.insertdata(sapid,name,add,marks)

 elif ch==2:
  s.showdata()

 elif ch==3:
  sapid=input("Enter sapid")
  s.deletedata(sapid)

 elif ch==4:
  sapid=input("Enter sapid")
  marks=int(input("Enter updated marks"))
  s.modifydata(sapid,marks)

 elif ch==0:
  print("Exit")
  break
  
 else:
  print("invalid")
  break
