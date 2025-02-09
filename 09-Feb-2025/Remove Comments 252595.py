# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []       
        in_block = False 
        newline = []      

        for line in source:
            i = 0
            if not in_block:
                newline = []
            
            while i < len(line):
                if not in_block:
                    if i + 1 < len(line) and line[i] == '/' and line[i+1] == '/':
                        break
                    elif i + 1 < len(line) and line[i] == '/' and line[i+1] == '*':
                        in_block = True
                        i += 2  
                        continue
                    else:
                        newline.append(line[i])
                        i += 1
                else:
                    if i + 1 < len(line) and line[i] == '*' and line[i+1] == '/':
                        in_block = False
                        i += 2  
                    else:
                        i += 1 
            if not in_block and newline:
                result.append("".join(newline))
        
        return result


