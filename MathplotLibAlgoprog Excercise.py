import matplotlib.pyplot as plt 
import numpy as np 
  
  
# X and Y variable data 
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 
y = x**2
  
plt.plot(x, y) 
plt.xlabel("Time (m)")  # X-axis label 
plt.ylabel("No. of Viruses")  # Y-axis label 
plt.title("Exponential Growth of Viruses in 10 minutes")  # title
plt.show() 