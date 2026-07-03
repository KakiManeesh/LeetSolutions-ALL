# Last updated: 7/3/2026, 12:49:15 PM
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        a = {float(-inf)}
        give  = []
        i = 0
        while len(give) != 2 :
            if nums[i] in a :
                give.append(nums[i])
            else :
                a.add(nums[i])
            i+=1
        return give 