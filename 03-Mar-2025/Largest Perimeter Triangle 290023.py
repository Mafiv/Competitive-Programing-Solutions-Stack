# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        mx=0
        for i in range(len(nums)-1,1,-1):
            if(nums[i]>=nums[i-1]+nums[i-2]):
                continue
            else:
                mx=max(mx,nums[i]+nums[i-1]+nums[i-2])
        return mx
            



        