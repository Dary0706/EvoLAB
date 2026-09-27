class Organism:
    def __init__(self, oragnism_id, diet, speed, vision, metabolism, gender, max_energy, energy, lifespan, x, y):
        self.oragnism_id = oragnism_id

        self.diet = diet #predator, herbivorous, omnivorous

        self.speed = speed
        self.vision = vision
        self.metabolism = metabolism

        self.max_energy = max_energy
        self.energy = energy

        self.lifespan = lifespan
        self.age = 0

        self.gender = gender

        self.x = x
        self.y = y