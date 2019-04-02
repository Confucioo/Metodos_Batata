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
for i in range(1, 7):
    k1 = func.subs([(y,y0),(t,t0)])
    y0 = y0+h*k1
    t0=t0+h
    f.append(y0)
    print (str(i) + ' ' + str(y0))

print (f[5])
for i in range(7, n+1):
    y_prox = f[5] + h*(((4277/1440)*func.subs([(y,f[5]),(t,t0)])) - ((2641/480)*func.subs([(y,f[4]),(t,t0-1)])) + ((4991/720)*func.subs([(y,f[3]),(t,t0-2)])) - ((3649/720)*func.subs([(y,f[2]),(t,t0-3)])) + ((959/480)*func.subs([(y,f[1]),(t,t0-4)])) - ((95/288)*func.subs([(y,f[0]),(t,t0-5)])))
    f[0] = f[1]
    f[1] = f[2]
    f[2] = f[3]
    f[3] = f[4]
    f[4] = f[5]
    f[5] = y_prox
    t0=t0+h
    print (str(i) + ' ' + str(y_prox))



