import pandas as pd
import numpy as np
import random as random
import array
import copy


class Chromosome:
    aX = 0
    bX = 5
    aY = 0
    bY = 3
    probabilityOfMutation = 0.3
    numberOfBitsX=9
    numberOfBitsY=9

    def __init__(self):
        self.length = self.numberOfBitsX + self.numberOfBitsY
        self.beingdominatedCount = 0
        self.dominatedPoints = []
        self.rank = 0
        self.crowdingDistance = 0
        self.populationID = 0
        self.frontID = 0
        self.string = []
        self.x = 0
        self.y = 0
        self.fitness1 = 0
        self.fitness2 = 0

    def initialize (self):
        self.string = [0] * self.length

        numberOfRandomPoints = random.randint (0, self.length - 1)
        randomPoints = random.sample(range(self.length), numberOfRandomPoints)
        for s in range(numberOfRandomPoints):
            self.string [randomPoints [s]] = 1

    def binary2decimal_X (self):
        decimalX = 0
        for i in range (self.numberOfBitsX):
            decimalX += self.string [i] * (2 ** (i))
        x = self.aX + decimalX * (self.bX - self.aX) / ((2 ** self.numberOfBitsX) - 1)
        return x

    def binary2decimal_Y (self):
        decimalY = 0
        for j in range (self.numberOfBitsX, self.length):
            decimalY += self.string [j] * (2 ** (j - self.numberOfBitsX))
        y = self.aY + decimalY * (self.bY - self.aY) / ((2 ** self.numberOfBitsY) - 1)
        return y

    def decode_X (self):
        self.x = self.binary2decimal_X ()
        return self.x

    def decode_Y (self):
        self.y = self.binary2decimal_Y ()
        return self.y

    def calculate_Fitness1 (self):
        self.x = self.decode_X ()
        self.y = self.decode_Y ()
        self.fitness1 = 4 * self.x ** 2 + 4 * self.y ** 2
        return self.fitness1

    def calculate_Fitness2 (self):
        self.x = self.decode_X ()
        self.y = self.decode_Y ()
        self.fitness2 = (self.x - 5) ** 2 + (self.y - 5) ** 2
        return self.fitness2

    def calculate_Fitness (self):
        self.calculate_Fitness1 ()
        self.calculate_Fitness2 ()

    def count_BeingDominated (self, population):
        for j in range (population.numberOfIndividuals): 
            if (self.fitness1 > population.chromosomes [j].fitness1) and (self.fitness2 > population.chromosomes [j].fitness2):
                self.beingdominatedCount += 1

    def detrmine_DominatedPoints (self, population):
        for j in range (population.numberOfIndividuals):
            if (self.fitness1 < population.chromosomes [j].fitness1) and (self.fitness2 < population.chromosomes [j].fitness2):
                self.dominatedPoints.append (population.chromosomes [j])

    def is_Rank1 (self):
        if self.beingdominatedCount == 0:
            self.rank = 1
            return True

    def mutation(self):
        rand = random.random ()
        if rand < self.probabilityOfMutation:
            randomPoint = random.randint (0, self.length - 1)
            self.string [randomPoint] = not (self.string [randomPoint])
