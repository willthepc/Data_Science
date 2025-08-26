import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10])
print(x)
x[x % 2 == 0] = -1
print(x)