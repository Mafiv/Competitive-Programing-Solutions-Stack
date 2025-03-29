# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0,len(matrix)-1
        best=0
        while(r>=l):
            mid=l+(r-l)//2
            if(matrix[mid][0]==target):
                return True
            elif(matrix[mid][0] < target):
                best=mid
                l=mid+1
            else:
                r=mid-1

        l,r=0,len(matrix[0])-1
        while(r>=l):
            mid=l+(r-l)//2
            if(matrix[best][mid] == target):
                return True
            elif(matrix[best][mid] < target):
                l=mid+1
            else:
                r=mid-1    
        return False
        