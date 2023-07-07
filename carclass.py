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
        