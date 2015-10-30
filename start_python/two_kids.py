# -*- coding: utf-8 -*-
import random

# boy 0, girl 1

n_trials = 10000
n= 0
n_cases = 0
kids = [0]*2

for i in range(n_trials):
    kids[0] = random.randint(0,1)
    kids[1] = random.randint(0,1)

    if kids[0]==0 or kids[1]==0:
        n_cases +=1
        if kids[0]==0 and kids[1]==0:
            n += 1

print  float(n)/float(n_cases)
