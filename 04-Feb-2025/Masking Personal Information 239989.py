# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        is_email='@' in s
        if(is_email):
            tmp=s.split('@')
            return(tmp[0][0].lower()+"*****"+tmp[0][-1].lower()+"@"+tmp[1].lower())
        else:
            z=[i for i in s if i.isdigit()]
            z="".join(z)
            country=z[-11::-1]
            if(len(country)==1):
                return f"+*-***-***-{z[-4:]}"
            elif(len(country)==2):
                return f"+**-***-***-{z[-4:]}"
            elif(len(country)==3):
                return f"+***-***-***-{z[-4:]}"
            else:
                return f"***-***-{z[-4:]}"
        