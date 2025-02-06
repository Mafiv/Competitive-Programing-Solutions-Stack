# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans=0
        for i in words:
            tmp=list(chars).copy()
            flag=1
            for j in i:
                if not(j in tmp):
                    flag=0
                    break
                else:
                    tmp.remove(j)
            if(flag):
                ans+=len(i)
            flag=1
        return ans

