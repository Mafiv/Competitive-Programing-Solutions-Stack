# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class ListNode:
    def __init__(self, val="",prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = ListNode(homepage)    
    

    def visit(self, url: str) -> None:
        newNode = ListNode(url, self.current, None)
        self.current.next = newNode
        self.current = newNode
        

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.current.prev:
                self.current = self.current.prev
            else:
                break
        return self.current.val
    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.current.next:
                self.current = self.current.next
            else:
                break
        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
