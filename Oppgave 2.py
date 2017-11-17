import math
import numpy as np
import matplotlib.pyplot as plt

# Oppgave 2
print('Oppgave 2')
print()
# lambda skal være ett reelt tall større enn 0
# Lλ(t) =λt(1−t)
# Df [0,1]
l = lambda t: 1.2*t*(1-t)

t_v = [] # Array for funksjonsverdiene som skal til grafen
startt = 0.4 # Tilfeldig start t mellom (0,1)
for x in range(0,100): # Går igjennom 100 ganger
	nyt = l(startt) # Regner ut lambda funksjonen
	startt = nyt # Setter svaret av lambda funksjonen til t
	t_v.append(nyt)
	if x<10 or x%10 == 0:
		# Printer t verdiene opp til 10, og deretter hver 10'ende t
		print('t'+str(x)+': '+str(nyt))


x = np.linspace(0,1,100)
lar = np.asarray(t_v)
y1 = l(lar)
y2 = 0*x # Rett null linje for 0-referanse
plt.plot(x,y1,'b--')
plt.plot(x,y2,'r--')
plt.show() # Viser grafen

print('Grafen beveger seg mot ett punkt, ca: 0.16666666666666')