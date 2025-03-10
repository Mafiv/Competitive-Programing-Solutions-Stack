# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

x = int(input())

for _ in range(x):
    n = int(input())
    nums = list(map(int, input().split()))
    
    result, count = 0, 1
    
    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            count += 1
        else:
            result += count // 2
            count = 1  # Reset count for the next segment
    
    result += count // 2  # Add the last segment's contribution
    print(result)
