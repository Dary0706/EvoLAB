from models import organism
from models.organism import Organism
from models.species import Species
from models.environment import Environment
from models.food import Food
import random

environment = Environment(500, 500, food_spawn=0.07, initial_food_density=0.07,)
for i in range(int(environment.width*environment.height*0.001)):
    f = Food(
        name="food",
        energy=int(random.randint(0,20)),
        diet="omnivorous",
        environment=environment,
    )
    environment.foods.append(f)

species_biba = Species(name = "Biba",)

species_list = [species_biba]

biba1 = Organism(
    organism_id=1,
    diet='herbivorous',
    speed=2,
    vision=15,
    metabolism=1.0,
    max_energy=100,
    energy=50,
    lifespan=5,
    gender='notable',
    environment=environment,
)
biba2 = Organism(
    organism_id=2,
    diet='herbivorous',
    speed=2,
    vision=15,
    metabolism=1.0,
    max_energy=100,
    energy=50,
    lifespan=50,
    gender='notable',
    environment=environment,
)

species_biba.organisms.append(biba1)
species_biba.organisms.append(biba2)



for spec in species_list:
    print(f"name: {spec.name}\ngeneration: {spec.generation}\norganisms: {len(spec.organisms)}\n")

tick = 0
b = int(input("1 - шаг, 0 - закончить: "))
while b != 0:
    tick += 1


    if random.random() < environment.initial_food_density:
        f = Food(
            name="food",
            energy=int(random.randint(0, 20)),
            diet="omnivorous",
            environment=environment,
        )


    for spec in species_list:
        spec.organisms = [
            organism for organism in spec.organisms
            if organism.alive
        ]
        for org in spec.organisms:
            org.step(environment)
        for org in spec.organisms:
            print(f"Тик: {tick}\n{spec.name} {org.organism_id}\nx: {org.x}\ny: {org.y}\nenergy: {org.energy}\nage: {org.age}\norganisms: {len(spec.organisms)}\n")


    print(f"Foods: {len(environment.foods)}")
    b = int(input("1 - шаг, 0 - закончить: "))



