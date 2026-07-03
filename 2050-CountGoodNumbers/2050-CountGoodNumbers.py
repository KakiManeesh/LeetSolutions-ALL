# Last updated: 7/3/2026, 1:31:45 PM
class Solution:
    def countGoodNumbers(self, n: int) -> int:

        MOD = 10**9 + 7
        def soln(x,n):
            if x== 1 :
                return 1
            if n == 0 :
                return 1
            elif n ==1 :
                return x
                
            half =  soln(x,n//2)

            if n%2 ==0 :
                return (half*half)%MOD
            else:
                return (half * half * x)% MOD
        
        ans = soln( 20, n//2 )
        limit = 10**9 + 7
        if n%2 == 1 :
            return (ans*5)%limit
        else:
            return ans%limit