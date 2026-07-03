# Last updated: 7/3/2026, 12:55:03 PM
class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        strings = []

        for i in range(len(nums1)):

            strings.append(  '1'*nums1[i] + '0'*nums0[i] ) 

        def compare(a,b) :    
            if a+b > b+a :
                return -1
            elif a+b==b+a :
                return 0
            else:
                return 1

        strings.sort(key = cmp_to_key(compare) )

        binary = "".join(strings)

        MOD = 10**9+7
        result = 0
        for bit in binary :
            result = (result *2 + int(bit))%MOD

        return result
        