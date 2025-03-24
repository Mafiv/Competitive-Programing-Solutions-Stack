# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import defaultdict

def solve():
    n = int(input())
    numbers = list(map(int, input().split()))
    num_count = defaultdict(int)   
    count_freq = defaultdict(int)  
    highest_freq = 0  
    for num in numbers:
        num_count[num] += 1
        new_count = num_count[num]
        count_freq[new_count] += 1  
        highest_freq = max(highest_freq, new_count) 
    max_removal_group = 0
    for freq, freq_count in count_freq.items():
        max_removal_group = max(max_removal_group, freq * freq_count)
    return n - max_removal_group


if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        print(solve())
