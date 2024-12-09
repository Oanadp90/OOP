class superhero():
    def __init__(superhero_name, secret_identity, super_power, arch_enemy):
        superhero.name = superhero_name
        superhero.identity = secret_identity
        superhero.power = super_power
        superhero.arch_enemy = arch_enemy

    def introduce(Superman):
        print(f"My name is {superhero.name}, I am {superhero.identity} while i am at work but when my help i needed I am {superhero.power} to save the world from {superhero.arch_enemy}")
    def introduce(Batman):
        print(f"My name is {superhero.name}, I am {superhero.identity} by day and whenever {superhero.arch_enemy} is causing troubles, i use my {superhero.identity} to save the world")
    def introduce(Spiderman):
        print("My name is {superhero.name}, I am {superhero.identity} while at work but when there is trouble, i {superhero.power} to find out what {superhero.arch_enemy} did")
    def introduce(Wonderwoman):
        print("My name is {superhero.name}, I am {superhero.identity} during the day and i use {superhero.power} to face my enemy {superhero.arch_enemy}")   


Superman = ("Superman", "Clark Kent", "flying", "Lex Luthor")

Batman = ("Batman", "Bruce Wayne", "genius intellect", "Joker")

Spiderman = ("Spiderman", "Peter Parker", "crawl the walls", "Green Goblin")

Wonderwoman= ("Wonderwoman", "Diana Prince", "Super strength", "Cheetah")