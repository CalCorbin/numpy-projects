from xml.dom.expatbuilder import theDOMImplementation
import numpy as np

"""
1. Use np.linspace() to generate an evenly spaced array
2. Set the dtype of an output
3. Reshape array with -1
Also, because of the particular calculation in this example, 
it makes life easier to have integers in the numbers array. 
But because the space between 5 and 50 doesn’t divide evenly by 24, 
the resulting numbers would be floating-point numbers. 
You specify a dtype of int to force the function to round down 
and give you whole integers.
"""
numbers = np.linspace(5, 50, 24, dtype=int).reshape(4, -1)

print(numbers)
# [[ 5  6  8 10 12 14]
#  [16 18 20 22 24 26]
#  [28 30 32 34 36 38]
#  [40 42 44 46 48 50]]

"""
A MASK is an array that has the exact same shape as your data, 
but instead of your values, it holds Boolean values: either True or False. 
You can use this mask array to index into your data array in nonlinear 
and complex ways. It will return all of the elements where the Boolean 
array has a True value.
"""

# This creates the mask by performing a vectorized Boolean computation,
# taking each element and checking to see if it divides evenly by four. This
# returns a mask array of the same shape with the Boolean results of the
# computation.
mask = numbers % 4 == 0
print(mask)
# [[False False  True False  True False]
#  [ True False  True False  True False]
#  [ True False  True False  True False]
#  [ True False  True False  True False]]

# This uses the mask to index into the original numbers array. 
# The array will lose its original shape, but the values will be
# we're looking for, in this case, all of the values that divide evenly by 4.
print(numbers[mask])
# [ 8 12 16 20 24 28 32 36 40 44 48]

# This a more traditional, idiomatic masked selection 
# that you might see in the wild, with an anonymous filtering 
# array created inline, inside the selection brackets. 
# This syntax is similar to usage in the R programming language.
by_four = numbers[numbers % 4 == 0]
print(by_four)
# [ 8 12 16 20 24 28 32 36 40 44 48]