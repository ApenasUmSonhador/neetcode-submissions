# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 1
        l = head
        while l != None:
            l = l.next
            size += 1
        i = size - n
        print(i)
        if i == 1:
            return head.next
        l = head
        for _ in range(i-2):
            l = l.next
        
        r = l.next.next if l and l.next else None
        l.next = r 
        return head