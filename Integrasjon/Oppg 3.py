import math

delintervaller = 100000
# Areal
def areal():
    intervall = b - a
    deltax = intervall/delintervaller
    i = 0
    x = a
    s = 0
    while x <= intervall:
        if s == 0:
            s = 1
            i = i + ((1/2)*(f(x)))
        else:
            i = i + f(x)
        x = x + deltax
    nsx = x-deltax
    i = i - f(nsx)
    i = i + ((1/2)*f(intervall))
    return(i*(deltax))


def areal2():
    intervall = b - a
    deltax = intervall/delintervaller
    i = 0
    x = a
    s = 0
    while x <= intervall:
        i = i + (f(x)*deltax)
        x = x + deltax
    return i


def f(x):
    #return (3*(x*x))-3
    return ((x*x)-(4*x)+3)
    #return (x*x*x)+(6*(x*x))-(3*x)+1
    #return (2*x)+3
a = 1
b = 3
print(areal2())
