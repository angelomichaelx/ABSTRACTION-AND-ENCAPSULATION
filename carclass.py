# Create car class
class Car:
    #constructor
    def __init__(self, yearmodel, make, speed = 0 ):
        self.year = yearmodel
        self.make = make
        self.speed = speed

    #Methods
    def get_yearmodel(self):
        return self.year 
    def set_yearmodel(self, yearmodel):
        self.year = yearmodel

    def get_make(self):
        return self.make
    def set_make(self, make):
        self.make = make

    def get_speed(self):
        return self.speed
    def set_speed(self, speed):
        self.speed = speed