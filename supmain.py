from superhero import superhero

Superman = superhero("Superman", "Clark Kent", "flying", "Lex Luthor")

Batman = superhero("Batman","Bruce Wayne", "using genius intelect", "The joker")

Spiderman = superhero("Spiderman", "Peter Parker", "climbing walls and shooting webs", "the Green Goblin")

Wonderwoman = superhero("Wonderwoman", "Diana Prince", "using Super strength", "Cheetah")

Superman.introduce()
Batman.introduce()
Spiderman.introduce()
Wonderwoman.introduce()

print(Spiderman.arch_enemy)