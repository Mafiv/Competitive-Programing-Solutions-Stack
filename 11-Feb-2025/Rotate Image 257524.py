# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ln=len(matrix)
        i,j=0,0
        tmp=[[]]
        for i in range((ln+1)//2):
            for j in range(ln//2):
                if(j==ln-1):
                    break
                matrix[i][j],matrix[j][ln-1-i],matrix[ln-1-i][ln-1-j],matrix[ln-j-1][i]=matrix[ln-j-1][i],matrix[i][j],matrix[j][ln-1-i],matrix[ln-1-i][ln-1-j]
                j+=1

