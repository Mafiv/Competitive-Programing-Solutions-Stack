# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque = deque() 
        max_deque = deque()          
        left = 0
        max_length = 0        
        for right, num in enumerate(nums):         
            while min_deque and min_deque[-1][0] > num:
                min_deque.pop()            
            while max_deque and max_deque[-1][0] < num:
                max_deque.pop()            
            min_deque.append((num, right))
            max_deque.append((num, right))
            while max_deque[0][0] - min_deque[0][0] > limit:
                if min_deque[0][1] == left:
                    min_deque.popleft()
                if max_deque[0][1] == left:
                    max_deque.popleft()
                left += 1            
            max_length = max(max_length, right - left + 1)        
        return max_length