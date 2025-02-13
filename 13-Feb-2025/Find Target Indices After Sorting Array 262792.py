# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        nums.sort()
        r=0
        while(r<len(nums)):
            if(nums[r]==target):
                ans.append(r)
            r+=1
        return ans

        