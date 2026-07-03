# Last updated: 7/3/2026, 1:31:50 PM
class Solution:
    def largestOddNumber(self, num: str) -> str:
        set_ = set(('1','3','5','7','9'))
        for i in range(len(num)-1 , -1 , -1 ):
            if num[i] in set_ :
                return num[:i+1]
        return ""
