# Last updated: 7/3/2026, 1:01:49 PM
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        target_count = nums.count(target)        

        if not target_count :
            return []
        nums.sort()
        i = 0 
        output = []
        while target_count :
                if nums[i] == target : 
                    output.append(i)
                    target_count -=1
                i+=1
        return output