#!/usr/bin/python

from matplotlib import pyplot as plt
import numpy as np


def f(x):
  if x < -2:
    return -x-2
  elif -2 <= x and x <= 0:
    return np.sqrt(4-x*x)
  elif x < 3:
    return 2
  else:
   return (3-x)*3+2


xvals = np.linspace(-4,4,1000)
yvals = [f(x) for x in xvals]

plt.plot(xvals,yvals)
plt.grid()
plt.savefig('../fig/finalfig.png')
plt.show()


