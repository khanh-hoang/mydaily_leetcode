#Time: O(n)
#Space:O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head 
        slow = head 
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 
            
        if fast != None:
            slow = slow.next 
        
        prev = None
        
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
            
        while prev: 
            if prev.val == head.val:
                prev = prev.next
                head = head.next 
            else:
                return False
        return True 