import numpy as np

"""
The number square below has some amazing properties. 
If you add up any of the rows, columns, or diagonals, 
then you'll get the same number, 34. 
That's also what you'll get if you add up each of the four quadrants, 
the center four squares, the four corner squares, 
or the four corner squares of any of the contained 3 x 3 grids. 
"""
square = np.array([
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1]  
])

for i in range(4):
    assert square[:, i].sum() == 34
    assert square[i, :].sum() == 34

assert square[:2, :2].sum() == 34
assert square[2:, :2].sum() == 34
assert square[:2, 2:].sum() == 34
assert square[2:, 2:].sum() == 34

print('Square confirmed to be magic')