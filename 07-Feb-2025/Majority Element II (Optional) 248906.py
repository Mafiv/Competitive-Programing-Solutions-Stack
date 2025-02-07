# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        n=len(nums)/3
        ans=[]
        for i in count:
            if(count[i]>n):
                ans.append(i)
        return ans
