# Last updated: 7/3/2026, 12:55:25 PM
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def helper(a):
            a = str(a)
            count = 0
            for i in range(len(a)) :
                if i == 0  or i == len(a)-1 :
                    continue
                if ( int(a[i-1] ) > int(a[i]) < int(a[i+1]) ) or ( int(a[i-1] ) < int(a[i]) > int(a[i+1]) )  :
                    count +=1
            
            return count


        total = 0
        for i in range(num1,num2+1):
            total += helper(i)

        return total
