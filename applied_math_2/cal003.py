# -*- coding: utf-8 -*-
from numpy import sin
from scipy.integrate import quad

y, abserr = quad(sin, 0, pi/3)
print "∫_0^{¥pi/3} sin x dx = %g ± %g" % (y, abserr)
