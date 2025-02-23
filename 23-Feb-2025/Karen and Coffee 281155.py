# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

def solve():
    n, k, q = map(int, input().split())
    MAX_T = 200000  
    freq = [0] * (MAX_T + 2)  
    for _ in range(n):
        l, r = map(int, input().split())
        freq[l] += 1
        freq[r + 1] -= 1
    prefix = [0] * (MAX_T + 1)
    for i in range(1, MAX_T + 1):
        prefix[i] = prefix[i - 1] + freq[i]
    is_admissible = [0] * (MAX_T + 1)
    for i in range(1, MAX_T + 1):
        is_admissible[i] = 1 if prefix[i] >= k else 0
    admissible_prefix = [0] * (MAX_T + 1)
    for i in range(1, MAX_T + 1):
        admissible_prefix[i] = admissible_prefix[i - 1] + is_admissible[i]
    results = []
    for _ in range(q):
        a, b = map(int, input().split())
        results.append(str(admissible_prefix[b] - admissible_prefix[a - 1]))
    print("\n".join(results))
solve()
