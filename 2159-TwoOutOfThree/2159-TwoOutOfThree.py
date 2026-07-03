# Last updated: 7/3/2026, 1:01:50 PM
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        set_nums3 = set(nums3)
        
        return list((set_nums1 & set_nums2) | (set_nums1 & set_nums3) | (set_nums2 & set_nums3))
