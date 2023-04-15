class Robot:
    def __init__(self,age):
        self.num=age+1
        print("Hello","self.num = argument passed +1 i.e",self.num,"arguments passed was",age)
old=int(input("Enter age of robo:"))
bot1=Robot(old)