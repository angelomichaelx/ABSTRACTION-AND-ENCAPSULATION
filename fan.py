# Create fan class
class Fan: 
#3 constants(Slow, Medium and Fast)
    SLOW = 1
    MEDIUM = 2
    FAST = 3

#constructor
    def __init__(self, speed = SLOW, on = False, radius = 5, color = "blue"):

            self.__speed = speed
            self.__on = on 
            self.__radius = radius
            self.__color = color

#methods

    def get__speed(self):
          return self.__speed
    
    def set_speed(self, speed):
          self.__speed = speed

    def set_on(self):
          return self.__on

    def set_on(self, on):
          self.__on = on

    def set_radius(self):
          return self.__radius

    def set_radius(self, radius):
          self.__radius = radius
    
    def set_color(self):
          return self.__color

    def set_color(self, color):
          self.__color = color
    
    
    
    
    


          
