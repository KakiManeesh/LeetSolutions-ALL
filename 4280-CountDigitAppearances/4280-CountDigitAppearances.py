# Last updated: 7/3/2026, 12:55:00 PM
class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0
        d = str(digit)
        for i in nums :
            count += str(i).count(d)
        return count 