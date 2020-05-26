import pandas as pd
import numpy as np
import random as random
import array
import copy


class Chromosome:
    ax = 0
    bx = 5
    ay = 0
    by = 3
    p_mutation = 0.3

    def __init__(self, x_bit=9, y_bit=9):
        self.__x_bit = x_bit  # This is equivalent to making the variable private!
        self.__y_bit = y_bit
        self.chrom_length = self.__x_bit+self.__y_bit
        self.n_domcount = 0
        self.domby = []
        self.rank = 0
        self.crowd_dist = 0
        self.pop_id = 0
        self.front_id=0
        self.string = []
        self.x = 0
        self.y = 0
        self.fit1 = 0
        self.fit2 = 0

    def initialize(self):
        self.string = [0] * self.chrom_length

        n_rand_point = random.sample(range(self.chrom_length), 1)
        rand_point = random.sample(range(self.chrom_length), n_rand_point[0])
        for s in range(n_rand_point[0]):
            self.string[rand_point[s]] = 1

    def bin2dec_x(self):
        x_dec = 0
        for i in range(self.__x_bit):
            x_dec += self.string[i]*(2**(i))
        x = self.ax+x_dec*(self.bx-self.ax)/((2**self.__x_bit)-1)
        return x

    def bin2dec_y(self):
        y_dec = 0
        for j in range(self.__x_bit, self.chrom_length):
            y_dec += self.string[j]*(2**(j-self.__x_bit))
        y = self.ay+y_dec*(self.by-self.ay)/((2**self.__y_bit)-1)
        return y

    def decode_x(self):
        self.x = self.bin2dec_x()
        return self.x

    def decode_y(self):
        self.y = self.bin2dec_y()
        return self.y

    def calc_fitness1_chrom(self):
        self.x = self.decode_x()
        self.y = self.decode_y()
        self.fit1 = 4*self.x**2+4*self.y**2
        return self.fit1

    def calc_fitness2_chrom(self):
        self.x = self.decode_x()
        self.y = self.decode_y()
        self.fit2 = (self.x-5)**2+(self.y-5)**2
        return self.fit2

    def calc_fitness_chrom(self):
        self.calc_fitness1_chrom()
        self.calc_fitness2_chrom()

    def domcount(self, n_pop, pop):
        for j in range(0, n_pop):
            if (self.fit1 > pop.answers[j].fit1) and (self.fit2 > pop.answers[j].fit2):
                self.n_domcount += 1
        return self.n_domcount

    def det_domby(self, n_pop, pop):
        for j in range(0,n_pop):
            if (self.fit1 < pop.answers[j].fit1) and (self.fit2 < pop.answers[j].fit2):
                self.domby.append(pop.answers[j])
        return self.domby

    def det_rank1(self):
        if self.n_domcount == 0:
            self.rank = 1
            return True

    def mutation(self):
        rand = random.random()
        if rand < self.p_mutation:
            rand_point = random.randint(0, self.chrom_length-1)
            self.string[rand_point] = not (self.string[rand_point])
