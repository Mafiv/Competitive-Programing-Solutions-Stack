# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        ans=0
        for i,v in enumerate(citations):
            if(i+1<=v):
                ans=i+1
            else:
                break
        return ans


