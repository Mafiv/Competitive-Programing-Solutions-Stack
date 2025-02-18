# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        min_prefix_sum = 0
        prefix_sum = 0
        max_sum = float('-inf')
        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum)        
        return max_sum
