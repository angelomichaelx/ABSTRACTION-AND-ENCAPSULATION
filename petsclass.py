#create pet class
class Pet:
    #constructor
    def __init__(self, nameofpet, typeofpet, ageofpet):
        self.name = nameofpet
        self.type = typeofpet
        self.age = ageofpet

    def get_name(self):
        return self.name
    def set_name(self, nameofpet):
        self.name = nameofpet

    def get_type(self):
        return self.type
    def set_type(self, typeofpet):
        self.type = typeofpet

    def get_age(self):
        return self.age
    def set_age(self, ageofpet):
        self.age = ageofpet





