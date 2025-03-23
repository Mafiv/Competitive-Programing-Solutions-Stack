# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
              (-1, -1), (-1, 1), (1, -1), (1, 1)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == '*':  
            continue 
        mine_count = sum(1 for dx, dy in directions 
                         if 0 <= i + dx < n and 0 <= j + dy < m and arr[i + dx][j + dy] == '*')
        if arr[i][j].isdigit():
            if int(arr[i][j]) != mine_count:
                print("NO")
                exit()
        elif arr[i][j] == "." and mine_count > 0:
            print("NO")
            exit()

print("YES")
