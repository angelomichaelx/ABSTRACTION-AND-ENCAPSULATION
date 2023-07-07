#import
from petsclass import Pet

#create petttest class
class pettest:
    #define class 
    def pet_test():

#input name of pet
        name = input("\033[93mEnter the name of your pet: ")
#input type of pet
        type = input("\033[93mEnter the type of your pet: ")
#input age of pet
        age = input("\033[93mEnter the age of your pet: ")
        pet = Pet(name, type, age)

#print output
        print()
        print("<=>" * 8)
        print("YOUR PET IDENTIFICATION")
        print("<=>" * 8)
        print()

#information output
        print("\033[94m#" * 15)
        print("\033[94mPet Name:", pet.get_name())
        print("\033[94mType:", pet.get_type())
        print("\033[94mAge:", pet.get_age())
        print("#" * 15)



# Instance to run pettest
run = pettest
run.pet_test()