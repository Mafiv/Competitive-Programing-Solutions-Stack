# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dup= defaultdict(list)
        ans=[]
        for i,v in enumerate(paths):
            tmp=v.split(' ')
            for j in tmp[1:]:
                tmp2=j.split('(')
                dup[tmp2[1]].append(tmp[0]+'/'+tmp2[0])
        for val in dup.values():
            if(len(val)>1):
                ans.append(val)
        return ans




        # result = []
        # for i,v in enumerate(paths):
        #     semi = []
        #     tmp=v.split()
        #     for k in range(1, len(tmp)):
        #         if tmp[k]
        