# Last updated: 7/3/2026, 12:49:34 PM
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = {}
        upper = {}

        for i, c in enumerate(word):

            if c.islower():
                lower[c] = i      

            else:
                ch = c.lower()

                if ch not in upper:
                    upper[ch] = i

        count = 0

        for ch in lower:

            if ch in upper and lower[ch] < upper[ch]:
                count += 1

        return count