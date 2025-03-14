# Problem: B - Nafargi's Binary Reduction Game - https://codeforces.com/gym/594077/problem/B

from collections import Counter
def solve():
  a=int(input())
  x=input()
  c=Counter(str(x))
  res=abs(c['0']-c['1'])
  return res


if __name__=="__main__":
    x=1
    for i in range(x):
        print(solve())