class Environment:
    def __init__(self, width, height, food_spawn, initial_food_density):
        self.width = width
        self.height = height
        self.foods = []
        self.food_spawn = food_spawn
        self.initial_food_density = initial_food_density