from Chromosome import Chromosome
from front import Front
from couple import Couple
import random
import copy
import pytest

class Population:
    def __init__ (self, numberOfIndividuals):
        self.numberOfIndividuals = numberOfIndividuals
        self.chromosomes=[]
        self.fronts = []
        self.averageFitness1 = 0
        self.averageFitness2 = 0

    def initialize (self):
        for i in range (self.numberOfIndividuals):
            self.chromosomes.append (Chromosome())
            self.chromosomes [i].populationID = i
            self.chromosomes [i].initialize ()
        return self.chromosomes

    def calculate_Fitness (self):
        for i in range (self.numberOfIndividuals):
            self.chromosomes [i].calculate_Fitness ()
            self.averageFitness1 += (self.chromosomes [i].fitness1 / self.numberOfIndividuals)
            self.averageFitness2 += (self.chromosomes [i].fitness2 / self.numberOfIndividuals)

    def NondominatedSorting (self):
        f1 = Front()
        for i in range (self.numberOfIndividuals):
            self.chromosomes [i].count_BeingDominated (self)
            self.chromosomes [i].detrmine_DominatedPoints (self)
            if self.chromosomes [i].is_Rank1 ():
                f1.answers.append (copy.deepcopy (self.chromosomes [i]))

        self.fronts.append (copy.deepcopy (f1))

        fi = copy.deepcopy (f1)
        a = 1
        while len (fi.answers) > 0:
            q = []
            for j in range (len (fi.answers)):
                for m in range (len (fi.answers [j].dominatedPoints)):
                    fi.answers [j].dominatedPoints [m].beingdominatedCount -= 1
                    if fi.answers [j].dominatedPoints [m].beingdominatedCount == 0:
                        fi.answers [j].dominatedPoints [m].rank = a+1
                        q.append (fi.answers [j].dominatedPoints [m])
            fi = Front()
            for n in range (len (q)):
                fi.answers.append (copy.deepcopy (q [n]))
            if fi.answers:
                self.fronts.append (copy.deepcopy (fi))
            a += 1

    def determine_FrontsAttributes (self):
        for i in range (len (self.fronts)):
            self.fronts [i].determine_AnswersID ()
            self.fronts [i].assign_CrowdDistance ()
    
    def determine_Fronts (self):
        self.NondominatedSorting ()
        self.determine_FrontsAttributes ()

    def tournamentselect(self, tournamentsize):
        rand_index=random.sample(range(0,self.numberOfIndividuals,tournamentsize),tournamentsize)
        best_rank=1000
        best_distance=-1000
        selected_chromosome=None
        for s in range(0,tournamentsize):
            if (self.chromosomes[rand_index[s]].rank <= best_rank) and (self.chromosomes[rand_index[s]].crowdingDistance>=best_distance):
                selected_chromosome=copy.deepcopy(self.chromosomes[rand_index[s]])
                best_rank=copy.deepcopy(self.chromosomes[rand_index[s]].rank)
                best_distance=copy.deepcopy(self.chromosomes[rand_index[s]].crowdingDistance)
    
        return selected_chromosome

    def select_Parents (self):
        first_parent=self.tournamentselect (3)
        second_parent=self.tournamentselect (3)
        return first_parent, second_parent

    def generate_Children (self):
        i=0
        children = Population (self.numberOfIndividuals)
        while (i < self.numberOfIndividuals):
            firstParent, secondParent = self.select_Parents () 
            couple = Couple (firstParent, secondParent)     
            child = couple.crossover ()
            children.chromosomes.append(Chromosome ())
            children.chromosomes[i].string = copy.deepcopy (child)
            i += 1
        return children

    def mutate (self):
        for i in range (self.numberOfIndividuals):
            self.chromosomes [i].mutation()
        return self

    def determine_AnswersID (self):
        for i in range (self.numberOfIndividuals):
            self.chromosomes [i].populationID = i

    def copyto_R (self, r):
        for chrom in self.chromosomes:
            r.chromosomes.append(copy.deepcopy (chrom))

    # def appendto_R (self, r):
    #     for j in range (self.numberOfIndividuals, 2 * self.numberOfIndividuals):
    #         r.chromosomes [j] = copy.deepcopy (self.chromosomes [j-self.numberOfIndividuals])

    def make_NewPopulation (self):
        new_pop = Population (int (self.numberOfIndividuals/2))
        new_pop_chromosomes = copy.deepcopy (self.fronts [0].answers)
        frontIndex = 1
        while (len (new_pop_chromosomes) < int(self.numberOfIndividuals/2)):
            for answer in self.fronts [frontIndex].answers:
                new_pop_chromosomes.append (copy.deepcopy (answer))
            frontIndex += 1
        if len (new_pop_chromosomes) > self.numberOfIndividuals :
            new_pop.chromosomes = copy.deepcopy (new_pop_chromosomes [0:self.numberOfIndividuals-1])
        else:
            new_pop.chromosomes = copy.deepcopy (new_pop_chromosomes)
        return new_pop
