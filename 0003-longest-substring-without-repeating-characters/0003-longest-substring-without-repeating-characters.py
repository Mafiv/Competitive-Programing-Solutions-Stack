class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se = set()
        l=0
        res=0
        for i in range(len(s)):
            while(s[i] in se):
                se.remove(s[l])
                l+=1
            se.add(s[i])
            res=max(res,i-l+1)        
        return res


        