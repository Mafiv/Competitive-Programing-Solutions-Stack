# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.dummy = Node(0) 
       
    def get(self, index: int) -> int:
        current = self.dummy.next 
        for _ in range(index):
            if not current:
                return -1
            current = current.next
        return current.val if current else -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val) 

    def addAtTail(self, val: int) -> None:
        current = self.dummy
        while current.next:
            current = current.next
        current.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        current = self.dummy  
        for _ in range(index):
            if not current.next:
                return
            current = current.next
        new_node = Node(val)
        new_node.next = current.next
        current.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        current = self.dummy 
        for _ in range(index):
            if not current.next:
                return
            current = current.next
        if current.next:
            current.next = current.next.next

# Example usage:
# obj = MyLinkedList()
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1, 2)  # Linked list: 1 -> 2 -> 3

