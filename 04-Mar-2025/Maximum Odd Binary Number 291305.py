# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count=Counter(s)
        ones='1'*(count['1']-1)
        if(ones==''):
            final='0'*count['0']+'1'
        else:
            final=str(int(ones)*10**(count['0']))+'1'
        return final



        