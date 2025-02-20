# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        dummy=ListNode()
        itr=dummy
        itr.next=head
        while(itr):
            count+=1
            itr=itr.next
        middle=(count-1)//2
        itr2=dummy
        for i in range(middle+1):
            if(itr2):
                itr2=itr2.next
            else:
                break
        return itr2

        