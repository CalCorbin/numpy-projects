import numpy as np

temperatures = np.array([29.3, 42.1, 18.8, 16.1, 38.0, 12.5,
    12.6, 49.9, 38.6, 31.3, 9.2, 22.22]).reshape(2, 2, 3)

# Here, we use a numpy.ndarray method called .reshape() to form a 2 x 2 x 3
# block of data.
print(temperatures.shape)
# (2, 2, 3)
print(temperatures)
# [[[ 29.3  42.1  18.8]
#   [ 16.1  38.   12.5]]
# 
#  [[ 12.6  49.9  38.6]
#   [ 31.3   9.2  22.2]]]

print('Swap axes')
print(np.swapaxes(temperatures, 1, 2))
# [[[ 29.3  16.1]
#   [ 42.1  38. ]
#   [ 18.8  12.5]]
# 
#  [[ 12.6  31.3]
#   [ 49.9   9.2]
#   [ 38.6  22.2]]]