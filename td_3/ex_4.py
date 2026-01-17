import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4,4,400)
y = np.cos(x) + 3*np.sin(2*x)
plt.plot(x,y)
plt.title("cos(x)+3sin(2x)")
plt.grid(True)
plt.show()
