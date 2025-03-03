# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        a=len(nums)
        mx=0
        for i in range(a-1):
            mx=max(nums[i],mx-1)
            if(nums[i]==0):
                if(mx==0):
                    return False
        return True
            