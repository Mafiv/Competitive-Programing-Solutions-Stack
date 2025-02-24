# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        heven = ListNode(0)
        hodd = ListNode(0)
        temp = head

        count = 1
        odd = hodd
        even = heven
        while temp: 
            prev = temp
            temp = temp.next
            if count % 2 != 0:
                odd.next = prev
                odd = odd.next
                prev.next = None
            elif count % 2 == 0:
                even.next = prev
                even = even.next
                prev.next = None
            count += 1
        
        odd.next = heven.next
        
        return hodd.next
