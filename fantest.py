from fanclass import Fan

class testfan:
    def runtest(self):
#two fans
        #Fan 1
        fan1 = Fan(Fan.FAST, True, 10, "Yellow")
        #Fan 2
        fan2 = Fan(Fan.MEDIUM, False, 5, "Blue")

#First fan properties
        print("=" * 15)
        print("\033[1mFAN NUMBER 1\033[0m") 
        print("=" * 15) 
        print("\033[93mFan 1 - Speed:", fan1.get_speed(), "\033[0m")
        print("\033[93mFan 1 - On:", fan1.is_on(), "\033[0m")
        print("\033[93mFan 1 - Radius:", fan1.get_radius(), "\033[0m")
        print("\033[93mFan 1 - Color:", fan1.get_color(), "\033[0m")
        
        print("")
#Second fan properties
        print("=" * 15)
        print("\033[1mFAN NUMBER 2\033[0m")
        print("=" * 15)
        print("\033[94mFan 2 - Speed:", fan2.get_speed(), "\033[0m")
        print("\033[94mFan 2 - On:", fan2.is_on(), "\033[0m")
        print("\033[94mFan 2 - Radius:", fan2.get_radius(), "\033[0m")
        print("\033[94mFan 2 - Color:", fan2.get_color(), "\033[0m")
        

# Instance to run testfan 
test = testfan()
test.runtest()