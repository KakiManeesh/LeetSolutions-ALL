# Last updated: 7/3/2026, 12:55:28 PM
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return (max(nums)-min(nums))*k