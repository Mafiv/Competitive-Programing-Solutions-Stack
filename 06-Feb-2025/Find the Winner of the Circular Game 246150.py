# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        x=list(range(1,n+1))
        a=n
        i=0
        while(a>1):
            print(x,a)
            i=(i+k-1)%a
            x.remove(x[i])
            a-=1
        return x[0]
        