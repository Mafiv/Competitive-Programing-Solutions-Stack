# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        i=1
        j=len(piles)-1
        tot=0
        while(i+1<=j):
            tot+=piles[i]
            i+=2
            j-=1
        return tot


        