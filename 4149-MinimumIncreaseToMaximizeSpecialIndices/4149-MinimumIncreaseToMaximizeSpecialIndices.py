# Last updated: 7/3/2026, 12:55:17 PM
from typing import List

class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: cost to make each index a peak
        cost = [0] * n
        for i in range(1, n - 1):
            needed = max(nums[i - 1], nums[i + 1]) + 1
            cost[i] = max(0, needed - nums[i])

        # Step 2: DP
        # dp[i] = (max_peaks, min_cost)
        dp = [(0, 0)] * n

        for i in range(1, n - 1):
            # skip
            skip = dp[i - 1]

            # take
            if i - 2 >= 0:
                take_peaks = dp[i - 2][0] + 1
                take_cost = dp[i - 2][1] + cost[i]
            else:
                take_peaks = 1
                take_cost = cost[i]

            if take_peaks > skip[0]:
                dp[i] = (take_peaks, take_cost)
            elif take_peaks < skip[0]:
                dp[i] = skip
            else:
                dp[i] = (take_peaks, min(take_cost, skip[1]))

        return dp[n - 2][1]