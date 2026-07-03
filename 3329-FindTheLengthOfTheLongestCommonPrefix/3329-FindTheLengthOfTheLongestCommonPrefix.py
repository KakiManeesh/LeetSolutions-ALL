# Last updated: 7/3/2026, 12:49:41 PM
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes1 = set()
        for num in arr1:
            s = str(num)
            for i in range(1, len(s) + 1):
                prefixes1.add(s[:i])
        
        max_len = 0
        for num in arr2:
            s = str(num)
            for i in range(1, len(s) + 1):
                if s[:i] in prefixes1:
                    max_len = max(max_len, i)
        
        return max_len