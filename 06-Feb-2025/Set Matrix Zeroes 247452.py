# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        a=[]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j]==0):
                    a.append([i,j])
        for i in a:
            for e in i:
                j=i[0]
                for k in range(len(matrix[0])):
                    matrix[j][k]=0
                    
            for e in i:
                j=i[1]
                for k in range(len(matrix)):
                    matrix[k][j]=0
                
        


        