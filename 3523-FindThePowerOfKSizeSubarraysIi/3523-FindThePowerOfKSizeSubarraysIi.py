# Last updated: 7/3/2026, 12:49:21 PM
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        if k == 1:
            return nums

        good = [0] * (n - 1)

        for i in range(n - 1):
            if nums[i + 1] == nums[i] + 1:
                good[i] = 1

        curr = sum(good[:k - 1])
        ans = []

        for start in range(n - k + 1):
            if curr == k - 1:
                ans.append(nums[start + k - 1])
            else:
                ans.append(-1)

            if start < n - k:
                curr -= good[start]
                curr += good[start + k - 1]

        return ans