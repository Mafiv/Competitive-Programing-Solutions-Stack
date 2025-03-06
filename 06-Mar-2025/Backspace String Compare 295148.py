# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def buildString(self, string: str) -> str:
        stack = []
        for char in string:
            if char == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

    def backspaceCompare(self, s,t):
        return self.buildString(s) == self.buildString(t)