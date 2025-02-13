# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        a=set(arr)
        x=arr.copy()
        p=sorted(a)
        ans=[]
        pt=len(arr)
        while(p!=x):
            mx=max(a)
            a.remove(mx)
            tmp=x.index(mx)
            if(tmp>0):
                ans.append(tmp+1)
            x=x[:tmp+1][::-1]+x[tmp+1:]
            x=x[:pt][::-1]+x[pt:]
            if(pt>1):
                ans.append(pt)
            pt-=1
        return ans




        
        