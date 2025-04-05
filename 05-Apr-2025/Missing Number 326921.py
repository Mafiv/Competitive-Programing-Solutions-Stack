# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums2=sorted(nums)
        for i in range(nums2[-1]+1):
            if(i==nums2[-1]):
                return i+1
            elif(i != nums2[i]):
                return i
                
            


        
