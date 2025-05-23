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