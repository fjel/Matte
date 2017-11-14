# import scipy
import math
import numpy as np
import matplotlib.pyplot as plt

def newtonsqr(n, ganger):
	#Newtons metode for å finne kvadratroter
	gj = 0.5 * n #Gjetter på halvparten
	for i in range(ganger):
		bgj = 0.5 * (gj + n/gj) #bedre gjetting
		if bgj == gj:
			break
		else:
			gj = bgj
	return gj

tall=[]

def deriver(grad,tall):
	#Derivere ett tall, fungerer ikke
	deriv = ''
	grader = list(reversed(range(grad+1)))
	for x in range(grad+1):
		if tall[x] != 0:
			xv = tall[x]*grader[x]
			if grader[x] != grad:
				xv = str(xv)
			if grader[x]-1 >= 1: #Om graden minus en blir mindre enn en, skal det ikke legges til x
				if grader[x]-1 >= 2:
					xv = str(xv) + 'x**'+grader[x]-1
				else:
					xv = str(xv) + 'x'
			deriv = deriv + str(xv)

	print(deriv)


def f(x):
	#Funksjonen
	return math.pow(x,5)-math.pow(x,4)-3*math.pow(x,2)+x

def f_(x):
	#Deriverte av funksjonen
	return 5*math.pow(x,4)-4*math.pow(x,3)-6*x


def newrap():
	#Newton Raphsons metode
	#Når Xn+1 = Xn - ( f(Xn) / f'(Xn) ) så har man funnet ett nullpunkt
	nullpunkter = []
	for x in range(-10,10):
		tall = x # startverdi
		if tall == 0:
			tall = 0.030
		for x in range(1,500): # Går igjennom 500 ganger
			# side2 = tall-(((tall**3)-(2*tall)-(5))/((3*tall**2)-2))
			side2 = tall-(f(tall)/f_(tall))
			# print(side2)
			if side2 == tall: # Om likningen er lik på begge sider
				if tall in nullpunkter:
					break
				else:
					print('Fant nullpunkt:')
					print(str(tall)+'='+str(tall))
					nullpunkter.append(tall)
					break
			tall = side2 # Setter Xn til 


x = np.linspace(-5,5)
y1 = x**5-x**4-3*x**2+x
y2 = 0*x+0
plt.plot(x,y1,'bo-')
plt.plot(x,y2,'r--')
plt.show()

newrap()


# deriver(2,[2,0,-5])


# print(newtonsqr(256,10))

# print(scipy.optimize.newton())