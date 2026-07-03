# Last updated: 7/3/2026, 12:54:52 PM
class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        
        x=str(x)
        n = str(n)
        if n[0]==x :
            return False
        for i in n :
            if i == x :
                return True
        return False