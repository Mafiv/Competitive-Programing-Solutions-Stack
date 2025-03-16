# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def calc(self,n,x,i,lim):
        if(i==lim):
            return n        
        return self.calc(n*x,x,i+1,lim)

    def myPow(self, x: float, n: int) -> float:
        return x**n
