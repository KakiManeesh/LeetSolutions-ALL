# Last updated: 7/3/2026, 12:50:18 PM
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        set_ = set()

        for n in nums :
            i = 3
            if n&1 == 0 :
                while n&1 == 0:
                    n >>=1
                if 2 not in set_ :
                    set_.add(2)
            while i*i<=n :
                if n %i == 0 :
                    n = n//i
                    if i not in set_ :
                        set_.add(i)
                else:
                    i+=2
            if n > 1:
                set_.add(n)
        return len(set_)