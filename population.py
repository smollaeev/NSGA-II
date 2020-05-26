from Chromosome import *
from front import *
from couple import *
import random
 
class Population:
    def __init__ (self, n_pop):
        self.n_pop=n_pop
        self.answers=[]
        for i in range(n_pop):
            self.answers.append(Chromosome())
            self.answers[i].pop_id=i

    def initialize(self):
        for i in range (self.n_pop):
            self.answers[i].initialize()
        return self.answers

    def calc_fitness(self):
        for i in range (self.n_pop):
            self.answers[i].calc_fitness_chrom()

    def ns(self):
        f1=Front()
        for i in range(0,self.n_pop):
            self.answers[i].domcount(self.n_pop,self)
            self.answers[i].det_domby(self.n_pop,self)
            if self.answers[i].det_rank1():
                f1.answers.append(self.answers[i])
        f=[]
        f.append(copy.deepcopy(f1))
        fi=Front()
        fi=f1
        a=1
        while len(fi.answers) > 0:
            q=[]
            for j in range(0,len(fi.answers)):
                for m in range(0,len(fi.answers[j].domby)):
                    fi.answers[j].domby[m].n_domcount-=1
                    # for l in range (0,self.n_pop):
                    #     if fi.answers[j].domby[m].pop_id==self.answers[l].pop_id:
                    #         self.answers[l].n_domcount-=1
                    #         break
                    # for p in range (0,len(fi.answers)):
                    #     for k in range(0,len(fi.answers[p].domby)):
                    #         if (fi.answers[p].domby[k].pop_id==fi.answers[j].domby[m].pop_id) and (j!=m):
                    #             fi.answers[p].domby[k].n_domcount-=1
                    #         break
                    if fi.answers[j].domby[m].n_domcount==0:
                        fi.answers[j].domby[m].rank=a+1
                        # for r in range (0,self.n_pop):
                        #     if fi.answers[j].domby[m].pop_id==self.answers[r].pop_id:
                        #         self.answers[r].rank=a+1
                        #         break
                        q.append(fi.answers[j].domby[m])
            fi=Front()
            for n in range(0,len(q)):
                fi.answers.append(copy.deepcopy(q[n]))
            if fi.answers:
                f.append(copy.deepcopy(fi))
            a+=1
        return f
    
    def tournamentselect(self, tournamentsize):
        rand_index=random.sample(range(0,self.n_pop,tournamentsize),tournamentsize)
        best_rank=1000
        best_distance=-1000
        selected_chromosome=None
        for s in range(0,tournamentsize):
            if (self.answers[rand_index[s]].rank <= best_rank) and (self.answers[rand_index[s]].crowd_dist>=best_distance):
                selected_chromosome=copy.deepcopy(self.answers[rand_index[s]])
                best_rank=copy.deepcopy(self.answers[rand_index[s]].rank)
                best_distance=copy.deepcopy(self.answers[rand_index[s]].crowd_dist)
    
        return selected_chromosome

    def select_parents (self):
        first_parent=self.tournamentselect(3)
        second_parent=self.tournamentselect(3)
        return first_parent, second_parent

    def generate_children (self):
        i=0
        children=Population(self.n_pop)
        while (i<self.n_pop) :
            first_parent, second_parent =self.select_parents() 
            couple=Couple(first_parent,second_parent)     
            child=couple.crossover()
            children.answers[i].string=copy.deepcopy(child)
            i+=1
        return children

    def mutation (self):
        for i in range(self.n_pop):
            self.answers[i].mutation()
        return self

    def det_id(self):
        for i in range(0,self.n_pop):
            self.answers[i].pop_id=i
