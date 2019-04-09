from mpmath import *
from sympy import *

arq = open('entrada.txt', 'r')

texto = arq.readline()
arq.close()


lista = texto.split()


print(lista[5])

y0, t0, h, n, func = sympify(lista[1]), sympify(lista[2]), sympify(lista[3]), sympify(lista[4]), sympify(lista[5])
y, t, y_prox= symbols("y t y_prox")

for i in range(1,n+1):
    res = y0 + h*func.subs([(y,y_prox),(t,t0+h)]) - y_prox
    y0 = solve(res,y_prox)
    print(str(t0) + ' ' + str(y0))
    t0 = t0+h

