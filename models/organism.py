import random
import math
class Organism:
    def __init__(self, organism_id, diet, speed, vision, metabolism, gender, max_energy, energy, lifespan, environment):
        self.organism_id = organism_id

        self.diet = diet #predator, herbivorous, omnivorous

        self.speed = speed
        self.vision = vision
        self.metabolism = metabolism

        self.max_energy = max_energy
        self.energy = energy

        self.lifespan = lifespan
        self.age = 0

        self.gender = gender

        self.x = random.randint(0, environment.width)
        self.y = random.randint(0, environment.height)

        self.alive = True

    def step(self, environment):
        nearest = None
        min_distance = self.vision ** 2

        for f in environment.foods:
            d = (f.x - self.x) ** 2 + (f.y - self.y) ** 2

            if d <= self.vision ** 2 and d < min_distance:
                nearest = f
                min_distance = d

        if nearest is not None:
            dx = nearest.x - self.x
            dy = nearest.y - self.y

            d = math.sqrt(dx ** 2 + dy ** 2)

            if d > 2:
                px = (dx / d) * self.speed
                py = (dy / d) * self.speed

                self.x += px
                self.y += py
            else:
                self.energy = min(self.energy + nearest.energy, self.max_energy)
                if self.energy > self.max_energy:
                    self.energy = self.max_energy
                environment.foods.remove(nearest)

        else:
            def random_move():
                a = random.randint(0, 7)
                diagonal_speed = self.speed / math.sqrt(2)

                if a == 0:
                    self.x += self.speed

                elif a == 1:
                    self.x += diagonal_speed
                    self.y -= diagonal_speed

                elif a == 2:
                    self.y -= self.speed

                elif a == 3:
                    self.x -= diagonal_speed
                    self.y -= diagonal_speed

                elif a == 4:
                    self.x -= self.speed

                elif a == 5:
                    self.x -= diagonal_speed
                    self.y += diagonal_speed

                elif a == 6:
                    self.y += self.speed

                elif a == 7:
                    self.x += diagonal_speed
                    self.y += diagonal_speed
            random_move()
        if self.x >= environment.width-5:
            self.x = environment.width-5
        elif self.x <= 5:
            self.x = 5

        if self.y >= environment.height-5:
            self.y = environment.height-5
        elif self.y <= 5:
            self.y = 5

        self.age += 1
        self.energy -= self.metabolism

        if self.age >= self.lifespan or self.energy <= 0:
            self.alive = False
