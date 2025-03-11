# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def check(self,n):
        print(n)
        if(n ==1):
            return True
        elif(n <1):
            return False
        return self.check(n/4)
    def isPowerOfFour(self, n: int) -> bool:
        return self.check(n)
        