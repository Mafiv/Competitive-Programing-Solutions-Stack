# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans=1
        points.sort()
        min_point=points[0][1]
        for i in range(1,len(points)):
            if(points[i][0] <= min_point):
                min_point=min(min_point,points[i][1])
            else:
                ans+=1
                min_point=points[i][1]
        return ans


