# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

from collections import defaultdict

def count_deletions(c):
    l, r = 0, n - 1
    deleted = 0
    while l < r:
        if melodies[l] != melodies[r]:
            if melodies[l] == c:
                deleted += 1
                l += 1
            elif melodies[r] == c:
                deleted += 1
                r -= 1
            else:
                return float('inf')
        else:
            l += 1
            r -= 1
    return deleted

def solve():
    global n, melodies
    n = int(input())
    melodies = input()

    l, r = 0, n - 1
    while l < r and melodies[l] == melodies[r]:
        l += 1
        r -= 1

    if l >= r:
        return 0
    
    deleted1 = count_deletions(melodies[l])
    deleted2 = count_deletions(melodies[r])
    
    ans = min(deleted1, deleted2)
    return ans if ans != float('inf') else -1

if __name__=="__main__":
    x = int(input())
    for i in range(x):
        print(solve())
