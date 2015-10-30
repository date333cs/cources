# -*- coding: utf-8 -*-
from pylab import *


# -5pi から 5pi まで 0.01 刻みの配列をつくる (numpy.arange )
# t = arange(-2*pi, 2*pi, 0.01)
t = linspace(-2.0*pi, 2.0*pi, 400)


s1 = sin(0*t)
K = 2
for k in range(K):
    s1 += pow(-1.0,k)*sin((k+1)*t + 3.2)/(k+1)

s2 = sin(0*t)
K = 10
for k in range(K):
    s2 += pow(-1.0,k)*sin((k+1)*t + 3.2)/(k+1)

s3 = sin(0*t)
K = 100
for k in range(K):
    s3 += pow(-1.0,k)*sin((k+1)*t + 3.2)/(k+1)

# plot (t, s1, linewidth=1.0, color="r", linestyle="--")
plot (t, s1, linewidth=1.0, color="r")
plot (t, s2, linewidth=1.0, color="b")
plot (t, s3, linewidth=1.0, color="g")
xlabel('t')
grid (True)
show()

# savefig('plt.eps')
