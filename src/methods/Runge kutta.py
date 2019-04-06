from mpmath import *
from sympy import *

arq = open('entrada.txt', 'r')

texto = arq.readline()
arq.close()


lista = texto.split()


print(lista[5])

y0, t0, h, n, func = sympify(lista[1]), sympify(lista[2]), sympify(lista[3]), sympify(lista[4]), sympify(lista[5])
t, y = symbols("t y")


print('Metodo de Euler')

print('h = '+str(h))
for i in range(1, n+1):
    k1 = func.subs([(y,y0),(t,t0)])
    k2 = func.subs([(y,y0 +0.5*h*k1),(t,t0+0.5*h)])
    k3 = func.subs([(y,y0 +0.5*h*k2),(t,t0+0.5*h)])
    k4 = func.subs([(y,y0 +h*k3),(t,t0+h)])
    y0 = y0 + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
    t0=t0+h
    print(str(i) + ' ' + str(y0))
print('\n\n')




