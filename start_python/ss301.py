# -*- coding: utf-8 -*-
import math
import random
import numpy
import matplotlib.pyplot as plt

# コインを N 回投げる．表がでれば 1，ウラがでれば 0 を足していく．N回後の総和を S とする．
# 平均値は S/2． ここからどのくらいズレるか．
# この作業を，T回繰り返して．S の値の分布を見る．
# これが目的．

T = 1000
N = 100 # コイントス（0 or 1）の繰り返し回数
Mu = N/2 # 平均値
Sigma = math.sqrt(N)/2 # 標準偏差
# random.seed( 20160817 )

y = []
n1 = 0; n2=0; n3=0

for i in range(T):
    S = 0
    for j in range(N):
	r = random.randint(0, 1)  # 0 か 1 の乱数をそれぞれ確率 0.5 で生成
	S = S + r
    y.append(S)
    
    if S > Mu - Sigma and r < Mu + Sigma:
           n1 +=1
    if S > Mu - 2.0*Sigma and r < Mu + 2.0*Sigma:
           n2 +=1
    if S > Mu - 3.0*Sigma and r < Mu + 3.0*Sigma:
           n3 +=1

y = numpy.array(y)

# キャンバス
fig = plt.figure()

ax = fig.add_subplot(111)
ax.hist(y, bins=101, range=(0, N), normed=False, facecolor='g')
# bins ： ビンの数
# range： ビンの範囲（デフォルトは配列の最小値と最大値)
# see http://qiita.com/supersaiakujin/items/be4a78809e7278c065e6
# ax.set_xlim(-5, 5)
ax.grid(True)

print float(n1)/float(T)
print float(n2)/float(T)
print float(n3)/float(T)

# plt.savefig(ss301.jpg)   # 図のファイルを作りたいとき
plt.show()
