#Time :O(n)
#Space:O(n)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return

        dummy = Node(0, None, head, None)
        prev = dummy
        queue = [head]
        while queue:
            node = queue.pop()
            
            prev.next = node
            node.prev = prev
                
            if node.next:
                queue.append(node.next)
            
            if node.child:
                queue.append(node.child)
                node.child = None
                
            prev = node
            
        dummy.next.prev = None
        return dummy.next