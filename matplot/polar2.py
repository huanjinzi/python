
import numpy as np
import matplotlib.pyplot as plt 

N = 50
r = 2 * np.random.rand(N)

theta = 2 * np.pi * np.random.rand(N)

area = 1000 * r**2

colors = theta 

ax = plt.subplot(111, projection='polar')

c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

plt.show()
