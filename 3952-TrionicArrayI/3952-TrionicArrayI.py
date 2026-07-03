# Last updated: 7/3/2026, 1:00:25 PM
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False
        
        state = 0 
        
        for i in range(n - 1):
            if state == 0:  
                if nums[i] < nums[i + 1]:
                    continue
                elif nums[i] > nums[i + 1]:
                    if i == 0: 
                        return False
                    state = 1 
                else:
                    return False  
            elif state == 1: 
                if nums[i] > nums[i + 1]:
                    continue
                elif nums[i] < nums[i + 1]:
                    state = 2  
                else:
                    return False  
            elif state == 2:  
                if nums[i] < nums[i + 1]:
                    continue
                else:
                    return False 
        return state == 2