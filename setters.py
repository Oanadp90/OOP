from person import Person

def set_new_name(self,person_name): #set method to change the name 
     self.name = person_name 

katy = Person("Katy", 31, "short")
katy.introduce()

katy.set_new_name("Oana") #Object method()

print(katy.name)
