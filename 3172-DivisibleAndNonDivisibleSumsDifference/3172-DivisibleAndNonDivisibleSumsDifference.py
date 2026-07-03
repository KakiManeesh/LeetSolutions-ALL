# Last updated: 7/3/2026, 12:49:52 PM
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Calculate the sum of numbers from 1 to n
        total_sum = (n * (n + 1)) // 2

        # Calculate the sum of numbers divisible by m from 1 to n
        sum_divisible_by_m = sum(i for i in range(m, n + 1, m))

        # Calculate the sum of numbers not divisible by m
        sum_not_divisible_by_m = total_sum - sum_divisible_by_m

        # Return the difference between sums
        return sum_not_divisible_by_m - sum_divisible_by_m
