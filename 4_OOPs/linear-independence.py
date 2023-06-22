# Program to check linear independence of two vectors

def independence_check(vector1,vector2,flag=0):
    
    if len(vector1)!=len(vector2):
        print("The dimensions are unequal and hence\nThe Vectors are linearly independent")
        return True
    
    ratios=[]
    for i in range (len(vector1)):
        ratios.append(vector1[i]/vector2[i])
        
    print("ratios of corresponding components:\n",ratios)

    for i in range(len(ratios)):
        if (ratios[i]!=ratios[0]):
            print("vectors are linearly Independent ")
            return True
            
        
        else:
            flag=0

    if flag==0:
        print("The Vectors are linearly dependent")
        return False
    

v1=[]; v2=[]
n1=int(input("Enter dimension of vector 1: "))
for i in range(n1):
    element=float(input("Enter vector components: "))
    v1.append(element) 

n2=int(input("Enter dimension of vector 2 :"))
for i in range(n2):
    element=float(input("Enter vector components: "))
    v2.append(element)

print(f"Vectors are\n{v1}\n{v2}")   

independence_check(v1,v2)
