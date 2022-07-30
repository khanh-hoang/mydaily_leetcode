# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        def reverseLL(node):
            pre = None
            current = node
            while current:
                nextnode = current.next
                current.next = pre
                pre = current
                current = nextnode
            return pre
        
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        temphead = slow.next
        head2 = reverseLL(temphead)
        slow.next = None
        head1 = head
        #1-2 4-3
        while head2:
            next1 = head1.next
            next2 = head2.next
            
            head1.next = head2
            head1 = next1
            head2.next = head1
            head2 = next2

            
            
            