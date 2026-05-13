# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            head1 = lists.pop(0)
            head2 = lists.pop(0)
            dummy = ListNode()
            prev = dummy
            while head1 and head2:
                prox1 = head1.next
                prox2 = head2.next
                if head1.val < head2.val:
                    prev.next = head1
                    head1 = prox1
                else:
                    prev.next = head2
                    head2 = prox2
                prev = prev.next
            prev.next = head1 or head2
            lists.append(dummy.next)
        return lists[0] if lists else None