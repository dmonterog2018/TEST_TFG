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

    