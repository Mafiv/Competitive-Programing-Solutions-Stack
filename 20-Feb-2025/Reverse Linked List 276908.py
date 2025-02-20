# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr=ListNode()
        itr.next=head
        itr=itr.next
        # ans=dummy
        c=1
        prv=None
        while(itr):
            newnode=ListNode(itr.val)
            newnode.next=prv
            prv=newnode
            itr=itr.next
            # ans.next=itr
            # itr=itr.next
        return prv

