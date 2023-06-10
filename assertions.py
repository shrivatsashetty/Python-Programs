n = input("Enter a number:")
try:
    assert float(n) > 10, " Enter a number greater than 10"
    print("Allright\nyour value :",n)
except Exception as e:
    print("Error:",e)

print("========End=========")    


