# Last updated: 7/3/2026, 12:49:26 PM
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowel = "aeiou"
        for i in vowel:
            if i in s:
                return True
        return False