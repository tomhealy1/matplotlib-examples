#2 plot side by side
import matplotlib.pyplot as plt 
import numpy as np 

plt.subplot(1, 2, 1)
x = np.random.normal(0.0, 1.0, 10000)

#More bins = more granularity
plt.hist(x,bins=20)

plt.subplot(1, 2, 2)
x = np.random.uniform(-3.0, 3.0, 10000)
plt.hist(x)

plt.show()