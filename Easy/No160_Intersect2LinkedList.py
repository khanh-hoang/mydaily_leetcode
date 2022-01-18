#Time: O(n+m)
#Space:O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        The ptrA will go through a + c + b 
        The ptrB will go through b + c + a
        With a,b is the exclusive part of linked listA, listB
        And c is the common part
        """

        pA = headA
        pB = headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA  
        return pA

        """
        The second solution is getting lenA and lenB, get diff abs(lenA-lenB)
        Jump the pointer of the longer list diff step
        Set the pointer to head of shorter list
        Jump together until they get the same value
        """