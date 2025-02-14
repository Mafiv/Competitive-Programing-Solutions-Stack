# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        flag=0
        while(i<j):
            if not(s[i]==s[j]):
                a=s[i:j]
                b=s[i+1:j+1]
                return(a==a[::-1] or b==b[::-1])
            i+=1
            j-=1
        return True
         