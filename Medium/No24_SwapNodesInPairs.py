#Time: O(n)
#Space:O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        
        while head and head.next:
            first_node = head
            second_node = head.next
            
            pre.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            
            pre = first_node
            head = first_node.next
        
        return dummy.next
            
        
        """
        #Time: O(n)
        #Space:O(1)
        def swap(node):
            if not node or not node.next:
                return node
            
            first_node = node
            second_node = node.next
            
            first_node.next = swap(second_node.next)
            second_node.next = first_node

            return second_node
            
        return swap(head)
        """