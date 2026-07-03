# Last updated: 7/3/2026, 1:01:25 PM
import numpy as np
from scipy.ndimage import maximum_filter
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        arr = np.array(grid)
        # Apply 3x3 max filter with mode='valid' to avoid padding
        result = maximum_filter(arr, size=3, mode='constant')[1:-1, 1:-1]
        return result.tolist()