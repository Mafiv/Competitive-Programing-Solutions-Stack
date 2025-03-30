# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0] * n
suffix = [0] * n

for i in range(1, n):
    prefix[i] = prefix[i - 1] + max(0, arr[i - 1] - arr[i])
for i in range(n - 2, -1, -1):
    suffix[i] = suffix[i + 1] + max(0, arr[i + 1] - arr[i])     

for _ in range(m):
    a, b = map(int, input().split())
    if b > a:
        print(prefix[b - 1] - prefix[a - 1])
    else:
        print(suffix[b - 1] - suffix[a - 1])