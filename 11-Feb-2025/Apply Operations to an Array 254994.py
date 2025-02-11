# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        coll=[]
        flag=0
        for i in range(len(nums)):
            if(i == len(nums)-1):
                if(nums[i]>0):
                    coll.append(nums[i])
                else:
                    flag+=1
            else:
                if(nums[i]==nums[i+1] and nums[i]>0):
                    nums[i]=nums[i]*2
                    nums[i+1]=0
                    coll.append(nums[i])
                else:
                    if(nums[i]>0):
                        coll.append(nums[i])
                    else:
                        flag+=1
        return coll+[0]*flag
