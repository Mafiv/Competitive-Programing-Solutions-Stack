# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        a=path.split('/')
        stack=['/']
        for i in a:
            if(i=='' or i=='.'):
                continue
            elif(i=='..'):
                p=len(stack)
                if(p>1):
                    stack.pop()
                    stack.pop()
                else:
                    continue
            else:
                stack.append(i)
                stack.append('/')
        if(len(stack)>1):
            stack=stack[:-1]
        return ''.join(stack)
                