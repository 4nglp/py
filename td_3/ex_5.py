import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,3,400)
y = x**2 - 4*x + 4
plt.plot(x,y)
plt.title("x**2-4x+4")
plt.grid(True)
plt.show()