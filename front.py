import pandas as pd
import numpy as np
import random
import array
import copy

class Front:
    def __init__ (self):                
        self.answers=[]
        self.asc_answers1=[]
        self.asc_answers2=[]
        self.asc_fit1=[]
        self.asc_fit2=[]
    
    def sort_asc_f1(self):        
        for i in range(len(self.answers)):
            self.asc_fit1.append(copy.deepcopy(self.answers[i].fit1))
        self.asc_fit1.sort()
        for i in range(0,len(self.answers)):
            for j in range(0,len(self.answers)):
                if self.asc_fit1[i]==self.answers[j].fit1:
                    self.asc_answers1.append(self.answers[j])
                    break
        return self.asc_fit1,self.asc_answers1


    def sort_asc_f2(self):
        for i in range(len(self.answers)):
            self.asc_fit2.append(copy.deepcopy(self.answers[i].fit2))
        self.asc_fit2.sort()
        for i in range(0,len(self.answers)):
            for j in range(0,len(self.answers)):
                if self.asc_fit2[i]==self.answers[j].fit2:
                    self.asc_answers2.append(self.answers[j])
                    break
        return self.asc_fit2,self.asc_answers2

    def det_id(self):
        for i in range(len(self.answers)):
            self.answers[i].front_id=i

    def crowd_dist_assign(self):
        self.asc_fit1,self.asc_answers1=self.sort_asc_f1()
        self.asc_fit2,self.asc_answers2=self.sort_asc_f2()
        self.asc_answers1[0].crowd_dist=np.Infinity
        self.asc_answers2[0].crowd_dist=np.Infinity
        self.asc_answers1[len(self.answers)-1].crowd_dist=np.Infinity
        self.asc_answers2[len(self.answers)-1].crowd_dist=np.Infinity
        for i in range(1,len(self.answers)-1):
            try:
                self.asc_answers1[i].crowd_dist+=(self.asc_fit1[i+1]-self.asc_fit1[i-1])/(self.asc_fit1[len(self.answers)-1]-self.asc_fit1[0])
            except:
                self.asc_answers1[i].crowd_dist=np.Infinity
            try:
                self.asc_answers2[i].crowd_dist+=(self.asc_fit2[i+1]-self.asc_fit2[i-1])/(self.asc_fit2[len(self.answers)-1]-self.asc_fit2[0])
            except:
                self.asc_answers2[i].crowd_dist=np.Infinity
    
        for i in range(0,len(self.answers)):
            for j in range(0,len(self.answers)):
                if self.answers[i].front_id==self.asc_answers1[j].front_id:
                    self.answers[i].crowd_dist+=self.asc_answers1[j].crowd_dist
                    break
            for j in range(0,len(self.answers)):
                if self.answers[i].front_id==self.asc_answers2[j].front_id:
                    self.answers[i].crowd_dist+=self.asc_answers2[j].crowd_dist
                    break
        
