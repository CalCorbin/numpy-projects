import numpy as np

A = np.arange(32).reshape(4, 1, 8)

print(A)
# A has 4 planes, each with 1 row and 8 columns. 
# [[[ 0  1  2  3  4  5  6  7]]
# 
#  [[ 8  9 10 11 12 13 14 15]]
# 
#  [[16 17 18 19 20 21 22 23]]
# 
#  [[24 25 26 27 28 29 30 31]]]

B = np.arange(48).reshape(1, 6, 8)

print(B)
# B has only 1 plane with 6 rows and 8 columns.
# [[[ 0  1  2  3  4  5  6  7]
#   [ 8  9 10 11 12 13 14 15]
#   [16 17 18 19 20 21 22 23]
#   [24 25 26 27 28 29 30 31]
#   [32 33 34 35 36 37 38 39]
#   [40 41 42 43 44 45 46 47]]]

print('A + B')
print(A + B)
"""
The way broadcasting works is that NumPy duplicates the plane in B 
three times so that you have a total of four, 
matching the number of planes in A. 
It also duplicates the single row in A five times for a total of six, 
matching the number of rows in B. Then it adds each element in 
the newly expanded A array to its counterpart in the same location in B. 
The result of each calculation shows up in the corresponding location 
of the output.
"""
# [[[ 0  2  4  6  8 10 12 14]
#   [ 8 10 12 14 16 18 20 22]
#   [16 18 20 22 24 26 28 30]
#   [24 26 28 30 32 34 36 38]
#   [32 34 36 38 40 42 44 46]
#   [40 42 44 46 48 50 52 54]] Plane 1

#  [[ 8 10 12 14 16 18 20 22]
#   [16 18 20 22 24 26 28 30]
#   [24 26 28 30 32 34 36 38]
#   [32 34 36 38 40 42 44 46]
#   [40 42 44 46 48 50 52 54]
#   [48 50 52 54 56 58 60 62]] Plane 2

#  [[16 18 20 22 24 26 28 30]
#   [24 26 28 30 32 34 36 38]
#   [32 34 36 38 40 42 44 46]
#   [40 42 44 46 48 50 52 54]
#   [48 50 52 54 56 58 60 62]
#   [56 58 60 62 64 66 68 70]] Plane 3

#  [[24 26 28 30 32 34 36 38]
#   [32 34 36 38 40 42 44 46]
#   [40 42 44 46 48 50 52 54]
#   [48 50 52 54 56 58 60 62]
#   [56 58 60 62 64 66 68 70]
#   [64 66 68 70 72 74 76 78]]] Plane 4