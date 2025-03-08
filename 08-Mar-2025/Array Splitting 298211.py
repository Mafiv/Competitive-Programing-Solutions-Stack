# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if k == n:
        return 0
    differences = [arr[i] - arr[i-1] for i in range(1, n)]
    differences.sort(reverse=True)
    min_cost = sum(differences) - sum(differences[:k-1])
    return min_cost
 
 
if __name__=="__main__":
    x=1
    for i in range(x):
        print(solve())
