import copy
import random
class Couple:
    p_crossover=0.7
    crossoverpoint1=5
    crossoverpoint2=14
    def __init__ (self, first_parent, second_parent):
        self.first_parent=first_parent
        self.second_parent=second_parent
        self.child=[]   

    def crossover (self):
        rand = random.random()
        if rand < self.p_crossover:
            for p in range(0,len(self.first_parent.string)):
                if (p < self.crossoverpoint1) or (p>self.crossoverpoint2):
                    self.child.append(copy.deepcopy(self.first_parent.string[p]))
                else:
                    self.child.append(copy.deepcopy(self.second_parent.string[p]))
        else:
            self.child=copy.deepcopy(self.first_parent.string)
                        
        return self.child