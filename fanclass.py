# Create fan class
class Fan: 
            
#3 constants(Slow, Medium and Fast)
      SLOW = 1
      MEDIUM = 2
      FAST = 3

#constructor
      def __init__(self, speed = SLOW, on = False, radius = 5, color = "blue"):

            self.speed = speed
            self.on = True
            self.radius = radius
            self.color = color

#methods

      def get_speed(self):
            return self.speed
            
      def set_speed(self, speed):
            self.speed = speed

      def is_on(self):
            return self.on

      def set_on(self, on):
            self.on = on

      def get_radius(self):
            return self.radius

      def set_radius(self, radius):
            self.radius = radius
            
      def get_color(self):
            return self.color

      def set_color(self, color):
            self.color = color
            
    
    
    
    


          
