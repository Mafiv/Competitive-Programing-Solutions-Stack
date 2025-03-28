# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

def solve():
    a=int(input())
    x=list(map(int,input().split()))    
    b=int(input())
    y=list(map(int,input().split()))    
    sum_x=0
    sum_y=0
    up,down=0,0
    ans=0
    if(sum(x)!=sum(y)):
        return -1
    while(up<a and down<b):
        sum_x+=x[up]
        sum_y+=y[down]
        up+=1
        down+=1
        while(sum_x != sum_y):
            if(sum_x<sum_y):
                sum_x+=x[up]
                up+=1
            else:
                sum_y+=y[down]                
                down+=1
            
        ans+=1
    return ans





if __name__=="__main__":
    # i=int(input())
    for _ in range(1):
        print(solve())