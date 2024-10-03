"""
    By Armando Canul - 29/09/2024

    A example for simple genetic algorithm (SGA) implementation.
    the problem consist in found the string target
    for example:
    found 'My Genetic Algorithm' from population size: N
    where population is a random string list
"""
import random

# GLOBAL VARIABLES (SETTING AND OTHERS)
GENES = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890_-=;/#@$!&*()<>,.? '
TARGET = 'armando'
CHROMOSOME_LENGTH = len(TARGET)
POPULATION_SIZE = 20

# CLASSES
class Chromosome:
    def __init__(self, length: int) -> None:
        if length != None:
            self.length = length # string length for string info
        self.fitness = -1
    
    def initWithString(self, s: str) -> None:
        self.info = s
        self.length = len(s)
    
    def randomGenes(self) -> None:
        # generate a random string for chromosome info
        self.info = ''
        for i in range(0, self.length):
            self.info += ranGene()
    
    def crossover(self, parent1, parent2, target) -> bool:
        # crossover function
        if self.length != parent1.length and self.length != parent2.length:
            print("can't crossover, parents don't have same length or with this chromosome")
            return False
        ranIndex = int(random.uniform(0.6,1) * self.length) - 1
        child1 = Chromosome(self.length)
        child1.initWithString(parent1.info[:ranIndex] + parent2.info[ranIndex:])
        child2 = Chromosome(self.length)
        child2.initWithString(parent2.info[:ranIndex] + parent1.info[ranIndex:])

        if child1.Fitness(target) >= child2.Fitness(target):
            self.info = child1.info
        else:
            self.info = child2.info
        
        return True
    
    # calculate fitness from target string
    # fitness function, depends from the what similar is Individual than target
    def Fitness(self, target: str):
        if len(target) != self.length:
            print("Incompatible",self.info,"chromosome, lengths are not equals")
            return self.length
        self.fitness = 0
        for i in range(0, self.length):
            if self.info[i] != target[i]:
                self.fitness += 1
        return self.fitness
    
    def mutation(self) -> None:
        new_info = list(self.info)
        for i in range(0, self.length):
            p_m = random.random()
            if p_m >= 0.1 and p_m <= 0.3:
                new_info[i] = ranGene()
        self.info = "".join(new_info)
    
    def getFitness(self) -> int:
        return self.fitness
    
    def getLength(self) -> int:
        return self.length

# FUNCTIONS

# return a random gene from GENES (valid genes list)
def ranGene():
    r = random.randint(0, len(GENES) - 1)
    return GENES[r]

# return a random population with N elements and each element
# has len(T) (target length) length
def generateInitialPopulation(N: int, chromosome_length: int):
    generated = []
    for _ in range(0, N):
        new_chromosome = Chromosome(chromosome_length)
        new_chromosome.randomGenes()
        generated.append(new_chromosome)
    return generated

def selection(population, target: str):
    found = False
    # create a list for new population (new generation)
    new_population = []
    # order our population by fitness, lower to greater
    population = sorted(population, key = lambda chromosome:chromosome.Fitness(target))

    # get the 10% index from population list
    n = int(0.1*POPULATION_SIZE)
    # save the 10% of best childs
    new_population.extend(population[:n])

    if population[0].getFitness() == 0:
        return [population, True]

    # get the 90% index from population list
    n = int(0.9*POPULATION_SIZE)
    # get the 50% index from population list, this is for get the top 50 of fitness
    nf = int(0.5*POPULATION_SIZE)
    for _ in range(0, n):
        parents = random.choices(population[:nf], k=10)
        parents = sorted(parents, key = lambda chromosome:chromosome.getFitness())
        child = Chromosome(CHROMOSOME_LENGTH)
        child.crossover(parents[0], parents[1], target)
        child.mutation()
        new_population.append(child)
    
    return [new_population, False]

def sga_test():

    found = False
    generation = 0
    population = generateInitialPopulation(POPULATION_SIZE, CHROMOSOME_LENGTH)
    while not found:
        generation+=1
        population, found = selection(population, TARGET)
        print(generation, "generation", "best", population[0].info, "fitness", population[0].getFitness())
        if found:
            break

sga_test()