# Last updated: 7/3/2026, 12:54:45 PM
class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        high = 0
        for i in range(len(nums)):
            if nums[i] > nums[high]:
                high = i
        
        left_sum = sum(nums[:high + 1])
        right_sum = sum(nums[high:])
        
        if left_sum > right_sum:
            return 0
        elif right_sum > left_sum:
            return 1
        else:
            return -1