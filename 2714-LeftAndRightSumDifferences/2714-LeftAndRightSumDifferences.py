# Last updated: 7/3/2026, 12:50:12 PM
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left = 0
        ans = []

        for num in nums:
            total -= num         
            ans.append(abs(left - total))
            left += num

        return ans