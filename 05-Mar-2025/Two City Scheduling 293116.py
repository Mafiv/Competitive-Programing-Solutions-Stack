# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: abs(x[0]-x[1]),reverse=True)
        a,b=0,0
        ans=0
        mid=len(costs)//2
        for i in costs:
            if(a==mid):
                ans+=i[1]
                b+=1
            elif(b==mid):
                ans+=i[0]
                a+=1
            elif(i[0]<=i[1]):
                a+=1
                ans+=i[0]
            else:
                b+=1
                ans+=i[1]
        return ans
        