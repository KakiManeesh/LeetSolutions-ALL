# Last updated: 7/3/2026, 1:01:48 PM
from typing import List
from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        out = set()
        for perm in permutations(digits, 3):
            num = perm[0] * 100 + perm[1] * 10 + perm[2]
            if num >= 100 and num % 2 == 0:
                out.add(num)

        return sorted(out)
