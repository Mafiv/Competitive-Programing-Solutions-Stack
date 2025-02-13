# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        dic=defaultdict(list)
        for k,v in count.items():
            dic[v].append(k)
        res=[]
        for i in range(len(s)+1):
            for m in dic[i]:
                res.append(m*i)
        return (''.join(res[::-1]))