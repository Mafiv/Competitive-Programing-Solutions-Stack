# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: list[int]) -> int:
        sum_x=0
        left=0
        right=len(height)-1
        while(left!=right):
            t=min(height[right],height[left])*(right-left)
            if(t>sum_x):sum_x=t
            
            if(height[left]>height[right]):
                right-=1
            else:
                left+=1
        return sum_x

