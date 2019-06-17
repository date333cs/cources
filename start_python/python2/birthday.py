# -*- coding: utf-8 -*-
import random

N = 50
n_trials = 10000
n_matches = 0

for i in range(n_trials):   # 繰り返し
    b = []                  # birthday の b
    for i in range(N):   
        day = random.randint(1,365)
        if day in b:
            print b.index(day), '番目と', i ,'番目が一致'
            n_matches +=1
            break
        else:
            b.append(day)
            if i == N-1:
                print '全員ちがう誕生日！'
                        
print float(n_matches)/float(n_trials)
