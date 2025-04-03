# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(L,R):
            if(L>R):
                return 0
            L_side=nums[L] - helper(L+1,R)
            R_side=nums[R] - helper(L,R-1)
            return max(L_side,R_side)

        ans=helper(0,len(nums)-1)
        return ans>=0
        