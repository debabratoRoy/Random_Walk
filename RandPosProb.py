import numpy as np
import matplotlib.pyplot as plt
import random as rand

N=100
time=100
#ensemble=5000000
ensemble=100000
randLim = 0.5
step=2

x=np.arange(-N,N+1,step)
y=np.zeros(len(x))

for i in range(ensemble):
    pos=0
    for j in range(time):
        r=rand.random()
        if(r<=randLim):
            pos = pos + 1
        elif(r>randLim):
            pos = pos - 1   
    
    indx = int( (N+pos)/step ) 
    y[indx]+=1
    
    #indx = (N+pos)/step  
    #print('index=',indx)
    '''
    if(pos>0):
        for i in range(midIndx,len(x)):
            if(x[i]==pos):
                y[i]+=1
                break
    elif(pos<0):
        for i in range(midIndx-1,-1,-1):
            if(x[i]==pos):
                y[i]+=1
                break
    '''
    
    
    '''
    for i in range(0,len(x)):
        if(x[i]==pos):
            y[i]+=1
            break
    
    '''
    
y=y/ensemble

dat = np.array([x,y])
dat = dat.T
np.savetxt('RandPosProbtst.txt',dat,delimiter = '\t')

plt.plot(x,y)
plt.show()


'''
while(count<=N):
    y.append(0)
    x.append(count)
    count+=1
'''

'''
while(count<10):
    while(t<time):
        pos = pos+rand.choice([-1,1])
        for i in range(0,len(x)):
            if(x[i] == pos):
                y[i]+=1
                break
        t+=1
    
    count+=1

'''

'''
r=pow(2,N)
m = y/r

print(y)
'''

