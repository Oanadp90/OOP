class superhero():
    def __init__(self, superhero_name, secret_identity, super_power, arch_enemy):
        self.name = superhero_name
        self.identity = secret_identity
        self.power = super_power
        self.arch_enemy = arch_enemy

        
    def introduce(self):
        print(f"My name is {self.name}, I am {self.identity} while i am at work but when my help i needed I am {self.power} to save the world from {self.arch_enemy}!")

    

