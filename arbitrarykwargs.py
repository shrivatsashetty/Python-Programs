
def display_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} is {value}")
    # print(kwargs.items)

display_info(name="Raman",age=25,native="Bangalore",job="Software Engineer")
display_info(name="Radha",age=27)
display_info(name="Prashanth",age=26,job="Mechanic")
display_info() # no args taken, nothing printed

