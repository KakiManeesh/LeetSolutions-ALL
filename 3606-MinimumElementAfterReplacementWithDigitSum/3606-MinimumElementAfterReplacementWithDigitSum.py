# Last updated: 7/3/2026, 12:49:12 PM
class Solution:
    def minElement(self, nums: List[int]) -> int:
        def sum_of_digits(n: int) -> int:
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total
        
        k = float('inf')

        for num in nums:
            p = sum_of_digits(num)
            k = min(k, p)
        
        return k
