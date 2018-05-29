import numpy as np
from scipy import ndimage


# Dirty
a = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 2, 2, 1, 2, 2, 0],
              [0, 1, 0, 2, 1, 1, 2, 2, 1, 2, 2, 0],
              [0, 0, 0, 1, 1, 1, 0, 2, 2, 2, 2, 0],
              [0, 1, 0, 1, 2, 1, 0, 0, 2, 2, 2, 0],
              [0, 0, 0, 1, 1, 1, 1, 0, 2, 2, 2, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# cleaned expected
b = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0],
              [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 0],
              [0, 0, 0, 1, 1, 1, 0, 2, 2, 2, 2, 0],
              [0, 0, 0, 1, 1, 1, 0, 0, 2, 2, 2, 0],
              [0, 0, 0, 1, 1, 1, 1, 0, 2, 2, 2, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])