# Last updated: 7/3/2026, 12:50:17 PM
from math import ceil
import heapq
from typing import List

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)

        score = 0
        for _ in range(k):
            popped_value = heapq.heappop(nums)  # Pop the largest value
            score -= popped_value  # Update score
            heapq.heappush(nums, -ceil(-popped_value / 3))  # Push back modified value

        return score
