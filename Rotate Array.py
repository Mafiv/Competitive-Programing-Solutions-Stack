class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cp=[]
        cp[:]=nums
        for i in range(len(nums)):
            cp[i]=nums[(i-k)%len(nums)]
        nums[:]=cp
