import matplotlib.pyplot as plt
import numpy as np
import random as rand

x = []
y = []

#x0 = []
#y0 = []

#x1 = []
#y1 = []

#x2 = []
#y2 = []

#x3 = []
#y3 = []

t = 0

m = 0
n = 0

while (t < 1000):
    r = rand.randint(0,3)
    
    if (r == 0):
        m = m + rand.randint(1,3)
        x.append(m)
        y.append(n)
    elif (r == 1):
        n = n + rand.randint(1,3)
        x.append(m)
        y.append(n)
    elif (r == 2):
        m = m - rand.randint(1,3)
        x.append(m)
        y.append(n)
    elif (r == 3):
        n = n - rand.randint(1,3)
        x.append(m)
        y.append(n)
    
    t += 1

#saving data in a file

dat = np.array([x,y])
dat = dat.T
np.savetxt('randWalk.txt',dat,delimiter = '\t')

#print (x,y)

#ax = plt.axes()
#ax.set_facecolor('black')

plt.plot(x,y,'.',markersize=2)
#plt.plot(x0,y0,'.')
#plt.plot(x1,y1,'.')
#plt.plot(x2,y2,'.')
#plt.plot(x3,y3,'.')
plt.show()
    
    