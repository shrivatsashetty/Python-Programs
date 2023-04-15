class Rooms:
    lenght=0
    breadth=0
    area=0
    def room_area(self,lenght,breadth):
        self.lenght=lenght
        self.breadth=breadth
        self.area=self.lenght*self.breadth

livingroom=Rooms()
livingroom.lenght=12
livingroom.breadth=10
livingroom.room_area(10,12)
print(f"the area of the room is {livingroom.room_area}")

