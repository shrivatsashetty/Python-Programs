def decorator_function(div):
    def smart_div(a,b): 
        print(f"The user wanted {a}/{b}")
        if(a<b):
            a,b=b,a
        print(f"The function gives {a}/{b}")
        result=div(a,b)
        print(result)
        return result
    return smart_div
    

@decorator_function
def div(a,b):
    return a/b
div(27,3)
div(2,8)
