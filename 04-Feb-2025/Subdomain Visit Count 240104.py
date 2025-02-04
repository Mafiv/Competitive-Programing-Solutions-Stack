# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        a=defaultdict(int)
        ans=[]
        for i in cpdomains:
            tmp=i.split(' ')
            tmp2=tmp[1].split('.')
            j=len(tmp2)
            # a[tmp[1]]+=int(tmp[0])
            for i in range(j):
                smp=".".join(tmp2[i:j])
                a[smp]+=int(tmp[0])
        for i,v in a.items():
            ans.append(f'{v} {i}')
        return ans
            

        