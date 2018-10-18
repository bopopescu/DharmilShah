class automobile:

    def __init__(self,car_name,seat):
        self.name = car_name
        self.rno = seat
        self.topspeed = self.topspeed()

    def show(self):
        print(self.car_name, self.seat)
        self.topspeed.show()

    class topspeed:
        def __init__(self):
            self.speed = 210
        def show(self):
            print(self.speed)






car_name = input('enter the car name : ')
seat = int(input('enter the seat : '))


a1 = automobile(car_name,seat)
t1 = automobile.topspeed()
print(t1.show())


