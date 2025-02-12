# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans=""
        nums_sorted = sorted(nums, key=lambda x: str(x) * 10, reverse=True)
        x=[str(i) for i in nums_sorted]
        print(x)
        if(len(set(x))==1 and x[0]=='0'):
            return str(x[0])
        return ''.join(x)

        
        