# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        count_zeros = 0
        moves = 0        
        for c in reversed(s):
            if c == '0':
                count_zeros += 1
            else:
                moves += count_zeros                
        return moves
