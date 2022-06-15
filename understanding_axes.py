import numpy as np

table = np.array([
    [5, 3, 7, 1],
    [2, 6, 7, 9],
    [1, 1, 1, 1],
    [4, 3, 2, 0],
])

# .max() returns the largest value in the entire array,
# no matter how many dimensions there are.
print(table.max())
# 9

# A two-dimensional array has a vertical axis (axis 0)
# Selects the maximum value in each of the four vertical sets 
# of values in table and returns a flattened 1-D array.
print(table.max(axis=0))
# array([5, 6, 7, 9])

# A two-dimensional array has a horizontal axis (axis 1)
# Selects the maximum value in each of the four horizontal sets
# of values in table and returns a flattened 1-D array.
print(table.max(axis=1))
# array([7, 9, 1, 4])
