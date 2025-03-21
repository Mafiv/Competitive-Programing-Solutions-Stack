# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque
def solve():
    a=list(map(int,input().split()))
    x=list(map(int,input().split()))
    ans=0
    maxStk=deque()
    minStk=deque()
    maxStk.append(x[0])
    minStk.append(x[0])
    r=0
    for i in range(1,a[0]):
        while(maxStk and maxStk[-1]<x[i]):
            maxStk.pop()
        maxStk.append(x[i])
        while(minStk and minStk[-1]>x[i]):
            minStk.pop()
        minStk.append(x[i])
        

        while(maxStk and minStk and  maxStk[0]-minStk[0]>a[1]):
            if(maxStk[0]==x[r]):
                maxStk.popleft()
            elif(minStk[0]==x[r]):
                minStk.popleft()            
            else:
                pass
            ans+=i-r
            r+=1
    f=a[0]-r
    for i in range(f,0,-1):
        ans+=i
    return ans


if __name__=="__main__":
    x=1
    for i in range(x):
        print(solve())