# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bal=0
        ans=0
        for i in s:
            if(i=='R'):
                bal+=1
            else:
                bal-=1
            if(bal==0):
                ans+=1
        return ans