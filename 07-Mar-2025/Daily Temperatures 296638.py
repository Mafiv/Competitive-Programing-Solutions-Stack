# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        store=[0]*len(temperatures)
        for i,val in enumerate(temperatures):
            while(stack and val>temperatures[stack[-1]]):
                id=stack.pop()
                store[id]=i-id
            stack.append(i)
        return store
        