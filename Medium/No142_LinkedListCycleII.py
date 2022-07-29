#Time: O(n)
#Space:O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        temp = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                temp = slow
                break
            
        if not temp:
            return None
        
        ptr1 = head
        ptr2 = temp
        while ptr1 != ptr2:
            ptr1 = ptr1.next 
            ptr2 = ptr2.next
        
        return ptr1
    
        
        """
        Time: O(n)
        Space:O(n)
        seen = set()
        
        node = head
        while node:
            if node not in seen:
                seen.add(node)
                node = node.next
            else:
                return node
        return None
        """