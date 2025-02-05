# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hold=defaultdict(int)
        ans=[]
        unit=max(len(list1),len(list2))*2
        for i,v in enumerate(list1):
            hold[v]=i
        for i,v in enumerate(list2):
            if(v in hold):
                if(i+hold[v] <= unit):
                    if(i+hold[v] == unit):
                        ans.append(v)
                    else:
                        unit=i+hold[v]
                        ans=[v]
        return ans



