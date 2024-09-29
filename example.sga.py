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
GENES = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890_-=;/#@$!&*()<>,.?'
TARGET = 'hola mama'
POPULATION_SIZE = 10
population = []


# FUNCTIONS

# return a random gene from GENES (valid genes list)
def ranGene():
    r = random.randint(0, len(GENES) - 1)
    return GENES[r]

# return a random population with N elements and each element
# has len(T) (target length) length
def generateInitialPopulation(N: int, T: str):
    generated = []
    for i in range(0, N):
        ranString = ''
        for j in range(0, len(T)):
            ranString += ranGene()
        generated.append(ranString)
    return generated