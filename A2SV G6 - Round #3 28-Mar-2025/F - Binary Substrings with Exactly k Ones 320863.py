# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

def sub_for_k(k,arr):
    if(k==-1):
        return 0
    l=0
    count=0
    ans=0
    for i in range(len(arr)):
        if(arr[i]=='1'):
            count+=1
        while(count>k):
            if(arr[l]=='1'):
                count-=1
            l+=1
        ans+=i-l+1
    return ans

def solve():
    x=int(input())
    y=input() 
    return (sub_for_k(x,y)-sub_for_k(x-1,y))

if __name__=="__main__":
    print(solve())