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
f=[]
print('h = '+str(h))
print('t0 = '+str(t0))
for i in range(0, 5):
   
    print (str(i) + ' ' + str(y0))
    k1 = func.subs([(y,y0),(t,t0)])
    y0 = y0+h*k1
    f.append(y0)
    t0=t0+h


for i in range(5, n+1):
    fy3 = (3/8.)* func.subs([(y,fy3),(t,t0)])
    fy2 = (19/24.)*func.subs([(y,f[2]),(t,t0-h)])
    fy1 = (-5/24.)*func.subs([(y,f[1]),(t,t0-h*2)])
    fy0 = (1/24.)*func.subs([(y,f[0]),(t,t0-h*3)])

    y_prox = f[3] + h * (fy3 + fy2 - fy1 + fy0)

    f[0] = f[1]
    f[1] = f[2]
    f[2] = f[3]
    f[3] = y_prox
    print (str(i) + ' ' + str(y_prox))
    t0 = t0+h
    
