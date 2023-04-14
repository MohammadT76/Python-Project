
# Finding local maxima/minima with Numpy in a 1D numpy array
# For more information see this link : https://stackoverflow.com/questions/4624970/finding-local-maxima-minima-with-numpy-in-a-1d-numpy-array

import numpy as np
from scipy.signal import argrelextrema

x = np.array([0,0,2,5,4,1,0,3,5,6,2,1,3,0])
x = np.array([0,7,2,4,1,8,0,0,3,2,0]+1)

# for local maxima
max_pos = argrelextrema(x, np.greater)
print(max_pos)

# for local minima
min_pos = argrelextrema(x, np.less)
print(min_pos)

# print values for local min and max
print(x[argrelextrema(x, np.greater)[0]])
print(x[argrelextrema(x, np.less)[0]])