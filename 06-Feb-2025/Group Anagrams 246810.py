# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=defaultdict(list)
        ans=[]
        for i,v in enumerate(strs):
            itr=list(v)
            itr.sort()
            count="".join(itr)
            a[count].append(v)
        for i in a:
            ans.append(a[i])
        return ans
        




        