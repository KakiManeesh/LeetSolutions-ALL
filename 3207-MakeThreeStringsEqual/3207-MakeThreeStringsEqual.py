# Last updated: 7/3/2026, 12:49:49 PM
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        lengths=[len(s1),len(s2),len(s3)]
        count=0
        for i in range(min(lengths)):
            if(s1[i] == s2[i] == s3[i]):
                count+=1
            else:
                break
        if(count==0):
            return -1
        
        return sum(lengths) - 3* count