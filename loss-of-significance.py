import numpy
from numpy import cos

import matplotlib.pylab as plt

x= numpy.linspace(-4*10**-8,4*10**-8,100000)
y= (1-cos(x))/(x**2)
plt.plot (x,y)