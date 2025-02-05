# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        x=[['q','w','e','r','t','y','u','i','o','p'],['a','s','d','f','g','h','j','k','l'],['z','x','c','v','b','n','m']]
        w=dict()
        for i in range(len(x)):
            for j in x[i]:
                w[j]=i

        ans=[]
        for i in words:
            flag=1
            fr=0
            for j,v in enumerate(i):
                if(j==0):
                    fr=w[v.lower()]
                else:
                    if(w[v.lower()] != fr):
                        flag=0
                        break
            if (flag):
                ans.append(i)
            flag=1
        return ans


        