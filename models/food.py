import random
class Food(object):
    def __init__(self, name, energy, diet, environment):
        self.name = name
        self.energy = energy
        self.diet = diet

        self.x = random.randint(0, environment.width - 5)
        self.y = random.randint(0, environment.height - 5)