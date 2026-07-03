# Last updated: 7/3/2026, 1:01:28 PM
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        cake = set()

        for i in s :
            if i not in cake :
                cake.add(i)
            else:
                return i
        