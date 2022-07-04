#Time: O(n)
#Space:O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next or k == 0:
            return head
        
        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n+=1
        tail.next = head
        
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        new_tail.next = None
        return new_head
        
        """
        Time: O(n)
        Space:O(n)
        if not head:
            return None
        queue = deque([])
        cur = head
        while cur:
            queue.append(cur.val)
            cur = cur.next
        
        for i in range(k % len(queue)):
            queue.appendleft(queue.pop())
        
        dummy = cur = ListNode()
        while queue:
            cur.next = ListNode(queue.popleft())
            cur = cur.next
        return dummy.next
        """