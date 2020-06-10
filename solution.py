from Chromosome import Chromosome
from front import Front
from population import Population
import matplotlib.pyplot as plt
import copy


class Solution:
    def __init__ (self):
        self.bestFitnesses = []
        self.bestChromosomes = []
        self.averagesOfFitness1 = []
        self.averagesOfFitness2 = []
        self.generation = 0
        self.xAxis = []
        self.yAxis = []

    def make_F1AndF2Axis (self, front):
        self.xAxis = []
        self.yAxis = []
        for answer in front.answers:
            self.xAxis.append (answer.fitness1)
            self.yAxis.append (answer.fitness2)

    def print_Results (self, front):
        print (f'Generation {self.generation}:')
        for answer in front.answers:
            print
            print (f'   Best fitness = f1: {answer.fitness1}, f2: {answer.fitness2}')
            print (f'   Best Answers = x: {answer.x}, y: {answer.y}')
        
        print
        print(f'    Average Fitness = {self.averagesOfFitness1 [self.generation]} , {self.averagesOfFitness2 [self.generation]}')

    def show_Diagrams (self):
        fig, axes = plt.subplots (nrows = 1, ncols = 2)
        axes [0].plot (self.averagesOfFitness1)
        axes [0].set_title ('Average of F1 in Each Generation')

        axes [1].plot (self.averagesOfFitness2)
        axes [1].set_title ('Average of F2 in Each Generation')
        # plt.plot (self.averagesOfFitness1)
        # plt.ylabel ('Average Fitness of f1 in Each Generation')
        # plt.show ()

        # plt.plot (self.averagesOfFitness2)
        # plt.ylabel ('Average Fitness of f2 in Each Generation')
        plt.show ()
        
        plt.scatter (self.xAxis, self.yAxis, label= "stars", color= "green", marker= "*", s=30) 
        plt.xlabel ('f1')
        plt.ylabel ('f2')
        plt.title ('The first Pareto Front')
        plt.show ()
            
    def NSGA (self, numberOfGenerations, numberOfIndividuals):

        pop = Population (numberOfIndividuals)

        pop.initialize ()        

        while self.generation < numberOfGenerations:

            pop.calculate_Fitness ()
            self.averagesOfFitness1.append (pop.averageFitness1)
            self.averagesOfFitness2.append (pop.averageFitness2)

            pop.determine_AnswersID ()
            pop.determine_Fronts ()

            self.print_Results (pop.fronts [0])
            
            r = Population (2 * numberOfIndividuals)
            pop.copyto_R (r) 
            lastPopulation = copy.deepcopy (pop)

            children = pop.generate_Children ()

            children.mutate ()

            children.copyto_R (r)

            r.determine_AnswersID ()
            r.calculate_Fitness()
            r.determine_Fronts ()

            newPopulation = r.make_NewPopulation ()
            pop = copy.deepcopy (newPopulation) 

            self.generation += 1

        self.make_F1AndF2Axis (lastPopulation.fronts [0])
        self.show_Diagrams ()
        