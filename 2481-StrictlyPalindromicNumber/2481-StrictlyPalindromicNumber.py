# Last updated: 7/3/2026, 1:01:22 PM
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        for i in range(2,n-1):
            current = ""
            k=n
            while k>0 :
                current = str(k%i) + current 
                k=k//i
            
            if current != current[::-1]:
                return False
        return True