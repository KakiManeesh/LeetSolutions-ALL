# Last updated: 7/3/2026, 12:55:13 PM
class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        low = 0
        high = len(s)-1
        while low <= high :
            if s[low] == s[high] :
                return low
            low +=1
            high -=1
        return -1