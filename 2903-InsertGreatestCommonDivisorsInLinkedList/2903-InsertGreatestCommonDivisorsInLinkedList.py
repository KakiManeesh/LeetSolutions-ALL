# Last updated: 7/3/2026, 12:49:59 PM
import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while (current.next):
            newnode = ListNode(math.gcd(current.val,current.next.val))
            newnode.next = current.next
            current.next = newnode
            current = current.next.next
        return head