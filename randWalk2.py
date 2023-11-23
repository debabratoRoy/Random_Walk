import random as rand
import numpy as np
import matplotlib.pyplot as plt

c = 0
m = 0
n = 0
d = []
t = []

while(c < 10000):
    d.append(np.sqrt(m**2 + n**2))
    t.append(c)
    m = m + rand.randint(-1,1)
    n = n + rand.randint(-1,1)    
    c += 1

plt.plot(t,d,',')
plt.show()