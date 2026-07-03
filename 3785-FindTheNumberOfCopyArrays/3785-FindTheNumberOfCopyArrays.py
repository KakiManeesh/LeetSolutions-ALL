# Last updated: 7/3/2026, 12:49:06 PM
from typing import List

class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        MOD = 10**9 + 7
        low, high = bounds[0]
        for i in range(1, len(original)):
            diff = original[i] - original[i - 1]
            new_low = low + diff
            new_high = high + diff           
            low = max(new_low, bounds[i][0])
            high = min(new_high, bounds[i][1])
            if low > high:
                return 0  
        return (high - low + 1) % MOD
