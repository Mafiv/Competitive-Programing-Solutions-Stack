# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

def preprocess_prefix_sums(arr):
    prefix_sums = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        prefix_sums[i] = prefix_sums[i - 1] + arr[i - 1]
    return prefix_sums

def solve(n, values, m, queries):
    original_prefix_sum = preprocess_prefix_sums(values)
    sorted_values = sorted(values)
    sorted_prefix_sum = preprocess_prefix_sums(sorted_values)
    result = []
    for query in queries:
        query_type, l, r = query
        if query_type == 1:
            result.append(original_prefix_sum[r] - original_prefix_sum[l - 1])
        else:
            result.append(sorted_prefix_sum[r] - sorted_prefix_sum[l - 1])
    print("\n".join(map(str, result)))

if __name__ == '__main__':
    n = int(input().strip())
    values = list(map(int, input().split()))
    m = int(input().strip())
    queries = [tuple(map(int, input().split())) for _ in range(m)]
    solve(n, values, m, queries)
