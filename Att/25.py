import numpy as np

x = np.random.randint(2, 30, size=30)
print(x[x % 2 == 0])

y = np.arange(2, 31, 2)
print(y)