# Last updated: 7/3/2026, 12:55:08 PM
class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        output = []

        for i in matrix :
            output.append(sum(i))
        return output