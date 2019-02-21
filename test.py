import numpy as np

x = np.array([[1,2],[3,4]])
b = np.repeat(x, 3, axis=0)
print(b)