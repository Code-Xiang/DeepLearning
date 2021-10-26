import numpy as np

x = np.array([1, 2, 3, 4])
print("x.shape:", x.shape)
y = np.zeros((2, 3, 4))
print("y.shape:", y.shape)
y.shape = (3, 8)
print(y)
print(y.shape[1])

