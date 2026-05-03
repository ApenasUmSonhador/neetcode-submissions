class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = None
        curr = head
        
        while curr != None:
            next_node = curr.next
            curr.next = new
            new = curr
            curr = next_node
        return new