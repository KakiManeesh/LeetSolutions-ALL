# Last updated: 7/3/2026, 12:49:53 PM
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        a=[]

        while(nums):
            alice = nums.pop(nums.index(min(nums)))
            bob = nums.pop(nums.index(min(nums)))
            
            a.append(bob)
            a.append(alice)
        return a