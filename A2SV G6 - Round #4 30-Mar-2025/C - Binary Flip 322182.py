# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C


def solve():
    n = int(input())
    s1 = input()
    s2 = input()
    s1 += '0'
    s2 += '0'
    count = 0    
    for i in range(n):
        if s1[i] == '1':
            count += 1
        else:
            count -= 1        
        if count != 0:
            if s1[i] != s2[i] and s1[i+1] == s2[i+1]:
                print("NO")
                return            
            elif s1[i] == s2[i] and s1[i+1] != s2[i+1]:
                print("NO")
                return    
    print("YES")

t = int(input())
for _ in range(t):
    solve()