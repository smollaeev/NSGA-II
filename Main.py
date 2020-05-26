import pandas as pd
import numpy as np
import random
import array
from Chromosome import Chromosome
from front import Front
from population import Population
import json
import matplotlib.pyplot as plt
import copy

def GA (n_rep, n_pop):
    pop=Population(n_pop)
    pop.initialize()
    pop.calc_fitness()
    n=0
    best_fit_gen=[]
    best_ans_gen=[]
    avg_fit_gen1=[]
    avg_fit_gen2=[]
    children=Population(n_pop)
    q=Population(n_pop)
    r=Population(2*n_pop)
    while n<n_rep:
        avg_fit1=0
        avg_fit2=0
        x_axis=[]
        y_axis=[]
        pop.calc_fitness()
        f=pop.ns()
        q=copy.deepcopy(pop)
        for i in range(0,n_pop):
            r.answers[i]=copy.deepcopy(q.answers[i])
        print (f'Generation {n}:')
        for i in range(0,len(f[0].answers)):
            best_fit_gen.append(f[0].answers[i].fit1)
            best_fit_gen.append(f[0].answers[i].fit2)
            best_ans_gen.append(f[0].answers[i].x)
            best_ans_gen.append(f[0].answers[i].y)
            print
            print (f'   Best fitness=f1: {best_fit_gen[2*i]},f2: {best_fit_gen[2*i+1]}')
            print (f'   Best Answers=x:{best_ans_gen[2*i]}, y:{best_ans_gen[2*i+1]}')
            x_axis.append(best_fit_gen[2*i])
            y_axis.append(best_fit_gen[2*i+1])
        for j in range(0,n_pop):
            avg_fit1+=(pop.answers[i].fit1/n_pop)
            avg_fit2+=(pop.answers[i].fit2/n_pop)
        avg_fit_gen1.append(avg_fit1)
        avg_fit_gen2.append(avg_fit2)
        print
        print(f'    Average Fitness={avg_fit_gen1[n]},{avg_fit_gen2[n]}')
        for i in range(len(f)):
            f[i].det_id()
            f[i].crowd_dist_assign()
        #selection and crossover
        children=pop.generate_children ()
        pop=copy.deepcopy(children)
        pop=copy.deepcopy(pop.mutation())
        for j in range(n_pop,2*n_pop):
            r.answers[j]=copy.deepcopy(pop.answers[j-n_pop])
        r.det_id()
        r.calc_fitness()
        fronts=r.ns()
        new_pop=Population(n_pop)
        new_pop.answers=copy.deepcopy(fronts[0].answers)
        j=1
        if len(new_pop.answers)<n_pop:
            for c in range(0,n_pop-len(new_pop.answers)):
                try:
                    new_pop.answers.append(copy.deepcopy(fronts[j].answers[c]))
                except:
                    j+=1
                    continue
        pop=copy.deepcopy(new_pop)           
        n+=1
    plt.plot(avg_fit_gen1)
    plt.ylabel('Average Fitness of f1 in Each Generation')
    plt.show()

    plt.plot(avg_fit_gen2)
    plt.ylabel('Average Fitness of f2 in Each Generation')
    plt.show()
    
    plt.scatter(x_axis, y_axis, label= "stars", color= "green", marker= "*", s=30) 
    plt.xlabel ('f1')
    plt.ylabel ('f2')
    plt.title ('The first Pareto Front')
    plt.show()

def main():
    n_rep=150
    n_pop=40
    GA(n_rep,n_pop)
    

if __name__ == "__main__":
    main() 