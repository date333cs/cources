# -*- coding: utf-8 -*-
import random
import numpy
import matplotlib.pyplot as plt

T = 10000
Mu = 0.0
Sigma = 1.0
# random.seed( 20131107 )

y = []
n1 = 0; n2=0; n3=0
for i in range(T):
    r = random.gauss(Mu, Sigma)
    y.append(r)
    if r > Mu - Sigma and r < Mu + Sigma:
        n1 +=1
    if r > Mu - 2.0*Sigma and r < Mu + 2.0*Sigma:
        n2 +=1
    if r > Mu - 3.0*Sigma and r < Mu + 3.0*Sigma:
        n3 +=1

y = numpy.array(y)

# キャンバス
fig = plt.figure()

ax = fig.add_subplot(111)
ax.hist(y, bins=101, range=(-5, 5), density=False, facecolor='g')
ax.set_xlim(-5, 5)
ax.grid(True)

print (float(n1)/float(T))
print (float(n2)/float(T))
print (float(n3)/float(T))

# plt.savefig(ss108.jpg)   # 図のファイルを作りたいとき
plt.show()
