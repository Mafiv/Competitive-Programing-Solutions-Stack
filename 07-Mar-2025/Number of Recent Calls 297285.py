# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:
    def __init__(self):
        self.arr=[]
        self.min=0
    def ping(self, t: int) -> int:
        self.arr.append(t)
        a=self.arr[self.min:]
        count=len(a)
        ans=count
        for j in range(count):
            if( t-3000<=a[j]<=t):
                self.min=j
                break
            else:
                ans-=1
        return ans



        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)