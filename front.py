import numpy as np
import copy

class Front:
    def __init__ (self):                
        self.answers = []
        self.ascendingAnswers_F1 = []
        self.ascendingAnswers_F2 = []
        self.ascendingFitness1 = []
        self.ascendingFitness2 = []
    
    def sortAscending_Fitness1 (self):        
        for i in range (len (self.answers)):
            self.ascendingFitness1.append (copy.deepcopy (self.answers[i].fitness1))
        self.ascendingFitness1.sort ()
        for i in range (len (self.answers)):
            for j in range (len (self.answers)):
                if self.ascendingFitness1 [i] == self.answers [j].fitness1:
                    self.ascendingAnswers_F1.append (self.answers [j])
                    break

    def sortAscending_Fitness2 (self):
        for i in range (len (self.answers)):
            self.ascendingFitness2.append (copy.deepcopy (self.answers [i].fitness2))
        self.ascendingFitness2.sort ()
        for i in range (len (self.answers)):
            for j in range (len (self.answers)):
                if self.ascendingFitness2 [i] == self.answers [j].fitness2:
                    self.ascendingAnswers_F2.append (self.answers [j])
                    break

    def determine_AnswersID (self):
        for i in range (len (self.answers)):
            self.answers [i].front_id = i

    def assign_CrowdDistance (self):
        self.sortAscending_Fitness1 ()
        self.sortAscending_Fitness2 ()

        self.ascendingAnswers_F1 [0].crowdingDistance = np.Infinity
        self.ascendingAnswers_F2 [0].crowdingDistance = np.Infinity
        self.ascendingAnswers_F1 [len (self.answers) - 1].crowdingDistance = np.Infinity
        self.ascendingAnswers_F2 [len (self.answers) - 1].crowdingDistance = np.Infinity

        for i in range (1,len (self.answers) - 1):
            try:
                self.ascendingAnswers_F1 [i].crowdingDistance += (self.ascendingFitness1 [i+1] - self.ascendingFitness1 [i-1]) / (self.ascendingFitness1 [len (self.answers) - 1] - self.ascendingFitness1 [0])
            except:
                self.ascendingAnswers_F1 [i].crowdingDistance = np.Infinity
            try:
                self.ascendingAnswers_F2 [i].crowdingDistance += (self.ascendingFitness2 [i+1] - self.ascendingFitness2 [i-1]) / (self.ascendingFitness2 [len (self.answers) - 1] - self.ascendingFitness2 [0])
            except:
                self.ascendingAnswers_F2 [i].crowdingDistance = np.Infinity
    
        for i in range (len (self.answers)):
            for j in range (len (self.answers)):
                if self.answers [i].front_id == self.ascendingAnswers_F1 [j].front_id:
                    self.answers [i].crowdingDistance += self.ascendingAnswers_F1 [j].crowdingDistance
                    break
            for j in range (len (self.answers)):
                if self.answers [i].front_id == self.ascendingAnswers_F2 [j].front_id:
                    self.answers [i].crowdingDistance += self.ascendingAnswers_F2 [j].crowdingDistance
                    break
        
