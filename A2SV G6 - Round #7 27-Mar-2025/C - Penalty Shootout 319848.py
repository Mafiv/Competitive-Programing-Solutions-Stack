# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

def calculate(arr1,arr2):
    itr=0
    scor1=0
    scor2=0
    # win=0
    for i,val in enumerate(arr1):
        # print(scor1,scor2)
        if(val==1):
            scor1+=1
        itr+=1
        if(scor1>scor2):
            # print(scor1,scor2,"a remain",5-i-1,"first")
            if(scor1-scor2>5-i):
                return itr
        else:
            # print(scor1,scor2,"b remain",5-i,"first",i)
            if(scor2-scor1>5-(i+1)):
                return itr
        if(arr2[i]==1):
            scor2+=1
        itr+=1
        # print(scor1,scor2)

        if(scor1>scor2):
            # print(scor1,scor2,"a remain",5-i-1,"second")
            if(scor1-scor2>5-i-1):
                return itr
        else:
            # print(scor1,scor2,"b remain",5-i-1,"second")
            if(scor2-scor1>5-i-1):
                return itr
    return itr
        

def  win(a,b):
    n=[]
    f=[]
    for i in a:
        if(i=='?'):
            n.append(1)
        else:
            n.append(int(i))
    for i in b:
        if(i=='?'):
            f.append(0)
        else:
            f.append(int(i))
    return (n,f)



def main():
    n=int(input())
    for i in range(n):
        x=list(input())
        a=[]
        b=[]
        for i in range(len(x)):
            if(i%2==0):
                a.append(x[i])
            else:
                b.append(x[i])
        win_a,loss_b=win(a,b)
        win_b,loss_a=win(b,a)
        # print(win_a,loss_b)
        # print(win_b,loss_a)
        # print(b)
        t1=calculate(win_a,loss_b)
        # print("______________________________")
        t2=calculate(loss_a,win_b,)
        print(min(t1,t2))
    return 
    
if __name__ == '__main__':
    main()