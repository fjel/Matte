# import scipy
import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
	# Selve funksjonen
	return math.pow(x,5)-math.pow(x,4)-3*math.pow(x,2)+x


def f_(x):
	# Deriverte av funksjonen
	# 5x^4-4x^3-6x
	return 5*math.pow(x,4)-4*math.pow(x,3)-6*x

def newrap(): # Newton Raphsons metode
	# Når Xn+1 = Xn - ( f(Xn) / f'(Xn) ) så har man funnet ett nullpunkt
	nullpunkter = [] # Array med nullpunkene
	for x in range(0,10): # Går igjennom 0-10 n startverdier
		tall = x # Startverdi
		for x in range(1,500): # Går igjennom 500 ganger for å gjette seg fram til nullpunkt
			try:
				side2 = tall-(f(tall)/f_(tall))
			except ZeroDivisionError: # Error handling om vi deler på null, skal vi få null
				side2 = tall-0
			if side2 == tall: # Om likningen er lik på begge sider
				if tall in nullpunkter:
					break # Om den allerde har funnet dette nullpunktet, går vi tilbake
				else:
					print('Fant nullpunkt: '+'X: '+str(tall)+' Y: 0') # Vi fant ett nytt nullpunkt
					nullpunkter.append(tall)
					break
			tall = side2 # Setter Xn til svaret


def maksverdi(start_v,slutt_v):
	# 5x^4-4x^3-6x = 5x^2(x-1.4065)(x-0)
	# X = 1.4065 og X = 0 er stasjonære punkter
	# Finner først y-verdi av de stasjonære punktene
	minmaksarray = []
	punkt_a = [0,14065,start_v,slutt_v]
	y0 = f(0)
	y1 = f(1.4065)
	minmaksarray.append(y0)
	minmaksarray.append(y1)
	minmaksarray.append(f(start_v))
	minmaksarray.append(f(slutt_v))
	maxval = max(minmaksarray)
	print('Globalt maks i: X='+str(punkt_a[minmaksarray.index(maxval)])+' , Y='+str(maxval))
	minval = min(minmaksarray)
	print('Globalt min i: X='+str(punkt_a[minmaksarray.index(minval)])+' , Y='+str(minval))


# Graf
x = np.linspace(-1,2,30)
y1 = x**5-x**4-3*x**2+x
y2 = 0*x+0
plt.plot(x,y1,'bo-')
plt.plot(x,y2,'r--')
# plt.show()

print('Oppgave 1 b)')
print()
newrap()
# input("Trykk enter for neste oppgave...")
print()
print('Oppgave 1 c)')
print()
maksverdi(-1,2)
