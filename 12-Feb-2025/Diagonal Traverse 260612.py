# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        i,j=0,0
        ans=[]
        cn=1
        while(i<len(mat)):
            tmp=[]
            print(i,j)
            if(j<len(mat[0])-1):
                j+=1
            else:
                i+=1
            t,p=i,j
            while(t<=len(mat)-1 and p>=0):
                tmp.append(mat[t][p])
                t+=1
                p-=1
            if(cn%2==0):
                ans+=tmp[::-1]
            else:
                ans+=tmp
            cn+=1
        return [mat[0][0]]+ans


        