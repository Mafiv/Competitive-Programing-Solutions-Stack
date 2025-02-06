# Problem: Toeplitz Matrix - https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i,v in enumerate(matrix):
            if(i ==len(matrix)-1):
                continue
            tmp1=v[:len(v)-1]
            tmp2=matrix[i+1][1:]
            if(tmp1!=tmp2):
                return False
        return True

        