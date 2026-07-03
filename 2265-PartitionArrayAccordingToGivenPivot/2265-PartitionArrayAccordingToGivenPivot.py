# Last updated: 7/3/2026, 1:01:37 PM
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arr1 = []
        arr2 = []
        arr3 = []

        for i in nums :
            if i < pivot :
                arr1.append(i)
            elif i == pivot :
                arr2.append(i)
            else:
                arr3.append(i)
            
        
        return arr1+arr2+arr3