# import scipy
import math

def newtonsqr(n, ganger):
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
	return math.pow(x,5)-math.pow(x,4)-3*math.pow(x,2)+x

def f_(x):
	#deriverte av f
	return 5*math.pow(x,4)-4*math.pow(x,3)-6*x


def newrap():
	for x in range(1,500):
		# side2 = tall-(((tall**3)-(2*tall)-(5))/((3*tall**2)-2))
		side2 = tall-(f(tall)/f_(tall))
		print(side2)
		if side2 == tall:
			print('ferdig')
			print(str(tall)+'='+str(tall))
			break
		tall = side2

newrap()

# deriver(2,[2,0,-5])


# print(newtonsqr(256,10))

# print(scipy.optimize.newton())