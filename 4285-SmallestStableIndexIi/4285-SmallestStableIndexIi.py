# Last updated: 7/3/2026, 12:54:53 PM
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Precompute max from left
        max_left = [0] * n
        max_left[0] = nums[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], nums[i])
        
        # Precompute min from right
        min_right = [0] * n
        min_right[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            min_right[i] = min(min_right[i+1], nums[i])
        
        # Find the first stable index
        for i in range(n):
            if max_left[i] - min_right[i] <= k:
                return i
        
        return -1