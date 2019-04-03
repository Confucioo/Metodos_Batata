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
    
    


for i in range(6, n+1):
    k0 = (1901/float(720))*func.subs([(y,f[4]),(t,t0)])
    k1 = (1387/float(360))*func.subs([(y,f[3]),(t,t0-h)])
    k2 = (109/float(30))*func.subs([(y,f[2]),(t,t0-h*2)])
    k3 = (637/float(360))*func.subs([(y,f[1]),(t,t0-h*3)])
    k4 = (251/float(720))*func.subs([(y,f[0]),(t,t0-h*4)])
    y_prox = f[4] + h*(k0 - k1 + k2 - k3 + k4)
    f[0] = f[1]
    f[1] = f[2]
    f[2] = f[3]
    f[3] = f[4]
    f[4] = y_prox
    print (str(i) + ' ' + str(y_prox))
    t0=t0+h
    



