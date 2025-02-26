# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

def solve():
    x=list(map(int,input().split()))
    x.sort()
    a=len(x)
    if(a%2==0):
        return x[a//2-1]
    return x[a//2]
if __name__=="__main__":
    x=int(input())
    print(solve())