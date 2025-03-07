# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

def max_prefix_sum(arr):
    max_sum = 0
    current_sum = 0
    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)
    return max_sum

def solve():
    n = int(input().strip())
    r = list(map(int, input().strip().split()))
    m = int(input().strip())
    b = list(map(int, input().strip().split()))

    max_r = max_prefix_sum(r)
    max_b = max_prefix_sum(b)

    print(max(0, max_r + max_b))

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        solve()
