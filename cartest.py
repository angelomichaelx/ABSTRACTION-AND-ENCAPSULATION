#import 
from carclass import Car

#create class for testcar
class testcar:
    def testingcar(self): 

#car object
        car = Car(2022, "Dodge", 0)

#result
        #car info
        print("<=>" * 5)
        print("YEAR:", car.get_yearmodel())
        print("MODEL:", car.get_make())
        print("SPEED:", car.get_speed())
        print("<=>" * 5)
        print()
        
        #accelerate       
        print("\033[1;32mAccelerating *BROOM*")
        #acceleraion 1st call
        print("\033[1;32mCurrent Speed:", car.get_speed())
        #acceleraion 2nd call
        car.accelerate()
        print("\033[1;32mCurrent Speed:", car.get_speed())
        #acceleraion 3rd call
        car.accelerate()
        print("\033[1;32mCurrent Speed:", car.get_speed())
        #acceleraion 4th call
        car.accelerate()
        print("\033[1;32mCurrent Speed:", car.get_speed())
        #acceleraion 5th call
        car.accelerate()
        print("\033[1;32mCurrent Speed:", car.get_speed())   
        print()
        
        #brake 
        print("\033[93mBraking")
        #braking 1st call
        car.brake()
        print("\033[93mCurrent Speed:", car.get_speed())
        #braking 2nd call
        car.brake()
        print("\033[93mCurrent Speed:", car.get_speed())
        #braking 3rd call
        car.brake()
        print("\033[93mCurrent Speed:", car.get_speed())
        #braking 4th call
        car.brake()
        print("\033[93mCurrent Speed:", car.get_speed())
        #braking 5th call
        car.brake()
        print("\033[93mCurrent Speed:", car.get_speed())

# Instance to run cartest
run = testcar()
run.testingcar()