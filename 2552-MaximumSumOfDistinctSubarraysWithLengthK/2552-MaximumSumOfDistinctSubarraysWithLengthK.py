# Last updated: 7/3/2026, 1:01:15 PM
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        i = 0

        window = set()
        total = 0
        window_sum = 0
        for j in range( len(nums) ) :

            while  nums[j] in window or (j-i+1) > k :
                window_sum -= nums[i]
                window.discard(nums[i])
                i+=1
            window.add(nums[j])
            window_sum += nums[j]
            

            if len(window) == k :
                total = max( total , window_sum )
        
        return total