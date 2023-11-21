x=int(input())
z=[]
d=[]
for i in range(x):
    a=int(input())
    z.append(list(map(int ,input().split())))
for i in z:
    sums=0
    a=i[0]
    for j in i:
        if(a<0):
            if(j>a and j<0):
                a=j
            elif(j>0):
                sums+=a
                a=j
        else:
            if(j>a):
                a=j
            elif(j<0):
                sums+=a
                a=j
    sums+=a
    d.append(sums)
for i in d:
    print(i)
