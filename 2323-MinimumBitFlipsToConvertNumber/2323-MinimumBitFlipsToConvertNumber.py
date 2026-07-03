# Last updated: 7/3/2026, 1:01:32 PM
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        result = start^goal
        count = 0

        while result :
            count +=1
            result = result&(result-1)
        return count