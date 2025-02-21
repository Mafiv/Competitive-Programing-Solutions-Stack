# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not (firstList or secondList):
            return []
        ans=[]
        i,j=0,0
        l1=len(firstList)
        l2=len(secondList)
        while(i<l1 and j<l2):
            firstStart,firstEnd=firstList[i]
            secondStart,secondEnd=secondList[j]
            if(firstStart>secondEnd):
                j+=1
            elif(secondStart>firstEnd):
                i+=1
            else:
                ans.append([max(firstStart,secondStart),min(firstEnd,secondEnd)])
                if(firstEnd>secondEnd):
                    j+=1
                else:
                    i+=1
            print(i,j)
        return ans



