# Last updated: 7/3/2026, 12:55:16 PM
class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs( n - int(str(n)[::-1] ) )
        