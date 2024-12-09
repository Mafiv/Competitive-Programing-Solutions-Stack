class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        non_special = [0] * (n - 1)
        for i in range(n - 1):
            if (nums[i] + nums[i + 1]) % 2 == 0:
                non_special[i] = 1
        prefix_sum = [0] * n
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + non_special[i - 1]
        res = []
        for l, r in queries:
            if prefix_sum[r] - prefix_sum[l] > 0:
                res.append(False)
            else:
                res.append(True)
        
        return res