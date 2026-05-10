class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 != None or l2 != None:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
                
            if l2:
                s += l2.val
                l2 = l2.next

            carry = s//10
            curr.next = ListNode(s % 10)
            curr  = curr.next
		
        if carry:
            curr.next = ListNode(carry)
            
        return dummy.next