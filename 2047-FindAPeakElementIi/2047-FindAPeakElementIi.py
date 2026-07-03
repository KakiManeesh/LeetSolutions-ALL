# Last updated: 7/3/2026, 1:31:48 PM
from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        top, bottom = 0, m - 1

        while top < bottom:
            mid = (top + bottom) // 2

            col = 0
            for j in range(1, n):
                if mat[mid][j] > mat[mid][col]:
                    col = j

            if mat[mid][col] < mat[mid + 1][col]:
                top = mid + 1
            else:
                bottom = mid

        col = 0
        for j in range(1, n):
            if mat[top][j] > mat[top][col]:
                col = j

        return [top, col]