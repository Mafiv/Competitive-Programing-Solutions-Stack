# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while(r>=l):
            mid=(r+l)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                l=mid+1
            else:
                r=mid-1
        return -1