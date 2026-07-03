# Last updated: 7/3/2026, 12:49:54 PM
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        sum = 0
        for i in range(0,len(nums)):
            if  bin(i).count('1') == k :
                sum += nums[i] 

        return sum