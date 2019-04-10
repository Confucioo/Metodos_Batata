from mpmath import *
from sympy import *


def k_2(func, k, n, f, t0):
    y_prox = symbols("y_prox")
    for i in range(k, n+1):
        k0 = (95/float(288))*func.subs([(y,y_prox),(t,t0+h)])
        k1 = (1427/float(1440))*func.subs([(y,f[0]),(t,t0)])
        res = f[0] + h*(k0 + k1) - y_prox
        res = solve(res,y_prox)
        f[0] = res[0]
        print (str(i) + ' ' + str(f[0]))
        t0=t0+h

def k_3(func, k, n, f, t0):
    y_prox = symbols("y_prox")
    for i in range(k, n+1):
        k0 = (95/float(288))*func.subs([(y,y_prox),(t,t0+h)])
        k1 = (1427/float(1440))*func.subs([(y,f[1]),(t,t0)])
        k2 = (133/float(240))*func.subs([(y,f[0]),(t,t0-h)])
        res = f[1] + h*(k0 + k1 - k2) - y_prox
        res = solve(res,y_prox)
        f[0] = f[1]
        f[1] = res[0]
        print (str(i) + ' ' + str(f[1]))
        t0=t0+h

def k_4(func, k, n, f, t0):
    y_prox = symbols("y_prox")
    for i in range(k, n+1):
        k0 = (95/float(288))*func.subs([(y,y_prox),(t,t0+h)])
        k1 = (1427/float(1440))*func.subs([(y,f[2]),(t,t0)])
        k2 = (133/float(240))*func.subs([(y,f[1]),(t,t0-h)])
        k3 = (241/float(720))*func.subs([(y,f[0]),(t,t0-h*2)])
        res = f[2] + h*(k0 + k1 - k2 + k3) - y_prox
        res = solve(res,y_prox)
        f[0] = f[1]
        f[1] = f[2]
        f[2] = res[0]
        print (str(i) + ' ' + str(f[2]))
        t0=t0+h

def k_5(func, k, n, f, t0):
    y_prox = symbols("y_prox")
    for i in range(k, n+1):
        k0 = (95/float(288))*func.subs([(y,y_prox),(t,t0+h)])
        k1 = (1427/float(1440))*func.subs([(y,f[3]),(t,t0)])
        k2 = (133/float(240))*func.subs([(y,f[2]),(t,t0-h)])
        k3 = (241/float(720))*func.subs([(y,f[1]),(t,t0-h*2)])
        k4 = (173/float(1440))*func.subs([(y,f[0]),(t,t0-h*3)])
        res = f[3] + h*(k0 + k1 - k2 + k3 - k4) - y_prox
        res = solve(res,y_prox)
        f[0] = f[1]
        f[1] = f[2]
        f[2] = f[3]
        f[3] = res[0]
        print (str(i) + ' ' + str(f[3]))
        t0=t0+h

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

def k_7(func, k, n, f, t0):
    y_prox = symbols("y_prox")
    for i in range(k, n+1):
        k0 = (19087/float(60480))*func.subs([(y,y_prox),(t,t0+h)])
        k1 = (2713/float(2520))*func.subs([(y,f[5]),(t,t0)])
        k2 = (15487/float(20160))*func.subs([(y,f[4]),(t,t0-h)])
        k3 = (586/float(945))*func.subs([(y,f[3]),(t,t0-h*2)])
        k4 = (6737/float(20160))*func.subs([(y,f[2]),(t,t0-h*3)])
        k5 = (263/float(2520))*func.subs([(y,f[1]),(t,t0-h*4)])
        k6 = (863/float(60480))*func.subs([(y,f[0]),(t,t0-h*5)])
        res = f[5] + h*(k0 + k1 - k2 + k3 - k4 + k5 - k6) - y_prox
        res = solve(res,y_prox)
        f[0] = f[1]
        f[1] = f[2]
        f[2] = f[3]
        f[3] = f[4]
        f[4] = f[5]
        f[5] = res[0]
        print (str(i) + ' ' + str(f[5]))
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
print('Adams Moulton por euler')

print('h = '+str(h))
for i in range(1, k):
    k1 = func.subs([(y,y0),(t,t0)])
    y0 = y0+h*k1
    f.append(y0)
    print(str(i) + ' ' + str(y0))
    t0=t0+h
    


if(k==2):
    k_2(func, k, n, f, t0)
elif(k==3):
    k_3(func, k, n, f, t0)
elif(k==4):
    k_4(func, k, n, f, t0)
elif(k==5):
    k_5(func, k, n, f, t0)
elif(k==6):
    k_6(func, k, n, f, t0)
elif(k==7):
    k_7(func, k, n, f, t0)
elif(k==8):
    k_8(func, k, n, f, t0)


