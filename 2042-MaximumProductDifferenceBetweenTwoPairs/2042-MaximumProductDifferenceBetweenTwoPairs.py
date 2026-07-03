# Last updated: 7/3/2026, 1:31:49 PM
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = list(tuple(nums))

        if len(nums) >= 4:
            nums.sort()
            return (nums[-1])*(nums[-2]) - (nums[0])*(nums[1])
        else:
            return 0