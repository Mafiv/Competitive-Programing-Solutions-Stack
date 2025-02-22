# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans=0
        count={0:1}
        sums=0
        for i in nums:
            sums+=i
            if(sums-goal in count):
                ans+=count[sums-goal]
            count[sums]=count.get(sums,0)+1
        return ans            
