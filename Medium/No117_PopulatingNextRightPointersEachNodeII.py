#Time: O(n)
#Space:O(n)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque([root])
        while queue:
            size = len(queue)
            
            for i in range(size):
                node = queue.popleft()
                
                if i < size - 1:
                    node.next = queue[0]
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)           
        return root
        
        """
        Time: O(n)
        Space:O(1)
        This solution is more efficient in space but it's more complicated as well
        def process(child, pre, leftmost):
            if child:
                if pre:
                    pre.next = child
                else:
                    leftmost = child
                pre = child
            return pre, leftmost
        
        if not root:
            return root
        
        leftmost = root
        
        while leftmost:
            pre, cur = None, leftmost
            leftmost = None
            
            while cur:
                pre, leftmost = process(cur.left, pre, leftmost)
                pre, leftmost = process(cur.right, pre, leftmost)
                cur = cur.next
        return root
        """