#import packages
import matplotlib.pyplot as plt 
import numpy as np 

#x is an item in numpy gen range between 0 and 10 going through .01 increment

x = np.arange(0.0,10.0,0.01)
#y = 3 mutiplied by x with 1 added
y = 3.0 * x + 1.0
# added noise using the random call in the numpy package
noise = np.random.normal(0.0,1.0, len(x))


plt.plot(x,y + noise, 'r.',label="Actual")
plt.plot(x,y, 'b-', label="Model")

plt.title("Simple Plot")
plt.xlabel("Weight")
plt.ylabel("Mass")
plt.legend()


plt.show()
