# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

from collections import Counter
def can_transform(s, t, p):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    if i < len(s):  
        return "NO"
    s_count = Counter(s)
    t_count = Counter(t)
    p_count = Counter(p)

    for char in t_count:
        needed = t_count[char] - s_count.get(char, 0)
        if needed > p_count.get(char, 0):
            return "NO"
    return "YES"

def solve():
    q = int(input().strip())
    results = []
    for _ in range(q):
        s = input().strip()
        t = input().strip()
        p = input().strip()
        results.append(can_transform(s, t, p))    
    print("\n".join(results))
if __name__ == '__main__':
    solve()
