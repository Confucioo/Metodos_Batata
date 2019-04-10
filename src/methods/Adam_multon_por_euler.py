from mpmath import *
from sympy import *

def k_6(func, k, n, f, t0):
    y_prox = symbols("y_prox")
    for i in range(k, n+1):
        k0 = (95/float(288))*func.subs([(y,y_prox),(t,t0+h)])
        k1 = (1427/float(1440))*func.subs([(y,f[4]),(t,t0)])
        k2 = (133/float(240))*func.subs([(y,f[3]),(t,t0-h)])
        k3 = (241/float(720))*func.subs([(y,f[2]),(t,t0-h*2)])
        k4 = (173/float(1440))*func.subs([(y,f[1]),(t,t0-h*3)])
        k5 = (3/float(160))*func.subs([(y,f[0]),(t,t0-h*4)])
        res = f[4] + h*(k0 + k1 - k2 + k3 - k4 + k5) - y_prox
        res = solve(res,y_prox)
        f[0] = f[1]
        f[1] = f[2]
        f[2] = f[3]
        f[3] = f[4]
        f[4] = res[0]
        print (str(i) + ' ' + str(f[4]))
        t0=t0+h



arq = open('entrada.txt', 'r')

texto = arq.readline()
arq.close()


lista = texto.split()


print(lista[5])

y0, t0, h, n, func = sympify(lista[1]), sympify(lista[2]), sympify(lista[3]), sympify(lista[4]), sympify(lista[5])
t, y = symbols("t y")
f=[]
k = int(lista[6])
print('Metodo de Euler')

print('h = '+str(h))
for i in range(1, k):
    k1 = func.subs([(y,y0),(t,t0)])
    y0 = y0+h*k1
    f.append(y0)
    print(str(i) + ' ' + str(y0))
    t0=t0+h
    


k_6(func, k, n, f, t0)


