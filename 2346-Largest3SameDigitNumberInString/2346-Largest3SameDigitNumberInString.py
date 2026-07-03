# Last updated: 7/3/2026, 1:01:30 PM
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good = []
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                good.append(num[i]*3)
        return max(good) if good else ""
