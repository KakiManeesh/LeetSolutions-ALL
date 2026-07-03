# Last updated: 7/3/2026, 12:49:24 PM
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(1 for i in nums if i % 3 != 0)