import random
from typing import List, Tuple

class Item:
    def __init__(self, name: str, weight: int, value: int):
        self.name = name
        self.weight = weight
        self.value = value

class Individual:
    def __init__(self, chromosome: List[int], items: List[Item], capacity: int):
        self.chromosome = chromosome
        self.items = items
        self.capacity = capacity
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self) -> int:
        total_weight = sum(g * item.weight for g, item in zip(self.chromosome, self.items))
        total_value = sum(g * item.value for g, item in zip(self.chromosome, self.items))
        if total_weight > self.capacity:
            return 0
        return total_value

    def mutate(self, mutation_rate: float):
        for i in range(len(self.chromosome)):
            if random.random() < mutation_rate:
                self.chromosome[i] = 1 - self.chromosome[i]
        self.fitness = self.calculate_fitness()

def crossover(parent1: Individual, parent2: Individual) -> Individual:
    point = random.randint(1, len(parent1.chromosome) - 2)
    new_chromosome = parent1.chromosome[:point] + parent2.chromosome[point:]
    return Individual(new_chromosome, parent1.items, parent1.capacity)

def selection(population: List[Individual]) -> Individual:
    tournament = random.sample(population, k=3)
    return max(tournament, key=lambda ind: ind.fitness)

def generate_initial_population(items: List[Item], capacity: int, size: int) -> List[Individual]:
    population = []
    for _ in range(size):
        chromosome = [random.randint(0, 1) for _ in items]
        population.append(Individual(chromosome, items, capacity))
    return population

def genetic_algorithm(items: List[Item], capacity: int, generations: int, population_size: int, mutation_rate: float) -> Tuple[Individual, int]:
    population = generate_initial_population(items, capacity, population_size)
    best = max(population, key=lambda ind: ind.fitness)

    for generation in range(generations):
        new_population = []
        for _ in range(population_size):
            parent1 = selection(population)
            parent2 = selection(population)
            child = crossover(parent1, parent2)
            child.mutate(mutation_rate)
            new_population.append(child)
        population = new_population
        current_best = max(population, key=lambda ind: ind.fitness)
        if current_best.fitness > best.fitness:
            best = current_best

    return best, best.fitness

if __name__ == "__main__":
    items = [
        Item("Laptop", 3, 2000),
        Item("Headphones", 1, 250),
        Item("Coffee Mug", 1, 50),
        Item("Notepad", 2, 300),
        Item("Smartphone", 1, 1500),
        Item("Book", 2, 500)
    ]
    capacity = 5
    best_solution, best_value = genetic_algorithm(
        items, capacity, generations=100, population_size=30, mutation_rate=0.05
    )

    print("Best solution value:", best_value)
    for gene, item in zip(best_solution.chromosome, items):
        if gene:
            print(f" - {item.name} (value: {item.value}, weight: {item.weight})")