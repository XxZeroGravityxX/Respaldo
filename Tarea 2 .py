
# coding: utf-8

# In[11]:

#P1 Tarea 2
from scipy.optimize import bisect as bi
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def raiz(f,h): #funcion para detectar ceros de una función con paso h para encontrar donde f(x)<0 y f(x)>0, para asi obtener a y b que necesita la funcion bisect de scipy
    contador=0
    while f(contador)>=0: #asume que la funcion es positiva y busca hasta que contador no lo es
        contador+=h
    return bi(f,contador-h,contador)
def altyvelocidad(omega,eta,yi,vi): #obtiene altura y velocidad de la pelota en el rebote n-esimo
    g=1
    A=1
    y0=yi
    v0=vi
    yp=lambda t:y0+v0*t-g*(t**2)/2.0 #altura de la pelota
    vp=lambda t:v0-g*t #velocidad de la pelota
    ys=lambda t:A*np.sin(omega*t+np.arcsin(y0)) #altura del suelo
    vs=lambda t:A*omega*np.cos(omega*t+np.arcsin(y0))
    vpantes=lambda t:vp(t) #velocidad de la pelota justo antes del choque (en t=t*)
    vpdespues=lambda t:(1+eta)*vs(t)-eta*vpantes(t) #velocidad de la pelota justo despues del choque (en t=t*)
    fraiz=lambda t:y0+v0*t-g*(t**2)/2.0 - A*np.sin(omega*t+np.arcsin(y0)) #funcion a la cual se le busca la raiz (yp-ys)
    traiz=raiz(fraiz,0.001) #busca tiempo* donde ocurre el choque
    altp=yp(traiz) #altura de la pelota en el instante del choque
    velpdespues=vpdespues(traiz) #velocidad de la pelota justo despues del choque
    print traiz
    return altp,velpdespues
print (altyvelocidad(1.66,0.15,0,10))
'''
#P2 Tarea 2

#eta=0.15 define la disipacion de energia en el choque (si eta es pequeño alcanza el numero de rebotes para la estabilizacion en pocos rebotes)
#omega=1.66
fig=plt.figure(1)
fig.clf
fig.set_size_inches(16, 8, forward=True)
n=np.linspace(0,20,num=21)
y0=0
v0=10
vpn=[]
for i in n:
    yi=y0
    vi=v0
    vpn.append(vi)
    y0=(altyvelocidad(1.66,0.15,yi,vi))[0]
    v0=(altyvelocidad(1.66,0.15,yi,vi))[1]
plt.plot(n,vpn,'r-')
plt.ylabel(r'Velocidad justo despues del choque $[\frac{m}{s}]$')
plt.xlabel(r'Numero de rebotes $[unidades]$')
plt.title('Velocidad vs numero de rebotes')
plt.grid(True)
plt.savefig('vpnvsn')
plt.show()

#P3 Tarea 2

#omega=1.68 y 1.7
#eta=0.15
n=np.linspace(0,50,num=51)
vpna=[]
vpnb=[]
y0a=0
v0a=10
y0b=0
v0b=10
for i in n:
    yia=y0a
    via=v0a
    yib=y0b
    vib=v0b
    vpna.append(via)
    vpnb.append(vib)
    y0a=(altyvelocidad(1.68,0.15,yia,via))[0]
    v0a=(altyvelocidad(1.68,0.15,yia,via))[1]
    y0b=(altyvelocidad(1.7,0.15,yib,vib))[0]
    v0b=(altyvelocidad(1.7,0.15,yib,vib))[1]
fig=plt.figure(1)
fig.clf
fig.set_size_inches(16, 8, forward=True)
plt.plot(n,vpna,'r-')#Primer grafico
plt.ylabel(r'Velocidad justo despues del choque $[\frac{m}{s}]$')
plt.xlabel(r'Numero de rebotes $[unidades]$')
plt.title('Velocidad vs numero de rebotes')
red_patch = mpatches.Patch(color='red', label=r'$\omega =1.68$')
plt.plot(n,vpnb,'b-')#Segundo grafico
plt.ylabel(r'Velocidad justo despues del choque $[\frac{m}{s}]$')
plt.xlabel(r'Numero de rebotes $[unidades]$')
plt.title('Velocidad vs numero de rebotes')
blue_patch = mpatches.Patch(color='blue', label=r'$\omega =1.7$')
plt.legend(handles=[red_patch,blue_patch])
plt.grid(True)
plt.savefig('vpnvsnp3')
'''
#P4 Tarea 2

#eta=0.15 define la disipacion de energia en el choque (si eta es pequeño alcanza el numero de rebotes para la estabilizacion en pocos rebotes)
#1.66<=omega<=1.79
fig=plt.figure(1)
fig.clf
fig.set_size_inches(16, 8, forward=True)
nrelax=2
n=[]
for j in range(50):
    n.append(2*nrelax+j)
y0=0
v0=10
numomegas=20
omegas=np.linspace(1.66,1.79,num=numomegas)
vpn=np.zeros((numomegas,50))
rebote=0
contomega=0
for h in omegas:
    j=0
    for i in n:
        yi=y0
        vi=v0
        while rebote<=i:
            y0=(altyvelocidad(h,0.15,yi,vi))[0]
            v0=(altyvelocidad(h,0.15,yi,vi))[1]
            rebote+=1
        vpn[contomega][j]=v0
        j+=1
    contomega+=1
for i in range(50):
    plt.plot(omegas,vpn[:,i],'r-')
plt.ylabel(r'Velocidad justo despues del choque $[\frac{m}{s}]$')
plt.xlabel(r'Frecuencia angular $[radianes]$')
plt.title('Velocidad vs frecuencia angular')
plt.grid(True)
plt.savefig('vpnvsomega')
plt.show()





# In[ ]:



