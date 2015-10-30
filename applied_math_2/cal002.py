# -*- coding: utf-8 -*-
from scipy.integrate import quad

y, abserr = quad(lambda x:x*x*x, 0, 2)
print "∫_0^2 x^3 dx = %g ± %g" % (y, abserr)
