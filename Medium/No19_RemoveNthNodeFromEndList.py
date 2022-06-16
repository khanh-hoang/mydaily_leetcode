#Time: O(n)
#Space:O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        before = after = dummy
        for i in range(n+1):
            after = after.next
        
        while after:
            after = after.next
            before = before.next
        
        before.next = before.next.next
        return dummy.next
        
        
            