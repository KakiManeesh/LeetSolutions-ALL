# Last updated: 7/3/2026, 12:49:09 PM
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        def isSorted(nums):
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    return False
            return True

        count = 0

        while not isSorted(nums):
            min_sum = float('inf')
            min_idx = 0

            for i in range(len(nums) - 1):
                curr = nums[i] + nums[i + 1]
                if curr < min_sum:
                    min_sum = curr
                    min_idx = i

            merged = nums[min_idx] + nums[min_idx + 1]
            nums.pop(min_idx + 1)
            nums.pop(min_idx)
            nums.insert(min_idx, merged)

            count += 1

        return count