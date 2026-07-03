# Last updated: 7/3/2026, 12:49:28 PM
class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        if k < n:
            return k
        elif k == n:
            return n - 2
        else:
            effective_k = k % (2 * (n - 1))
            if effective_k < n:
                return effective_k
            else:
                return (2 * (n - 1)) - effective_k
