class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        x=[]
        k=1
        j=0
        for i in range(k,len(s)):
            if((set(s[j:i]).intersection(set(s[i:])))==set()):
                x.append(len(s[j:i]))
                k=i+1
                j=i
            if(i==len(s)-1):
                x.append(len(s[j:i+1]))
        return x
        
        
