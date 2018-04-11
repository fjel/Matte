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
    while x < b:
        i = i + (f(x)*deltax)
        x = x + deltax
    return i


def f(x):
    return (1/(x*x))
a = 1
b = math.inf
print(areal2())
