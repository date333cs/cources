# -*- coding: utf-8 -*-
import random
import numpy
import matplotlib.pyplot as plt

T1 = 100
T2 = 1000
T3 = 10000
Sigma = 0.7
Mu = 0.0
# random.seed( 20131107 )

y1 = []
for i in range(T1):
    y1.append(random.gauss(Mu, Sigma))

y1 = numpy.array(y1)


y2 = []
for i in range(T2):
    y2.append(random.gauss(Mu, Sigma))

y2 = numpy.array(y2)


y3 = []
for i in range(T3):
    y3.append(random.gauss(Mu, Sigma))

y3 = numpy.array(y2)


# キャンバス
fig = plt.figure()

# プロット領域（2x2分割の1番目に領域を配置せよという意味）
ax = fig.add_subplot(221)
ax.hist(y1, bins=15, range=(-3.75, 3.75), normed=False, facecolor='g')
ax.set_xlim(-3.5, 3.5)
ax.grid(True)
ax.set_title('Histogram 1', size=16)

ay = fig.add_subplot(222)
ay.hist(y2, bins=15, range=(-3.75, 3.75), normed=False, facecolor='g')
ay.set_xlim(-3.5, 3.5)
ay.grid(True)
ay.set_title('Histogram 2', size=16)

az = fig.add_subplot(223)
az.hist(y3, bins=15, range=(-3.75, 3.75), normed=False, facecolor='g')
az.set_xlim(-3.5, 3.5)
az.grid(True)
az.set_title('Histogram 3', size=16)


plt.show()
