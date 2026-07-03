# Last updated: 7/3/2026, 12:54:48 PM
class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        count = nums.count(0)

        zeros_in_place = 0
        for i in range(len(nums) - count, len(nums)):  
            if nums[i] == 0:
                zeros_in_place += 1

        return count - zeros_in_place