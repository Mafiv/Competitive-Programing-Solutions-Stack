# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def calculate(minute):
            cars_no=0
            for i in ranks:
                a=math.floor((minute/i)**0.5)
                cars_no+=a
            if(cars_no>=cars):
                return True
            return False
        mn,mx=0,max(ranks)*cars**2
        best=mx
        while(mx>=mn):
            mid=(mn+(mx-mn)//2)
            ans=calculate(mid)
            if(ans and mid<best):
                best=mid
                mx=mid-1
            else:
                mn=mid+1
        return best



        