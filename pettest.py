#import
from petsclass import Pet

#create petttest class
class pettest:
    #define class 
    def pet_test():

#input name of pet
        name = input("Enter the name of your pet: ")
#input type of pet
        type = input("Enter the type of your pet: ")
#input age of pet
        age = input("Enter the age of your pet: ")
        pet = Pet(name, type, age)

#print output
        print()
        print("<=>" * 8)
        print("YOUR PET IDENTIFICATION")
        print("<=>" * 8)
        print()





# Instance to run pettest
run = pettest
run.pet_test()