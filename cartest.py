#import 
from carclass import Car

#create class for testcar
class testcar:
    def testingcar(self): 

#car object
        car = Car(2022, "Dodge", 0)

#result
        #car info
        print("=" * 15)
        print("YEAR:", car.get_yearmodel())
        print("MODEL:", car.get_make())
        print("SPEED:", car.get_speed())
        print("=" * 15)
        print()
        

run = testcar()
run.testingcar()