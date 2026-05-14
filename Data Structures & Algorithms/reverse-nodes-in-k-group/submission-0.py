# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _reverseLinkedList(self, head):
        new = None
        curr = head
        while curr != None:
            next_node = curr.next
            curr.next = new
            new = curr
            curr = next_node
        return new

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        dummy = ListNode(0,head)
        l, m = dummy, dummy.next
        while m:
            for _ in range(k-1):
                m = m.next
                if not m:
                    return dummy.next
            
            r = m.next
            m.next = None
            tail = l.next
            l.next = self._reverseLinkedList(l.next)
            tail.next = r
            l = tail
            m = r
        return dummy.next
