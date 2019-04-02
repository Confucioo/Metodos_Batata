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
    y0 = y0+h*k1
    t0=t0+h
    print(str(i) + ' ' + str(y0))
print('\n\n')




