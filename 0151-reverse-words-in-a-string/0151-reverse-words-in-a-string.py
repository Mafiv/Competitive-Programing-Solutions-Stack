class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split(' ')
        z=[]
        for i in a:
            if not(i==''):
                z.append(i)
        strs=" ".join(z[::-1])
        return (strs)
