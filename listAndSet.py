while(True):
	print("1.List Opeations \n 2.Set Operations")
	ch=int(input("enter your choice"))
	if(ch==1):
		while(True):
			list1=[5,1,3,2,4]
			list2=[6,9,7,8,10]
			print("1.concatination \n  2.Length \n 3.append \n 4.Repeatation \n 5.slicing \n 6.clear \n 7.reverse \n 8.sort \n 9.remove \n 10.insert")
			ch1=int(input("enter your choice "))
			if(ch1==1):
				print(f"concatination of {list1} and {list2} = ",list1+list2)
			elif(ch1==2):
				print(f"Length of {list1} = ",len(list1))
			elif(ch1==3):
				app=int(input("enter element to append"))
				list2.append(app)
				print(list)
			elif(ch1==4):
				no=int(input("enter number"))
				print(f"repeatation of {list2}  {no} times = ",no*list2)
			elif(ch1==5):
				s=int(input("enter starting index "))
				e=int(input("enter ending index "))
				print("slicing {list2} from {s} to {e} = ",list2[s:e])
			elif(ch1==6):
				print(f"{list1} after clear = ",list2.clear())
			elif(ch1==7):
				list2.reverse()
				print(list2)
			elif(ch1==8):
				list1.sort()
				print(list1)
			elif(ch1==9):
				rm=int(input("enter value to remove"))
				print(f"removing {rm} from {list2} = ")
				list2.remove(9)
				print(list2)
			elif(ch1==10):
				iin=int(input("enter value to insert "))
				list1.insert(2,iin)
				print(list1)
			else:
				break
	elif(ch==2):
		while(True):
			set1={1,3,4,5,2}
			set2={6,8,7,9}
			print("1.size \n 2.length of set \n 3.union \n 4.intersection \n 5.difference of set \n 6.symmetric difference \n.7 check for element \n 8.pop \n 9.deletion \n 10.remove ")
			ch2=int(input("enter your choice "))
			if(ch2==1):
				print(f"size of {set1} = ",set1.__sizeof__())
			elif(ch2==2):
				print(f"length of {set2} = ",len(set2))
			elif(ch2==3):
				print(set1.union(set2))
			elif(ch2==4):
				print(set1.intersection(set2))
			elif(ch2==5):
				print(set1.difference(set2))
			elif(ch2==6):
				print(set1^set2)
				print(set1)
			elif(ch2==7):
				nu=int(input("enter element "))
				print(f"is {nu} in {set1} = ",set1.__contains__(10))
			elif(ch2==8):
				print("pop operation = ",set2.pop())
			elif(ch2==9):
				print("clear operation ")
				set1.clear()
				print(set1)
			elif(ch2==10):
				print(set2)
				num=int(input("enter element to remove "))
				print(f"removing {num} from {set2} = ",set2.remove(num))
			else:
				break
	else:
		exit()
