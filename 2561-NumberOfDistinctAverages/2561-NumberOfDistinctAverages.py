# Last updated: 7/3/2026, 12:50:21 PM
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        
        nums1 = nums[:len(nums)//2]
        nums2 = nums[len(nums)//2:]
        nums2 = nums[::-1]  

        k = set()

        for i,j in  zip(nums1,nums2) :
            k.add((i+j)/2)
        return len(k)