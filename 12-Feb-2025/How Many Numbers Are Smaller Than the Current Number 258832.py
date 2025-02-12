# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        w=sorted(nums)
        ans=[]
        a=defaultdict(int)
        for i in range(len(w)-1,-1,-1):
            a[w[i]]=i
        for i in nums:
            ans.append(a[i])
        return ans
        
        