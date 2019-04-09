from mpmath import *
from sympy import *

def k_1(func, k, n, f, t0):

    for i in range(k, n+1):
        k0 = func.subs([(y,f[0]),(t,t0)])
        y_prox = f[0] + h* k0
        f[0] = y_prox
        print (str(i) + ' ' + str(y_prox))
        t0=t0+h

def k_2(func, k, n, f, t0):

    for i in range(k, n+1):
        k0 = (3/float(2))*func.subs([(y,f[1]),(t,t0)])
        k1 = (1/float(2))*func.subs([(y,f[0]),(t,t0-h)])
        y_prox = f[1] + h* (k0 - k1)
        f[0] = f[1]
        f[1] = y_prox
        print (str(i) + ' ' + str(y_prox))
        t0=t0+h

def k_3(func, k, n, f, t0):

    for i in range(k, n+1):
        k0 = (23/float(12))*func.subs([(y,f[2]),(t,t0)])
        k1 = (4/float(3))*func.subs([(y,f[1]),(t,t0-h)])
        k2 = (5/float(12))*func.subs([(y,f[0]),(t,t0-h*2)])
        y_prox = f[2] + h*(k0 - k1 + k2)
        f[0] = f[1]
        f[1] = f[2]
        f[2] = y_prox
        print (str(i) + ' ' + str(y_prox))
        t0=t0+h

def k_4(func, k, n, f, t0):

    for i in range(k, n+1):
        k0 = (55/float(24))*func.subs([(y,f[3]),(t,t0)])
        k1 = (59/float(24))*func.subs([(y,f[2]),(t,t0-h)])
        k2 = (37/float(24))*func.subs([(y,f[1]),(t,t0-h*2)])
        k3 = (3/float(8))*func.subs([(y,f[0]),(t,t0-h*3)])
        y_prox = f[3] + h*(k0 - k1 + k2 - k3)
        f[0] = f[1]
        f[1] = f[2]
        f[2] = f[3]
        f[3] = y_prox
        print (str(i) + ' ' + str(y_prox))
        t0=t0+h

def k_5(func, k, n, f, t0):

    for i in range(k, n+1):
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

def k_6(func, k, n, f, t0):

    for i in range(k, n+1):
        k0 = (4277/float(1440))*func.subs([(y,f[5]),(t,t0)])
        k1 = (2641/float(480))*func.subs([(y,f[4]),(t,t0-h)])
        k2 = (4991/float(720))*func.subs([(y,f[3]),(t,t0-h*2)])
        k3 = (3649/float(720))*func.subs([(y,f[2]),(t,t0-h*3)])
        k4 = (959/float(480))*func.subs([(y,f[1]),(t,t0-h*4)])
        k5 = (95/float(288))*func.subs([(y,f[0]),(t,t0-h*5)])
        y_prox = f[5] + h*(k0 - k1 + k2 - k3 + k4 - k5)
        f[0] = f[1]
        f[1] = f[2]
        f[2] = f[3]
        f[3] = f[4]
        f[4] = f[5]
        f[5] = y_prox
        print (str(i) + ' ' + str(y_prox))
        t0=t0+h
    
def k_7(func, k, n, f, t0):

    for i in range(k, n+1):
        k0 = (198721/float(60480))*func.subs([(y,f[6]),(t,t0)])
        k1 = (18637/float(2520))*func.subs([(y,f[5]),(t,t0-h)])
        k2 = (235183/float(20160))*func.subs([(y,f[4]),(t,t0-h*2)])
        k3 = (10754/float(945))*func.subs([(y,f[3]),(t,t0-h*3)])
        k4 = (135713/float(20160))*func.subs([(y,f[2]),(t,t0-h*4)])
        k5 = (5603/float(2520))*func.subs([(y,f[1]),(t,t0-h*5)])
        k6 = (19187/float(60480))*func.subs([(y,f[0]),(t,t0-h*6)])
        y_prox = f[6] + h*(k0 - k1 + k2 - k3 + k4 - k5 + k6)
        f[0] = f[1]
        f[1] = f[2]
        f[2] = f[3]
        f[3] = f[4]
        f[4] = f[5]
        f[5] = f[6]
        f[6] = y_prox
        print (str(i) + ' ' + str(y_prox))
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
for i in range(0, k):
    k1 = func.subs([(y,y0),(t,t0)])
    k2 = func.subs([(y,y0 +0.5*h*k1),(t,t0+0.5*h)])
    k3 = func.subs([(y,y0 +0.5*h*k2),(t,t0+0.5*h)])
    k4 = func.subs([(y,y0 +h*k3),(t,t0+h)])
    y0 = y0 + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
    f.append(y0)
    t0=t0+h
    print(str(i) + ' ' + str(y0))


if(k==2):
    k_1(func, k, n, f, t0)
elif(k==3):
    k_2(func, k, n, f, t0)
elif(k==4):
    k_3(func, k, n, f, t0)
elif(k==5):
    k_4(func, k, n, f, t0)
elif(k==6):
    k_5(func, k, n, f, t0)
elif(k==7):
    k_6(func, k, n, f, t0)
elif(k==8):
    k_7(func, k, n, f, t0)
    
