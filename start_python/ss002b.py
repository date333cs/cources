# -*- coding: utf-8 -*-
# 平均 μ=0，標準偏差 σ=0.7 のデータを200個生成して，ファイルに保存
import random

filename = "random200.dat"
T = 200;
mu = 0.0
sigma = 0.7
# random.seed( 20131107 )

f = open(filename, 'w')
for i in range(T):
    f.write("%f\n" % random.gauss(mu,sigma) )

f.close()
