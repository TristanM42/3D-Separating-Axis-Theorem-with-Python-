import numpy as np

x = np.array([[1,2],[3,4]])
y = np.max(np.max(x, axis=1))
print(y)