# Create car class
class Car:
    #constructor
    def __init__(self, yearmodel, make, speed = 0 ):
        self.year = yearmodel
        self.make = make
        self.speed = speed