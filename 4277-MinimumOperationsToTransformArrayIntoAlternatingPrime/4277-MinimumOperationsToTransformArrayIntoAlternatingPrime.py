# Last updated: 7/3/2026, 12:55:04 PM
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        def isPrime(n):
            if n < 2 :
                return False
            if n ==2 :
                return True
            if n%2 == 0:
                return False
            for i in range(3,int(n**0.5) +1 ,2):
                if n%i == 0 :
                    return False
            return True
            
        count = 0
        i = 0
        while i<len(nums):
            if i%2 ==0 :
                if not isPrime(nums[i]):
                    nums[i] += 1
                    count +=1 
                    continue
                else:
                    i+=1
                
            else:
                if  isPrime(nums[i]) :
                    count +=1
                    nums[i]+=1
                    continue
                else:
                    i += 1

        return count