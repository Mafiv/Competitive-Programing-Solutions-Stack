# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        sum_map = {0: 1}
        total_sum = 0
        for num in nums:
            total_sum += num
            if total_sum - k in sum_map:
                count += sum_map[total_sum - k]
            sum_map[total_sum] = sum_map.get(total_sum, 0) + 1
        return count
