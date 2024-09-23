n = 100000
x = np.zeros(n)
y = np.zeros(n)

from math import e
import random
for i in range(1, n):
  val = random.randint(1, 4)
  if val == 1:
    x[i] = x[i-1] +1
    y[i] = y[i-1]
  elif val == 2:
    x[i] = x[i-1] -1
    y[i] = y[i-1]
  elif val == 3:
    x[i] = x[i-1]
    y[i] = y[i-1] +1
  else:
    x[i] = x[i-1]
    y[i] = y[i-1] -1

import pylab
pylab.title('Random Walk - 100000 steps')
pylab.plot(x, y)

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))  # Increase figure size
plt.plot(x, y, color='blue', lw=2, alpha=0.7)  # Line with transparency
plt.scatter(x[0], y[0], c='green', s=100, label='Start')  # Mark start point
plt.scatter(x[-1], y[-1], c='red', s=100, label='End')  # Mark end point

plt.title('2D Random Walk', fontsize=16)
plt.xlabel('X-Coordinate')
plt.ylabel('Y-Coordinate')
plt.grid(True)
plt.legend()

plt.show()
