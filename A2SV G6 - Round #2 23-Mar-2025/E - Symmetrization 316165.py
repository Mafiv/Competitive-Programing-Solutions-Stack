# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

def process_matrix():
    size = int(input())
    grid = [input() for _ in range(size)]
    changes = 0
    if size == 1:
        return 0
    for row in range(size // 2):
        for col in range(row, size - row - 1):
            diff_count = 0
            if grid[row][col] != grid[size - row - 1][size - col - 1]:
                diff_count += 1
            if grid[row][col] != grid[col][size - row - 1]:
                diff_count += 1
            if grid[row][col] != grid[size - col - 1][row]:
                diff_count += 1
            changes += 1 if diff_count == 3 else diff_count
    return changes
if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        print(process_matrix())
