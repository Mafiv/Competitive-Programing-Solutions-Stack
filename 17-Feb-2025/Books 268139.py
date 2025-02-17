# Problem: Books - https://codeforces.com/contest/279/problem/B

import math as m, sys, heapq as heap, collections as cl, itertools, bisect as bi, random as ra

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yn = lambda condition: 'YES' if condition else 'NO'
test = lambda inp=0: number() if not inp else inp
rand = lambda: ra.randint(1, 10000)


def solve():
    a=numbers()
    x=numbers()
    i,j=0,0
    mx=1 if a[1]>x[0] else 0
    sums=x[i]
    while(j<len(x)-1):
        j+=1
        sums+=x[j]
        while(sums>a[1]):
            sums-=x[i]
            i+=1
        mx=max(mx,j-i+1)
    return mx




if __name__=="__main__":
    i=1
    for i in range(i):
        print(solve())