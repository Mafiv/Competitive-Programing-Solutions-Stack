# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.queue=[]
    def push(self, x: int) -> None:
        return self.queue.append(x)
    def pop(self) -> int:
        return self.queue.pop()    
    def top(self) -> int:
        return self.queue[-1] if self.queue else None
    def empty(self) -> bool:
        return False if self.queue else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()