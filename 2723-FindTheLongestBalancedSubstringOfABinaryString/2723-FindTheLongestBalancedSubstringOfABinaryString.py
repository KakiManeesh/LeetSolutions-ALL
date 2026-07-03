# Last updated: 7/3/2026, 12:50:09 PM
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        for i in range(len(s)//2,0,-1): 
            if '0'*i+'1'*i in   s :
                return i*2
        return 0