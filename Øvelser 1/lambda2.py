import math
import numpy as np
import matplotlib.pyplot as plt


# Oppgave 2 a)
# λ er nå satt til 2.95

# i)

l = lambda t: 2.95*t*(1-t)

t_v = [] # Array for funksjonsverdiene som skal til grafen
startt = 0.4 # Tilfeldig start t mellom (0,1)
for x in range(0,70): # Går igjennom 70 ganger
	nyt = l(startt) # Regner ut lambda funksjonen
	startt = nyt # Setter svaret av lambda funksjonen til t
	t_v.append(nyt) # legger til funksjonsverdien til arrayet


x = np.linspace(0,1,70)
lar = np.asarray(t_v)
y1 = l(lar)
y2 = 0*x # rett linje
plt.plot(x,y1,'b--')
plt.plot(x,y2,'r--')
plt.show()


# ii)
# Nå kjører vi den igjen, opp til 1000, for å finne ut hva verdien nærmer seg
print('Oppgave ii):')

startt = 0.4
for x in range(0,1000):
	nyt = l(startt)
	if round(nyt,6) == round(startt,6):
		print('Tn naermer seg: '+str(round(nyt,6)))
		break
	startt = nyt