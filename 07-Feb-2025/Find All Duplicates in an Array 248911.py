# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        ans=[]
        for i in count:
            if(count[i] >1):
                ans.append(i)
        # ans.sort()
        return ans
        