# Last updated: 7/3/2026, 1:01:21 PM
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2 == 0 :
            return n
        return n*2