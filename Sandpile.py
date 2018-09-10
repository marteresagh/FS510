#SANDPILE

import numpy as np
import matplotlib.pyplot as plt

def measure_av(n_iter,tsav):
    n_max_av=10000
    e_av=np.zeros(n_max_av)
    p_av=np.zeros(n_max_av)
    t_av=np.zeros(n_max_av)
    n_av,somma,istart,avmax=-1,0,0,0
    for iterate in range(1,n_iter):
        if tsav[iterate]>0 and tsav[iterate-1]==0:
            somma,avmax=0,0
            istart=iterate
            if n_av==n_max_av-1:
                print("troppe valanghe")
                break
            n_av+=1
        somma+=tsav[iterate]
        if tsav[iterate]>avmax:
            avmax=tsav[iterate]
        if tsav[iterate]<=0 and tsav[iterate-1]>0:
            e_av[n_av]=somma
            p_av[n_av]=avmax
            t_av[n_av]=iterate-istart
                
    return n_av,e_av,p_av,t_av
	
N=100
E=0.1
critical_slope=5
n_iter=20000 #200000

sand=np.zeros(N)
tsav=np.zeros(n_iter)
mass=np.zeros(n_iter)

for iterate in range(0,n_iter):
    move=np.zeros(N)
    for j in range(0,N-1):
        slope=abs(sand[j+1]-sand[j])
        if slope >= critical_slope:
            avrg=(sand[j]+sand[j+1])/2
            move[j]+=(avrg-sand[j])/2
            move[j+1]+=(avrg-sand[j+1])/2
            tsav[iterate]+=slope/4
            
    if tsav[iterate]>0:
        sand+=move
    else:
        j=np.random.randint(0,N-1)
        sand[j]+=np.random.uniform(0,E)
            
    sand[N-1]=0
    mass[iterate]=np.sum(sand)

   # print("{0},mass {1}.".format(iterate,mass[iterate]))    

misure=measure_av(n_iter,tsav)
	
plt.subplot(2,1,1)
plt.plot(range(0,n_iter),mass)
plt.ylabel("Sandpile mass")
plt.xlabel("iteration")
plt.subplot(2,1,2)
plt.plot(range(0,n_iter),tsav)
plt.ylabel("Displaced mass")
plt.xlabel("iteration")
plt.show()