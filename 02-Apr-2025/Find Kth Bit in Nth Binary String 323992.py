# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def help(s):
            a=''
            for i in s:
                if(i=='1'):
                    a+='0'
                else:
                    a+='1'
            return a
        ans='0'
        for i in range(n):
            inv=help(ans[::-1])
            res=ans+'1'+inv
            ans=res
        return ans[k-1]
        

        