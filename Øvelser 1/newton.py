# import scipy
import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
	# Selve funksjonen
	return math.pow(x,5)-math.pow(x,4)-3*math.pow(x,2)+x


def f_(x):
	# Deriverte av funksjonen
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


def maksverdi():
	#finner først topppunkt og bunnpunkt
	#der f'(x) == 0 er det ett stasjonært punkt
	lavestlok_old = 20
	cnt=0
	df = [-1,2]
	dfstart = df[0]*1000
	dfslutt = df[1]*1000
	for x in range(dfstart,dfslutt):
		x = x/1000
		derivert = f_(x)


		# print(derivert)
		# print(abs(derivert_r))
		if  derivert == 0:
			print('stasj.punkt i :'+str(x))

	#punkt i -1
	print('f(-1) = '+str(f(df[0])))
	#punkt i 2
	print('f(2) = '+str(f(df[1])))

# Graf
x = np.linspace(-1,2,30)
y1 = x**5-x**4-3*x**2+x
y2 = 0*x+0
plt.plot(x,y1,'bo-')
plt.plot(x,y2,'r--')
# plt.show()

print('Oppgave 1 b)')
newrap()
# input("Trykk enter for neste oppgave...")
print('Oppgave 1 c)')
maksverdi()

# deriver(2,[2,0,-5])


# print(newtonsqr(256,10))

# print(scipy.optimize.newton())

def test():
		derivert_r = abs(round(f_(x),4))
		lavestlok = derivert_r
		if lavestlok <= lavestlok_old:
			lavestlok_old = lavestlok
			cnt = 0
			# print(synker)
			# print(lavestlok)
		elif cnt != 5:
			cnt = cnt + 1
			# print(cnt)
			if cnt == 2:
				cnt = 5
				stasj_punkt = x-0.002
				print('Stasjonert punkt i x='+str(stasj_punkt))
				print('Med y verdi: ' + str(f(stasj_punkt)))