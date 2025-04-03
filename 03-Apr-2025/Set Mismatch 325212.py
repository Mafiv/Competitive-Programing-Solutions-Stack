# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        sums=0
        ans=[]
        s=set()
        for i in nums:
            if(i in s):
                ans.append(i)
            else:
                s.add(i)
            sums+=i
        n=len(nums)
        total=(n*(n+1))//2
        if(total>=sums):
            ans.append(ans[-1]+(total-sums))
        else:
            ans.append(ans[-1]-(sums-total))
        return ans
