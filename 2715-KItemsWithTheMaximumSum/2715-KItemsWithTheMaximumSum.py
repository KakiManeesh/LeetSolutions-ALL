# Last updated: 7/3/2026, 12:50:11 PM
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        if k < numOnes :
            return k
        k = k-numOnes - numZeros

        if k>0 :
            return numOnes - k
        return numOnes