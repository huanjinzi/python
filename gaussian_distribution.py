import math
import numpy
import matplotlib.pyplot as plt


# Standard Normal distribution
x = numpy.arange(-5, 5, 0.01)
y = 1 / math.sqrt(2 * math.pi) * numpy.power(math.e, -x * x / 2)
plt.plot(x, y)
plt.show()

