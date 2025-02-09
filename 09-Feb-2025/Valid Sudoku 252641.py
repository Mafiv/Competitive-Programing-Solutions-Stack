# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            numbers = [x for x in row if x != '.']
            if len(numbers) != len(set(numbers)):
                return False
        for j in range(9):
            col = [board[i][j] for i in range(9) if board[i][j] != '.']
            if len(col) != len(set(col)):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = []
                for di in range(3):
                    for dj in range(3):
                        if board[i + di][j + dj] != '.':
                            box.append(board[i + di][j + dj])
                if len(box) != len(set(box)):
                    return False

        return True
                