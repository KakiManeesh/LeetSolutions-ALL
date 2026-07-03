# Last updated: 7/3/2026, 12:49:01 PM
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        return total%k