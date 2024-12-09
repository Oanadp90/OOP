class Person():
    def __init__(self, person_name, person_age, person_height):
        self.name = person_name
        self.age = person_age
        self.height = person_height

    def introduce(self):
     print(f"My name is {self.name}, I am {self.age} and I am {self.height}")


    def set_new_name(self,person_name): #set method to change the name 
     self.name = person_name 


    def set_hair_colour(self, hair_colour):
       self.hair_colour = hair_colour









