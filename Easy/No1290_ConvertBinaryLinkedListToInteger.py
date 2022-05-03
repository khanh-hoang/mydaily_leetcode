# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head:
            res = (res<<1) + head.val
            head = head.next
        return res
        
        
        """
        bad solution
        res = []
        ans = 0
        while head:
            res.append(head.val)
            head = head.next
        for i, v in enumerate(res):
            if v:
                ans += 2**(len(res)-1-i)
        return ans
        """