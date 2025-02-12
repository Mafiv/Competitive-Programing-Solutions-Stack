# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        p=0
        z=int(c**0.5)
        while(True):
            val=p**2+z**2
            if(val==c):
                return True
                break
            elif(p==z):
                if(val==c):
                    return True
                else:
                    return False
                break
            elif(val<c):
                p+=1
            elif(val>c):
                z-=1
            