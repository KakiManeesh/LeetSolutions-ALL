# Last updated: 7/3/2026, 12:49:55 PM
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        all = set()

        for i,p in enumerate(reversed(nums)) :
            if p > k :
                continue 
            all.add(p)
            if len(all) == k :
                return i+1