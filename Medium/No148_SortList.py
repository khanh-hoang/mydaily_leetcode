# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        
        return self.merge(left, right)
    
    def getMid(self, head):
        slow,fast = head,head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None 
        return mid 
    
    def merge(self, l1, l2):
        cur = dummy = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2 
        return dummy.next