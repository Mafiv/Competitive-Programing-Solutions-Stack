class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=len(set(nums))
        nums[:]=list(set(nums))
        return count
