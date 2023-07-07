#create pet class
class pet:
    #constructor
    def __init__(self, nameofpet, typeofpet, ageofpet):
        self.name = nameofpet
        self.type = typeofpet
        self.age = ageofpet

    def get_name(self):
        return self.name
    def set_name(self, nameofpet):
        self.name = nameofpet
        