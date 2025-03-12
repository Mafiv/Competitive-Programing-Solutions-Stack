# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:

    def facotial(self,n):
        if(n<2):
            return 1
        return n*self.facotial(n-1)
        
    
    def trailingZeroes(self, n: int) -> int:
        x=self.facotial(n)
        # x=sys.set_int_max_str_digits(a)
        ans=0
        while(x%10==0):
            ans+=1
            x=x//10
        return ans



        