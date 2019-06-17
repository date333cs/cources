#!/usr/bin/python
# 平均 μ=0，標準偏差 σ=0.7 のデータを200個生成
# 
import random
 
T = 200;
Sigma = 0.7
random.seed( 20131030 )
 
for i in range(T):
    print random.gauss(0,Sigma)
