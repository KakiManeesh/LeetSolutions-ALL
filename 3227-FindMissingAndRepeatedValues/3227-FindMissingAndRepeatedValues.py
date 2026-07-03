# Last updated: 7/3/2026, 12:49:47 PM
from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)  
        total_numbers = n * n 
        
        k = set()
        dup = 0
        for row in grid:
            for num in row:
                if num in k:
                    dup = num 
                k.add(num)

        
        expected_sum = total_numbers * (total_numbers + 1) // 2
        actual_sum = sum(sum(row) for row in grid)
        missing = expected_sum - (actual_sum - dup)  # Missing number calculation
        
        return [dup, missing]
