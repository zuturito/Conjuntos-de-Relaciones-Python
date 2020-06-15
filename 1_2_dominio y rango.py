from sympy import *
from fractions import *
from sympy import Symbol, S
from sympy.calculus.util import continuous_domain
import math

x = Symbol("x")
f = 1/x-2
z = continuous_domain(f, x, S.Reals)

def dominio_rango(R):
	x = []
	y = []
	for a, b in R:
		x.append(a)
		y.append(b)
	return "El dominio es: ", sorted(set(x), key=x.index)," El rango es: ", sorted(set(y), key=y.index)



print("En caso de ingresar una relación el dominio y rango estarán definidos por sus ejes X y Y")
print("Relación ingresada")
print("[(1,1), (1,2), (2,3), (4,2)]")
print(dominio_rango([(1,1), (1,2), (2,3), (4,2)]))