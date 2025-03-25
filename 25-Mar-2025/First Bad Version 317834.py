# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        best=-1
        l,r=0,n
        while(r>=l):
            mid=l+(r-l)//2
            ans=isBadVersion(mid)
            if(ans):
                best=mid
                r=mid-1
            else:
                l=mid+1
        return best