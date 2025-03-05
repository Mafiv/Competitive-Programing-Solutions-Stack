# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c=Counter(answers)
        ans=0
        for i in c:
            if(c[i]>i+1):
                p=math.ceil(c[i]/(i+1))
                ans+=(i+1)*p
            else:
                ans+=i+1
        return ans