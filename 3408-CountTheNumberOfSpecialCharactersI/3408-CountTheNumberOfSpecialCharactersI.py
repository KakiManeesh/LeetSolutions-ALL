# Last updated: 7/3/2026, 12:49:32 PM
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        for i in range(65,91,1):
            if (chr(i) in word )and (chr(i+32) in word ):
                count +=1
        return count