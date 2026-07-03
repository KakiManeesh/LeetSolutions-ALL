# Last updated: 7/3/2026, 12:50:08 PM
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        k = set()

        for i in range(1,n+1):
            if  i%3 ==0 or i%5 ==0 or i %7 == 0 :
                k.add(i)

        return sum(k)