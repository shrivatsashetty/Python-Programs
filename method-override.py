class Employee:
	#increment=1.5 times base pay
	def __init__(self,name,age,salary):
		self.name=name
		self.age=age
		self.salary=salary
	def info(self):
		print(f"name:{self.name} age:{self.age} starting pay:{self.salary}")
	def promotion(self):
		self.salary*=1.5
		print(f"salary after increment:{self.salary}")
class Developer(Employee):
	# increment = 2.5 times base pay
	def promotion(self):
		self.salary*=2.5
		print(f"salary after increment:{self.salary}")
class Manager(Employee):
	#incr=3.5 times base
	def promotion(self):
		self.salary*=3.5
		print(f"salary afte increment:{self.salary}")
while True:
	print(f"1.Employee\n2.Developer\n3.Manager\n4.exit")
	ch=int(input("Enter a choice:"))
	if ch==1:
		e1=Employee(name=input("Enter name:"),age=int(input("Enter age")),salary=float(input("Enter salary:")))
		e1.info()
		e1.promotion()
	elif ch==2:
		d1=Developer(name=input("Enter name:"),age=int(input("Enter age")),salary=float(input("Enter salary:")))
		d1.info()
		d1.promotion()
	elif ch==3:
		m1=Manager(name=input("Enter name:"),age=int(input("Enter age")),salary=float(input("Enter salary:")))
		m1.info()
		m1.promotion()
	elif ch==4:
		break
