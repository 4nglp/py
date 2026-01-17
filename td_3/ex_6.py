import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,400)
y = x**2+7
plt.plot(x,y, color='red')
plt.title("placeholder")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend('f(x)=x**2+7')
plt.grid(True)
plt.show()