import random

swarmalikas = [
    ["Sa", "Re", "Ga", "Ma", "Pa"],
    ["Re", "Ma", "Pa", "Ni", "Dh"],
    ["Re", "Ga", "Re", "Sa", "Ma"]
]

def fitness(swarmalika):
    high_notes = ["Sa", "Re", "Ga"]
    low_notes = ["Ma", "Pa", "Ni", "Dh"]
    return sum(1 for note in swarmalika if note in high_notes)

def crossover(swarmalika1, swarmalika2):
    split_point = random.randint(1, len(swarmalika1) - 1)
    new_swarmalika = swarmalika1[:split_point] + swarmalika2[split_point:]
    return new_swarmalika

def mutate(swarmalika):
    index = random.randint(0, len(swarmalika) - 1)
    if swarmalika[index] in ["Sa", "Re", "Ga"]:
        swarmalika[index] = random.choice(["Sa", "Re", "Ga"])
    else:
        swarmalika[index] = random.choice(["Ma", "Pa", "Ni", "Dh"])
    return swarmalika

population = [random.choice(swarmalikas) for _ in range(10)]

generations = 1000
for _ in range(generations):
    
    fitness_values = [fitness(swarmalika) for swarmalika in population]

    
    if any(fitness_value >= 3 for fitness_value in fitness_values):
        break

    selected_population = [population[i] for i in range(len(population)) if fitness_values[i] >= 3]
    new_population = []
    for _ in range(len(population)):
        parent1 = random.choice(selected_population)
        parent2 = random.choice(selected_population)
        new_swarmalika = crossover(parent1, parent2)
        new_population.append(new_swarmalika)

    for i in range(len(new_population)):
        if random.random() < 0.1:
            new_population[i] = mutate(new_population[i])

    population = new_population

best_swarmalika = max(population, key=lambda x: fitness(x))
print("Best Swarmalika:", best_swarmalika)
print("Fitness:", fitness(best_swarmalika))
