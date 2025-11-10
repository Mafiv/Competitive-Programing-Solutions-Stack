class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        staks = [0]         
        for num in nums:
            while staks and staks[-1] > num:
                staks.pop()
            if staks[-1] < num:
                operations += 1
                staks.append(num)                
        return operations