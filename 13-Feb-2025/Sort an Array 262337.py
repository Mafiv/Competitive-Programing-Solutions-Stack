# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mx=max(nums)+abs(min(nums))+1
        mini=abs(min(nums))
        ords=[0]*(mx)
        for i in nums:
            ords[i+mini]+=1
        ans=[]
        for i in range(mx):
            for j in range(ords[i]):
                ans.append(i-mini)
        return ans


        