#Time: O(n+m)
#Space:O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointer1 = headA
        pointer2 = headB
        
        while pointer1 != pointer2:
            if pointer1:
                pointer1 = pointer1.next
            else:
                pointer1 = headB
            
            if pointer2:
                pointer2 = pointer2.next
            else:
                pointer2 = headA
            
            
                
        return pointer1