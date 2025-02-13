# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i,j=0,len(skill)-1
        mx=skill[i]+skill[j]
        ans=skill[i]*skill[j]
        i+=1
        j-=1
        while(i+1<=j):
            if(skill[i]+skill[j]!=mx):
                return -1
            else:
                ans+=skill[i]*skill[j]
                i+=1
                j-=1
        return ans
        