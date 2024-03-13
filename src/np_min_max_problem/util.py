import numpy as np

def minimum_maximum(arr):
    min_axis1 = np.min(arr, axis=1)
    max_min_axis1 = np.max(min_axis1)
    return max_min_axis1
