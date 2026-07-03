# Last updated: 7/3/2026, 1:31:52 PM
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate_array(matrix ):
            n = len(matrix)
            for i in range(n):
                for j in range(i+1):
                    if i==j :
                        continue
                    else:
                        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            for i in range(n):
                matrix[i] = matrix[i][::-1]
            return matrix

        if mat == target :
            return True

        rotated_90 =rotate_array(mat)
        if rotated_90 == target :
            return True

        rotated_180 =rotate_array(rotated_90)
        if rotated_180 == target :
            return True

        rotated_270 =rotate_array(rotated_180)
        if rotated_270 == target :
            return True
        
        return False