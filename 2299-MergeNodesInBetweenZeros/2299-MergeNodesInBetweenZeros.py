# Last updated: 7/3/2026, 1:01:34 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        visited0 = False
        sum = 0
        head1 = None
        new = None

        while current:
            if current.val == 0:
                if visited0:
                    node = ListNode(sum)
                    if new:
                        new.next = node
                        new = new.next
                    else:
                        head1 = node
                        new = node
                    sum = 0
                else:
                    visited0 = True
            else:
                sum += current.val
            current = current.next
        
        return head1
