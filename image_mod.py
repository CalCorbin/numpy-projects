import numpy as np
import matplotlib.image as mpimg

img = mpimg.imread("kitty.jpg")
print(type(img))
print(img.shape)
# Should print
# <class 'numpy.ndarray'>
# (1299, 1920, 3)

# Generate a blue kitty
output = img.copy()
output[:, :, :2] = 0
mpimg.imsave("blue.jpg", output)

# Generate a gray kitty
averages = img.mean(axis=2)  # Take the average of each R, G, and B
mpimg.imsave("bad-gray.jpg", averages, cmap="gray")

# Use the luminosity method to generate a gray kitty. This
# technique does a weighted average of the three channels, 
# with the mindset that the color green drives how bright an image appears to be,
# and blue can make it appear darker.
weights = np.array([0.3, 0.59, 0.11])
grayscale = img @ weights
mpimg.imsave("good-gray.jpg", grayscale, cmap="gray")