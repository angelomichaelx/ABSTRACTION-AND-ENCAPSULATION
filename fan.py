# Create fan class
class Fan: 
#3 constants(Slow, Medium and Fast)
    SLOW = 1
    MEDIUM = 2
    FAST = 3

#constructor
    def __init__(self, speed = SLOW, on = False, radius = 5, color = "blue"):
