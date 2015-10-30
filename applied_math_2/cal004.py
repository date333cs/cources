# -*- coding: utf-8 -*-
#
#  from http://naoyat.hatenablog.jp/entry/2012/03/03/221022

from pylab import *
from scipy.integrate import quad

def fourier(fun, n_max):
  a = []
  b = []
  for n in xrange(0, 1+n_max):
    res, err = quad(lambda x:fun(x)*cos(n*x), -pi, pi)
    a.append(res/pi)
    res, err = quad(lambda x:fun(x)*sin(n*x), pi, pi)
    b.append(res/pi)
  def fn(x):
    sum = a[0] / 2
    for n in xrange(1, 1+n_max):
      sum += a[n]*cos(n*x) + b[n]*sin(n*x)
    return sum
  return fn

def f(x):
  x = (x + pi) % (pi * 2) - pi
  if x >= 0:
    return 1
  else:
    return 0

x_min = -pi - 0.5
x_max = pi*2 + 0.5
y_min = -0.25
y_max = 1.25
axis([x_min, x_max, y_min, y_max])

f_fn = fourier(f, 10)
xs = linspace(x_min, x_max, 256)
plot(xs, amap(f, xs), 'b:', lw=1)
plot(xs, amap(f_fn, xs), 'r-', lw=1)
show()
