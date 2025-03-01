# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = min_sum = 0
        max_curr = min_curr = 0
        for num in nums:
            max_curr = max(num, max_curr + num)
            max_sum = max(max_sum, max_curr)
            min_curr = min(num, min_curr + num)
            min_sum = min(min_sum, min_curr)
        return max(abs(max_sum), abs(min_sum))
        