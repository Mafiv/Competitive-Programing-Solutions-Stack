# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        s=set()
        i=0
        p=0
        while(i<n):
            pos=nums[i]-1
            if(pos!=i):
                nums[pos],nums[i]=nums[i],nums[pos]
                if(nums[pos]==nums[i]):
                    if not(nums[i] in s):
                        ans.append(nums[i])
                        s.add(nums[i])
                    i+=1
            else:
                i+=1
        return ans