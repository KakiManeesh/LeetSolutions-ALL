# Last updated: 7/3/2026, 12:49:08 PM
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        count_even = 0
        count_odd = 0 
        for i in nums :
            if i%2 == 0 :
                count_even +=1
                continue
            count_odd +=1
        return [0]*count_even + [1]*count_odd