import numpy as np
import matplotlib.pyplot as plt

def f1(t, z, a1, a2, p): # mutualism, unbounded growth
    x, y = z
    return x*(1-x+a1*y), p*y*(1-y+a2*x)


fig = plt.figure(figsize=(10,10))
a1 = 1
a2 = 2
p = 1
X, Y = np.meshgrid(np.arange(0, 4, 0.2), np.arange(0, 4, 0.2))
U, V, = f1(0, (X,Y), a1, a2, p)
denom = np.sqrt(U**2 + V**2)
denom[denom==0]=0.000000000001
U = U / denom
V = V / denom

plt.quiver(X,Y,U,V, color='blue')
x1 = np.arange(0,1.5,0.1)
y1 = 1+a2*x1
x2 = np.arange(1,4,0.1)
y2 = (1-x2)/(-a1)
plt.plot(x1, y1, color='r')
plt.plot(x2, y2, color='r')
plt.show()


def f2(t, z, a1, a2, p): # mutualism, unbounded growth
    x, y = z
    return x*(1-x+a1*y), p*y*(1-y+a2*x)


fig = plt.figure(figsize=(10,10))
a1 = 0.5
a2 = 0.5
p = 1
X, Y = np.meshgrid(np.arange(0, 4, 0.2), np.arange(0, 4, 0.2))
U, V, = f2(0, (X,Y), a1, a2, p)
denom = np.sqrt(U**2 + V**2)
denom[denom==0]=0.000000000001
U = U / denom
V = V / denom

plt.quiver(X,Y,U,V, color='blue')
x1 = np.arange(0, 5)
y1 = 1+a2*x1
x2 = np.arange(1, 4)
y2 = (1-x2)/(-a1)
plt.plot(x1, y1, color='r')
plt.plot(x2, y2, color='r')
plt.show()



def f3(t, z, a1, a2, p): # competition, case 1
    x, y = z
    return x*(1-x-a1*y), p*y*(1-y-a2*x)


fig = plt.figure(figsize=(10,10 ))
a1 = 0.5
a2 = 0.5
p = 1
X, Y = np.meshgrid(np.arange(0, 2, 0.1), np.arange(0, 2, 0.1))
U, V, = f3(0, (X,Y), a1, a2, p)
denom = np.sqrt(U**2 + V**2)
denom[denom==0]=0.000000000001
U = U / denom
V = V / denom

plt.quiver(X,Y,U,V, color='blue')
x1 = np.arange(0, 3)
y1 = 1-a2*x1
x2 = np.arange(0, 2)
y2 = (1-x2)/(a1)
plt.plot(x1, y1, color='r')
plt.plot(x2, y2, color='r')
plt.show()


def f4(t, z, a1, a2, p): # competition, case 2
    x, y = z
    return x*(1-x-a1*y), p*y*(1-y-a2*x)


fig = plt.figure(figsize=(10,10))
a1 = 1.4
a2 = 1.4
p = 1
X, Y = np.meshgrid(np.arange(0, 2, 0.1), np.arange(0, 2, 0.1))
U, V, = f4(0, (X,Y), a1, a2, p)
denom = np.sqrt(U**2 + V**2)
denom[denom==0]=0.000000000001
U = U / denom
V = V / denom

plt.quiver(X,Y,U,V, color='blue')
x1 = np.arange(0, 0.8,0.05)
y1 = 1-a2*x1
x2 = np.arange(0, 1,0.1)
y2 = (1-x2)/(a1)
plt.plot(x1, y1, color='r')
plt.plot(x2, y2, color='r')
plt.show()


def f5(t, z, a1, a2, p): # competition, case 3
    x, y = z
    return x*(1-x-a1*y), p*y*(1-y-a2*x)


fig = plt.figure(figsize=(10,10))
a1 = 0.5
a2 = 1.5
p = 1
X, Y = np.meshgrid(np.arange(0, 2, 0.1), np.arange(0, 2, 0.1))
U, V, = f5(0, (X,Y), a1, a2, p)
denom = np.sqrt(U**2 + V**2)
denom[denom==0]=0.000000000001
U = U / denom
V = V / denom

plt.quiver(X,Y,U,V, color='blue')
x1 = np.arange(0, 0.7,0.05)
y1 = 1-a2*x1
x2 = np.arange(0, 1.1,0.1)
y2 = (1-x2)/(a1)
plt.plot(x1, y1, color='r')
plt.plot(x2, y2, color='r')
plt.show()

def f6(t, z, a1, a2, p): # competition, case 4
    x, y = z
    return x*(1-x-a1*y), p*y*(1-y-a2*x)


fig = plt.figure(figsize=(10,10))
a1 = 1.1
a2 = 0.5
p = 1
X, Y = np.meshgrid(np.arange(0, 2, 0.1), np.arange(0, 2, 0.1))
U, V, = f6(0, (X,Y), a1, a2, p)
denom = np.sqrt(U**2 + V**2)
denom[denom==0]=0.000000000001
U = U / denom
V = V / denom
plt.quiver(X,Y,U,V, color='blue')
x1 = np.arange(0, 2,0.05)
y1 = 1-a2*x1
x2 = np.arange(0, 1.1,0.1)
y2 = (1-x2)/(a1)
plt.plot(x1, y1, color='r')
plt.plot(x2, y2, color='r')
plt.show()


def f7(t, z, a, b, d): # realistic LV
    x, y = z
    return x*(1-x)-((a*x*y)/(x+d)), b*y*(1-(y/x))


fig = plt.figure(figsize=(10,10))
a = 1 
b = 1 #change this for bifurcation
d = 0.2
X, Y = np.meshgrid(np.arange(0, 1, 0.05), np.arange(0,1, 0.05))
U, V, = f7(0, (X,Y), a, b, d)
denom = np.sqrt(U**2 + V**2)
denom[denom==0]=0.000000000001
U = U / denom
V = V / denom
plt.quiver(X,Y,U,V, color='blue')
# x1 = np.arange(0, 2,0.05)
# y1 = 1-a2*x1
# x2 = np.arange(0, 1.1,0.1)
# y2 = (1-x2)/(a1)
#plt.plot(x1, y1, color='r')
#plt.plot(x2, y2, color='r')
plt.show()
