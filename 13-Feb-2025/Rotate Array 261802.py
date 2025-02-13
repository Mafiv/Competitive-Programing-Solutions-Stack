# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        t=k%n
        d=[0]*(n)
        for i in range(n):
            d[(i+t)%n]=nums[i]
        for i in range(len(nums)):
            nums[i]=d[i]
        


        