class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 != None or l2 != None:
            s = carry
            s += l1.val if l1 else 0
            s += l2.val if l2 else 0
            carry = s//10

            curr.next = ListNode(s % 10)
            curr  = curr.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            curr.next = ListNode(carry)
        
        return dummy.next