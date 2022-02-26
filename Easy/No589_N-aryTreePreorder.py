#Time :O(n)
#Space:O(n)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        queue = deque([(root)])
        res = []
        
        while queue:
            node = queue.pop()
            res.append(node.val)
            queue.extend(node.children[::-1])
        
        return res
        """
        def dfs(node):
            if node:
                res.append(node.val)
                for child in node.children:
                    dfs(child)
        
        res = []
        dfs(root)
        return res
        """