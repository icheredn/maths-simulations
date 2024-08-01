import matplotlib.pyplot as plt
from math import *
from random import *
from numpy import cbrt

Y = []
X = []
Z = []
R = 5

for i in range (10000):

    #disk
    
    r = R*sqrt(uniform(0,1))
    phi = uniform(0,2*pi)
    x = r*cos(phi)
    y = r*sin(phi)
    X.append(x)
    Y.append(y)
    
    #sphere
    '''
    r = R*cbrt(uniform(0,1))        #
    phi = acos(2*uniform(0,1)-1)
    theta = uniform(0,2*pi)

    z = r*cos(phi)                #back to rectangular coordinates
    x = r*cos(theta)*sin(phi)
    y = r*sin(theta)*sin(phi)

    X.append(x)
    Y.append(y)
    Z.append(z)
    '''
    
plt.scatter(X,Y)
plt.show()
