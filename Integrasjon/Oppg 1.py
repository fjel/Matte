import math

# Øving 1


### Felles verdier/funksjoner ###
# Setter pi
pi = math.pi

def numeriskintegral():
	# Brukte den gule blobben på s.632 for å lage funksjonen
	# Regner ut deltax
	deltax = intervall/delintervaller
	# print("▲X = "+str(deltax))
	# i = sum av alle f(Xn)
	i = 0
	# x er teller for while funksjonen
	x = 0
	# simpel variabel for å regne halve av første gang
	s = 0
	while x <= intervall:
		# veldig simpel if for å sjekke om det er X0
		if s == 0:
			s = 1
			i = i + ((1/2)*(f(x)))
		else:
			# print(f(x))
			i = i + f(x)
			#i = i + (((f(x)+f(x+deltax)))*deltax)
		x = x + deltax
	# Istedet for å sjekke om en verdi var den siste i while loopen, så trekk fra siste lagt til verdi
	nsx = x-deltax
	i = i - f(nsx)
	# Legger til halvparten av siste f(x)
	i = i + ((1/2)*f(intervall))
	return(i*(deltax))

def analytiskintegral():
	# Brukte den gule blobben på s.612 for å lage funksjonen
	return F(intervall)-F(0)





### Oppgaver ###

# a)
print("\n")
print("Oppgave a) \n")
# Funksjonen f()
def f(x):
	return math.sin(x)
# Antideriverte funksjonen F() til f()
def F(x):
	return (-math.cos(x))
# intervall = [0,pi/7]
intervall = ((pi/7)-0)



print("Printer integraler løst numerisk med forskjellige delintervaller: ")
delintervaller = 100
print("Delintervall på "+str(delintervaller)+" gir: "+str(numeriskintegral()))
delintervaller = 1000
print("Delintervall på "+str(delintervaller)+" gir: "+str(numeriskintegral()))
delintervaller = 10000
ni = numeriskintegral(); print("Delintervall på "+str(delintervaller)+" gir: "+str(ni))

print("Printer integral løst analytisk: ")
ai = analytiskintegral(); print(ai)

# Forskjellen på analytiske og numeriske:
print("Forskjell: "+str(ai-ni)+" ("+str(ai/ni)+"%)")
	







# b)
print("\n\n")
print("Oppgave b) \n")
# Funksjonen f()
def f(x):
	return x*math.sin(x)
# Antideriverte funksjonen F() til f()
def F(x):
	return -x*math.cos(x)+math.sin(x)
# intervall = [0,pi/7]
intervall = ((pi/7)-0)

print("Printer integraler løst numerisk med forskjellige delintervaller: ")
delintervaller = 100
print("Delintervall på "+str(delintervaller)+" gir: "+str(numeriskintegral()))
delintervaller = 1000
print("Delintervall på "+str(delintervaller)+" gir: "+str(numeriskintegral()))
delintervaller = 10000
print("Delintervall på "+str(delintervaller)+" gir: "+str(numeriskintegral()))

print("Printer integral løst analytisk: ")
ai = analytiskintegral(); print(ai)

# Forskjellen på analytiske og numeriske:
print("Forskjell: "+str(ai-ni)+" ("+str(ai/ni)+"%)")







# c)
print("\n\n")
print("Oppgave c) \n")
# Funksjonen f()
def f(x):
	return x*math.sin((x*x))
# Antideriverte funksjonen F() til f()
def F(x):
	return -x*math.cos(x)+math.sin(x)
# intervall = [0,pi/7]
intervall = ((pi/7)-0)

print("Printer integraler løst numerisk med forskjellige delintervaller: ")
delintervaller = 100
print("Delintervall på "+str(delintervaller)+" gir: "+str(numeriskintegral()))
delintervaller = 1000
print("Delintervall på "+str(delintervaller)+" gir: "+str(numeriskintegral()))
delintervaller = 10000
print("Delintervall på "+str(delintervaller)+" gir: "+str(numeriskintegral()))


print("Printer integral løst analytisk: ")
ai = analytiskintegral(); print(ai)

# Forskjellen på analytiske og numeriske:
print("Forskjell: "+str(ai-ni)+" ("+str(ai/ni)+"%)")
