# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

x=int(input())

for index in range(x):
    a=list(map(int,input().split()))
    k=[]
    for i in range(a[0]):
        k.append(list(map(int,input().split())))
   

    mx=0
    id=len(k)-1
    ids=len(k[0])-1
  
    
    for i in range(id+1):
        for j in range(ids+1):
            sums=0
            lk=[i-j,0] if i>j else [0,j-i]
            r,c=i,j
            while(c<ids and r>0):#here
                r-=1
                c+=1
            # print("main diagonal")
            while(lk[0]<=id and lk[1]<=ids):
                # print(lk[0],lk[1])
                sums+=k[lk[0]][lk[1]]
                lk[0]+=1
                lk[1]+=1
            # print("second diagonal")
            while(r<=id and c>=0):
                sums+=k[r][c]
                r+=1
                c-=1
            sums-=k[i][j]
            mx=max(mx,sums)
    print(mx)






 