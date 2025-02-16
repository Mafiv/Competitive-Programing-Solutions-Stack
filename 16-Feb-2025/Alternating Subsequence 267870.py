# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

def max_alternating_subsequence_sum(n, a):
    total_sum = 0
    i = 0
    while i < n:
        max_val = a[i]
        while i + 1 < n and (a[i] < 0) == (a[i + 1] < 0):
            max_val = max(max_val, a[i + 1])
            i += 1
        total_sum += max_val
        i += 1
    return total_sum

def solve():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        a = list(map(int, input().split()))
        results.append(str(max_alternating_subsequence_sum(n, a)))
    print("\n".join(results))

if __name__ == "__main__":
    solve()
