from mpmath import *
from sympy import *

arq = open('entrada.txt', 'r')

texto = arq.readline()
arq.close()


lista = texto.split()


print(lista[5])

y0, t0, h0, n, func = sympify(lista[1]), sympify(lista[2]), sympify(lista[3]), sympify(lista[4]), sympify(lista[5])
y, t, h = symbols("y t h")

t0 = t0+h0
for i in range(1,n+1):
    b = y0+h*func
    c = solveset(Eq(y,b),y)
    d = c.subs([(h,h0),(t,t0)])
    y0 = d.args[0]
    print(str(t0) + ' ' + str(y0))
    t0 = t0+h0
