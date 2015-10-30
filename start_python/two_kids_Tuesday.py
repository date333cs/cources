# -*- coding: utf-8 -*-
import random

n_trials = 10000
n= 0
n_cases = 0
kids = [0]*2  # 2人の性別． 男 0, 女 1
week = [0]*2  # 2人の誕生日の曜日

for i in range(n_trials):
    kids[0] = random.randint(0,1)
    week[0] = random.randint(0,6)
    kids[1] = random.randint(0,1)
    week[1] = random.randint(0,6)

    if kids[0]==0 and week[0]==2:
        n_cases +=1
        if kids[1]== 0:
            n += 1
    elif  kids[1]==1 and week[1]==2:
        n_cases +=1
        if kids[0]== 0:
            n += 1

# print  "#cases = ", n_cases,"/", n_trials

print  float(n)/float(n_cases)
