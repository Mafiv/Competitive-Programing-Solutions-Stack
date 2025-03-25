# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def chk(nums,cap):
            days=0
            sm=0
            for i in nums:
                if(sm+i==cap):
                    days+=1
                    sm=0
                elif(sm+i>cap):
                    days+=1
                    sm=i
                else:
                    sm+=i
            if(sm):
                days+=1
            print(cap,days)
            return days
        ans=sum(weights)
        mn,mx=max(weights),ans
        while(mx>=mn):
            mid=mn+(mx-mn)//2
            tmp=chk(weights,mid)
            if(tmp<=days):
                ans=mid
                mx=mid-1
            else:
                mn=mid+1
        return ans






        