# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

def max_f_a_plus_f_b(n, s):
    prefix_count = set()
    suffix_count = {}
    for ch in s:
        suffix_count[ch] = suffix_count.get(ch, 0) + 1
    max_value = 0
    for i in range(n - 1): 
        prefix_count.add(s[i])
        suffix_count[s[i]] -= 1
        if suffix_count[s[i]] == 0:
            del suffix_count[s[i]]
        max_value = max(max_value, len(prefix_count) + len(suffix_count))
    return max_value

def solve():
    t = int(input().strip()) 
    results = []
    for _ in range(t):
        n = int(input().strip()) 
        s = input().strip() 
        results.append(str(max_f_a_plus_f_b(n, s)))
    print("\n".join(results))
if __name__ == "__main__":
    solve()
