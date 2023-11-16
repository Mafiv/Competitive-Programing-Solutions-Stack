class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        for i in s:
            if(ord(i)<65 or ord(i)>122):
                s=s.replace(i,'')
        if(s==s[::-1]):
            return True
        else:
            return False




