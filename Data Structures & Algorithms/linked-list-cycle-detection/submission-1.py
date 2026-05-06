# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            head = head.next
            if fast == head:
                return True
        return False