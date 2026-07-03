# Last updated: 7/3/2026, 12:49:36 PM
class Solution:
    def scoreOfString(self, s: str) -> int:
        if not s:  # Check if the string is empty
            return 0
        
        total_sum = 0
        prev = s[0]
        
        for i in s[1:]:  # Start from the second character
            total_sum += abs(ord(i) - ord(prev))
            prev = i
        
        return total_sum
