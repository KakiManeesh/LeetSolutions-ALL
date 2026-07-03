# Last updated: 7/3/2026, 12:55:15 PM
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []

        for word in words:
            total = 0

            for ch in word:
                total += weights[ord(ch) - ord('a')]

            ans.append(chr(ord('z') - (total % 26)))

        return "".join(ans)