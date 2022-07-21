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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                
                #It means not at the end of each level
                if i < size - 1:
                    node.next = queue[0] 
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return root
        """
        #Time: O(n)
        #Space:O(1)
        this solution is more efficient but only when we have perfect binary tree
        if not root:
            return None
        leftNode = root
        while leftNode.left:
            node = leftNode
            while node:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                node = node.next
            leftNode = leftNode.left
        return root
        """