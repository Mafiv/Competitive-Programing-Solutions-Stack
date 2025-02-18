# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

import sys

def solve(n, k, a):
    freq = {}
    l = 0
    max_len = 0
    best_l, best_r = 1, 1
    
    for r in range(n):
        freq[a[r]] = freq.get(a[r], 0) + 1
        
        while len(freq) > k:
            freq[a[l]] -= 1
            if freq[a[l]] == 0:
                del freq[a[l]]
            l += 1
        
        if r - l + 1 > max_len:
            max_len = r - l + 1
            best_l, best_r = l + 1, r + 1
    
    print(best_l, best_r)

if __name__=='__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    solve(n, k, a)
