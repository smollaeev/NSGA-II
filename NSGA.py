from Chromosome import Chromosome
from front import Front
from population import Population
import copy

class NSGA:
    def __init__ (self):
        self.bestFitnesses = []
        self.bestChromosomes = []
        self.averagesOfFitness1 = []
        self.averagesOfFitness2 = []
        self.generation = 0
        self.fronts = []

    def determine_Bests (self):
        for i in range (len (self.fronts [0].answers)):
            self.bestFitnesses.append (self.fronts [0].answers [i].fitness1)
            self.bestFitnesses.append (self.fronts [0].answers [i].fitness2)
            self.bestChromosomes.append (self.fronts [0].answers [i].x)
            self.bestChromosomes.append (self.fronts [0].answers [i].y)

    def make_F1AndF2Axis (self, pop):
        self.xAxis = []
        self.yAxis = []
        for i in range (len (pop.fronts [0].answers)):
            self.xAxis.append (copy.deepcopy (self.bestFitnesses [2*i]))
            self.yAxis.append (copy.deepcopy (self.bestFitnesses [2*i+1]))

    def start (self, numberOfGenerations, numberOfIndividuals):

        pop = Population (numberOfIndividuals)
        r = Population (2*numberOfIndividuals)

        pop.initialize ()        

        while self.generation < numberOfGenerations:
            pop.calculate_Fitness ()
            self.averagesOfFitness1.append (pop.averageFitness1)
            self.averagesOfFitness2.append (pop.averageFitness2)

            pop.determine_Fronts ()
            self.fronts = copy.deepcopy (pop.fronts)
            self.determine_Bests ()

            self.make_F1AndF2Axis (pop)

            self.print_Results ()

            pop.copyto_R (r) 

            children = pop.generate_Children ()
            pop = copy.deepcopy (children)
            # for i in range (len(pop.chromosomes)):
            #     if pop.chromosomes [i].string != children.chromosomes [i].string:
            #         a = 1
            # l = 0
            # for i in range (pop.numberOfIndividuals):
            #     if pop.chromosomes [i].string == r.chromosomes [i].string:
            #         l+=1
            # if l == pop.numberOfIndividuals:
            #     m = 1
            pop.mutate ()

            pop.appendto_R (r)

            r.determine_AnswersID ()
            r.calculate_Fitness()
            r.determine_Fronts ()

            newPopulation = r.make_NewPopulation ()

            pop = copy.deepcopy (newPopulation) 

            self.generation += 1