from models import organism
from models.organism import Organism
from models.species import Species
from models.environment import Environment
from models.food import Food

species_biba = Species(name = "Biba",)
biba1 = Organism(
    oragnism_id=1,
    diet='herbivorous',
    speed=2,
    vision=15,
    metabolism=1.0,
    max_energy=100,
    energy=50,
    lifespan=5,
    x=0.0,
    y=0.0,
    gender='notable'
)
biba2 = Organism(
    oragnism_id=1,
    diet='herbivorous',
    speed=2,
    vision=15,
    metabolism=1.0,
    max_energy=100,
    energy=50,
    lifespan=5,
    x=0.0,
    y=0.0,
    gender='notable'
)

species_biba.organisms.append(biba1)
species_biba.organisms.append(biba2)

print(f"name: {species_biba.name}\ngeneration: {species_biba.generation}\norganisms: {len(species_biba.organisms)}")



