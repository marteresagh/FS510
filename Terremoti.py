import numpy as np
import matplotlib.pyplot as plt

N=64
f_thresh=5
delta_f=1.e-4
alpha=0.15
n_iter=100000

dx=np.array([-1,0,1,0])
dy=np.array([0,-1,0,1])
force=np.zeros([N+2,N+2])
toppling=np.zeros(n_iter,dtype="int")
totalf=np.zeros(n_iter,dtype="int")

for i in range(1,N+1):
    for j in range(1,N+1):
        force[i,j]=f_thresh*(np.random.uniform())
		
for iterate in range(0,n_iter):
    move=np.zeros([N+2,N+2])
    for i in range(1,N+1):
        for j in range(1,N+1):
            if force[i,j]>=f_thresh:
                move[i,j]-=force[i,j]
                move[i+dx[:],j+dy[:]]+=alpha*force[i,j]
                toppling[iterate]+=1
        
    if toppling[iterate]>0:
        force+=move
    else:
        force[:,:]+=delta_f
        
    totalf[iterate]=force.sum()
    if iterate%10000==0:
        print("{0},toppl {1}.".format(iterate,toppling[iterate]))
		
plt.subplot(2,1,1)
plt.plot(range(0,n_iter),totalf)
plt.xlabel("iteration")
plt.ylabel("Total force")
plt.subplot(2,1,2)
plt.plot(range(o,n_iter),toppling)
plt.xlabel("iteration")
plt.ylabel("toppling nodes")
plt.show()