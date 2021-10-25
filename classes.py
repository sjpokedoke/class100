class Car(object):
    def __init__(self, colour, brand, model, speedlimit, weight):
        self.colour = colour
        self.brand = brand
        self.model = model
        self.speedlimit = speedlimit
        self.weight = weight
    
    def start(self):
        print('the car has started')
    
    def stop(self):
        print('the car has stopped')
    
    def accelarate(self, speedlimit):
        print('the car is accelerating at')
        print(speedlimit)
    
car1 = Car("red", "toyota", "drs", 90, 1200)

print(car1.accelarate(car1.speedlimit))