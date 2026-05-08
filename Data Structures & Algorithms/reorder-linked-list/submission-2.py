# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half
        right = slow.next
        prev = slow.next = None
        while right:
            tmp = right.next
            right.next = prev
            prev = right
            right = tmp
        
        # Merge
        left, right = head, prev
        while right:
            tmp1, tmp2 = left.next, right.next
            left.next = right
            right.next = tmp1
            left, right = tmp1, tmp2
        