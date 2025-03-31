# Problem: D - Creating an a-Good String - https://codeforces.com/gym/596141/problem/D

def solve(s,l, r, c):
    if l == r:
        if s[l] == c:
            return 0
        return 1    
    mid = (l + r) // 2    
    left_changes = (mid - l + 1) - s[l:mid + 1].count(c)    
    left_result = left_changes + solve(s,mid + 1, r, chr(ord(c) + 1)) 
    right_changes = (r - mid) - s[mid + 1:r + 1].count(c)
    right_result = right_changes + solve(s,l, mid, chr(ord(c) + 1)) 
    return min(left_result, right_result)

if __name__=="__main__":
    i=int(input())
    for _ in range(i):
        n = int(input())
        s = input()
        print(solve(s,0, len(s) - 1, 'a'))