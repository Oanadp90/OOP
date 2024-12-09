from person import Person

Liam = Person("Liam", 30, "Tall") # Liam is the object we create, it was constructed from the Person class with: name, age, and we defined the specifics when we asked for Liam object to be built.

Oana = Person ("Oana", 20, "Tall")

print(f"My name is {Oana.name}, I am {Oana.age} and I am {Oana.height}")


class Person():
    def __init__(self, person_name):
        self.name = person_name

print(Liam.height) #liam.height is a method to bring out our objects properties

print(Liam.age)

print(Oana.age)

print(Oana.name)

print(Oana.height)

# print(Liam) this will print: <person.Person object at 0x000001951197CCD0> and it won't give us what we need, which is why we need to use a method in order to acces the information from our object 



