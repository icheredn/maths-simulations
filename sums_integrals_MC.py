from math import *
from random import *
from numpy import cbrt

def double_sum(n, k):
    sum = 0
    for i in range(1,n+1):
        for j in range(i,k+1):
            sum += 1/(i**2*(j+1)**2)
    return sum

#print(double_sum(1000,1000000))

def oily_macaroni(n):
    H_n = 0
    for i in range(1,n+1):
        H_n+=1/i
    return H_n - log(n)

#print(oily_macaroni(1000000000)) #first correct digit n=22; second: n=180
#third - n=638; forth - n=5929; slowly convergent

def f1(x,y,z):
    return x+y*y+z


def triple_sphere_integral_MC(n,f):
    M = 0
    R = 1
    for i in range(n):
        #x = uniform(-1,1)
        #y = uniform(-sqrt(1-x*x),sqrt(1-x*x))
        #z = uniform(-sqrt(1-x*x-y*y),sqrt(1-x*x-y*y))

        r = R*cbrt(uniform(0,1))        #inverse sampling method
        phi = acos(2*uniform(0,1)-1) #zenith 
        theta = uniform(0,2*pi)         #azimuth

        z = r*cos(phi)                #back to rectangular coordinates
        x = r*cos(theta)*sin(phi)
        y = r*sin(theta)*sin(phi)

        f_val = f(x,y,z)

        #print(x,y,z,f_val)
        if f_val >= 0:
            u = uniform(0,5)
            if u <= f_val:
                M+=1
        else:
            u = uniform(-5,0)
            if u >= f_val:
                M-=1
    print(M)
    return M/n*4/3*pi*R*R*R*5

print(triple_sphere_integral_MC(10000000,f1))

def f2(x,y):
    return exp(x+y)

def double_integral_circle(n,f):
    M = 0
    for i in range(n):
        #x = uniform(-1,1)
        #y = uniform(-sqrt(1-x*x),sqrt(1-x*x)) #not uniform, doesnt work (higher density around x=+-1)

        r = sqrt(uniform(0,1))        #
        phi = uniform(0,2*pi)
        x = r*cos(phi)
        y = r*sin(phi)                #


        f_val = f(x,y)

        #print(x,y,f_val)
        if f_val >= 0:
            u = uniform(0,10)
            if u <= f_val:
                M+=1
        elif f_val < 0:
            u = uniform(-10,0)
            if u >= f_val:
                M-=1
    print(M/n)
    return (M/n)*pi*10
#print(double_integral_circle(1000000,f2))

def f3(x):
    return exp(x)+x**2

def integral_1dim(n,f):
    M=0
    for i in range(n):
        x = uniform(-1,1)
        f_val = f(x)
        if f_val >= 0:
            u = uniform(0,10)
            if u <= f_val:
                M+=1
        elif f_val < 0:
            u = uniform(-10,0)
            if u >= f_val:
                M-=1
    print(M/n)
    return (M/n)*2*10

#print(integral_1dim(10000000,f3))
    

    
        
