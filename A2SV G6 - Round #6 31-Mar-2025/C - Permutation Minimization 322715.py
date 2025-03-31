# Problem: C - Permutation Minimization - https://codeforces.com/gym/594077/problem/C

from collections import deque
def solve():
  a=int(input())
  x=list(map(int,input().split()))
  ans=deque()
  ans.append(x[0])
  for i in range(1,a):
    if(x[i]>ans[0]):
        ans.append(x[i])
    else:
        ans.appendleft(x[i])
  return ans

if __name__=="__main__":
    x=int(input())
    for i in range(x):
        print(*(solve()))