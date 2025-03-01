# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next        
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        curr = head        
        while count >= k:  
            prev = None
            tail = curr  
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node            
            prev_group_end.next = prev
            tail.next = curr
            prev_group_end = tail              
            count -= k
        return dummy.next
        