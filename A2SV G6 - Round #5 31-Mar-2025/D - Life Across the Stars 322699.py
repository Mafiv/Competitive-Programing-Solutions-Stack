# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

from collections import defaultdict
def solve():
    i=int(input())
    dicts=defaultdict(int)
    for j in range(i):
        x=list(map(int,input().split()))
        dicts[x[0]]+=1
        dicts[x[1]]-=1
    p=sorted(dicts.keys())
    population=0
    max_p=0
    year=p[0]
    for i in p:
        population+=dicts[i]
        if(population > max_p):
            year=i
            max_p=population
    return year,max_p
if __name__=="__main__":
    i=1
    for _ in range(i):
        print(*(solve()))