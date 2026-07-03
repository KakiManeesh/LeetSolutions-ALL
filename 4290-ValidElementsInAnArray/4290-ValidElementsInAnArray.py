# Last updated: 7/3/2026, 12:54:51 PM
class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)

        if n==1 :
            return nums

        left_max  = [0]*n
        right_max  = [0]*n

        left_max[0]=float('-inf')
        for i in range(1,n):
            left_max[i] = max(left_max[i-1],nums[i-1])

        right_max[n-1]=float('-inf')
        for i in range(n-2,-1,-1):
            right_max[i]=max(right_max[i+1],nums[i+1])

        result=[]

        for i in range(n) :
            if i==0 or i == n-1 :
                result.append(nums[i])
            elif nums[i]>left_max[i] or nums[i] > right_max[i]:
                result.append(nums[i])
        return result