# Last updated: 7/3/2026, 12:55:09 PM
class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        limit = int(n**(1/3)) + 1
        sum_count = {
            
        }
        
        for i in range(1,limit) :
            for j in range(i,limit) :
                temp = i**3 + j**3
                if temp > n :
                    break
                if temp in sum_count :
                    sum_count[temp] += 1
                else:
                    sum_count[temp] = 1
        output = []
        for i in sum_count :
            if sum_count[i] >= 2 :
                output.append(i)
        return sorted(output)