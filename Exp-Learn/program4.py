from Dunder import *
obj1=Dunder()
obj2=Dunder()
obj1.accept(obj2)

while True:
	print("1.Add\n2.Sub\n3.Div\n4.Mul\n5.Less Than\n6.Less Than Equal to\n7.Greater than\n8.Greater than equal to\n9.Equal to\n10.Not equal to\n")
	ch=int(input("Enter Choice\n"))
	if ch==1:
		obj1+obj2
	elif ch==2:
		obj1-obj2
	elif ch==3:
		obj1//obj2
	elif ch==4:
		obj1*obj2
	elif ch==5:
		obj1<obj2
	elif ch==6:
		obj1<=obj2
	elif ch==7:
		obj1>obj2
	elif ch==8:
		obj1>=obj2
	elif ch==9:
		obj1==obj2
	elif ch==10:
		obj1!=obj2
	else:
		break
