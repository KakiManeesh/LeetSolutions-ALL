# Last updated: 7/3/2026, 12:50:14 PM
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:

        a=[]

        for i in nums :
            a += list(str(i))
        
        return list(map(int,a))