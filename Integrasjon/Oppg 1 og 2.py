import math

# Øving 1


### Felles verdier/funksjoner ###
# Setter pi
pi = math.pi

intervaller = [100,10000,1000000] # Intervaller på 100, 10 000 og 1 000 000

def numerisktrapes():
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
	# Brukte den gule blobben på s.612 for å lage "funksjonen"
	return F(intervall)-F(0)

def numeriskintegral():
	# Brukte s.606 for å lage funksjonen
	deltax = intervall/delintervaller
	i = 0
	x = 0
	s = 0
	while x <= intervall:
		i = i + (f(x)*deltax)
		x = x + deltax
	return i



### Oppgave 1 ###

# a)
print("\n")
print("Oppgave a) \n")
def f(x):
	return math.sin(x)
def F(x):
	return (-math.cos(x))
intervall = ((pi/7)-0)


print("Printer integraler løst numerisk med forskjellige delintervaller: ")
for intev in intervaller:
	delintervaller = intev
	ni = numeriskintegral(); print(str(ni)+" ved delintervall på: "+str(delintervaller))

print("Printer integral løst analytisk: ")
ai = analytiskintegral(); print(ai)

forskjt1a = ai-ni; print("Forskjell: "+str(forskjt1a)+" ("+str(ai/ni)+"%)")








# b)
print("\n\n")
print("Oppgave b) \n")
def f(x):
	return x*math.sin(x)
def F(x):
	return -x*math.cos(x)+math.sin(x)

intervall = ((pi/7)-0)

print("Printer integraler løst numerisk med forskjellige delintervaller: ")
for intev in intervaller:
	delintervaller = intev
	ni = numeriskintegral(); print(str(ni)+" ved delintervall på: "+str(delintervaller))

print("Printer integral løst analytisk: ")
ai = analytiskintegral(); print(ai)

forskjt1b = ai-ni; print("Forskjell: "+str(forskjt1b)+" ("+str(ai/ni)+"%)")






# c)
print("\n\n")
print("Oppgave c) \n")
def f(x):
	return x*math.sin((x*x))
def F(x):
	return math.cos(x*x)*(-(1/2))

intervall = ((pi/7)-0)

print("Printer integraler løst numerisk med forskjellige delintervaller: ")
for intev in intervaller:
	delintervaller = intev
	ni = numeriskintegral(); print(str(ni)+" ved delintervall på: "+str(delintervaller))


print("Printer integral løst analytisk: ")
ai = analytiskintegral(); print(ai)

forskjt1c = ai-ni; print("Forskjell: "+str(forskjt1c)+" ("+str(ai/ni)+"%)")








### Oppgave 2 ###

# a)
print("\n")
print("Oppgave a) \n")
def f(x):
	return math.sin(x)
def F(x):
	return (-math.cos(x))

intervall = ((pi/7)-0)


print("Printer integraler løst numerisk med forskjellige delintervaller: ")
for intev in intervaller:
	delintervaller = intev
	ni = numerisktrapes(); print(str(ni)+" ved delintervall på: "+str(delintervaller))

print("Printer integral løst analytisk: ")
ai = analytiskintegral(); print(ai)

forskjt2a = ai-ni; print("Forskjell: "+str(forskjt2a)+" ("+str(ai/ni)+"%)")








# b)
print("\n\n")
print("Oppgave b) \n")
def f(x):
	return x*math.sin(x)
def F(x):
	return -x*math.cos(x)+math.sin(x)
intervall = ((pi/7)-0)

print("Printer integraler løst numerisk med forskjellige delintervaller: ")
for intev in intervaller:
	delintervaller = intev
	ni = numerisktrapes(); print(str(ni)+" ved delintervall på: "+str(delintervaller))

print("Printer integral løst analytisk: ")
ai = analytiskintegral(); print(ai)


forskjt2b = ai-ni; print("Forskjell: "+str(forskjt2b)+" ("+str(ai/ni)+"%)")






# c)
print("\n\n")
print("Oppgave c) \n")
def f(x):
	return x*math.sin((x*x))
def F(x):
	return math.cos(x*x)*(-(1/2))
intervall = ((pi/7)-0)

print("Printer integraler løst numerisk med forskjellige delintervaller: ")
for intev in intervaller:
	delintervaller = intev
	ni = numerisktrapes(); print(str(ni)+" ved delintervall på: "+str(delintervaller))


print("Printer integral løst analytisk: ")
ai = analytiskintegral(); print(ai)


forskjt2c = ai-ni; print("Forskjell: "+str(forskjt2c)+" ("+str(ai/ni)+"%)")

print("\n")
print("Konklusjon øving 1: Resultatene blir veldig like så sant man bruker høye nok delintervaller.")

print("\n")
oppg1gjforskj = ((forskjt1a+forskjt1b+forskjt1c)/3); print ("Gjennomsnittling forskjell mellom numerisk og analytisk i oppgave 1: "+str(oppg1gjforskj))
oppg2gjforskj = ((forskjt2a+forskjt2b+forskjt2c)/3); print ("Gjennomsnittling forskjell mellom numerisk og analytisk i oppgave 2: "+str(oppg2gjforskj))
print("Konklusjon øving 2: Resultatene blir enda likere, og den gjennomsnittlige forskjellen mellom oppgave 1 og 2 er ganske forskjellig, med en gjennomsnittlig økt nøyaktighet på ca: "+str(round(abs(oppg1gjforskj/oppg2gjforskj),4))+" prosent.")
