import copy
import random

class Couple:
    probabilityOfCrossover = 0.7
    crossoverPoint1 = 5
    crossoverPoint2 = 14

    def __init__ (self, firstParent, secodnParent):
        self.firstParent = firstParent
        self.secondParent = secodnParent
        self.child = []  

    def crossover (self):
        rand = random.random()
        if rand < self.probabilityOfCrossover:
            for p in range(len (self.firstParent.string)):
                if (p < self.crossoverPoint1) or (p > self.crossoverPoint2):
                    self.child.append (copy.deepcopy (self.firstParent.string [p]))
                else:
                    self.child.append (copy.deepcopy (self.secondParent.string [p]))
        else:
            self.child = copy.deepcopy (self.firstParent.string)
                        
        return self.child