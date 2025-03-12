# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int):
        x=[1]
        rowIndex-=1
        for i in range(0,rowIndex+1):
            x.append(int(x[i]*(rowIndex-i+1)/(i+1)))
        print(x)
        return x
