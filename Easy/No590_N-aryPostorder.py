#Time: O(n)
#Space:O(n)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        queue = deque([root])
        
        while queue:
            node = queue.pop()
            if node:
                res.append(node.val)
            for n in node.children:
                queue.append(n)
        return res[::-1]
        
        
        """
        Recursion:
        def dfs(node):
            if node:
                for n in node.children:
                    dfs(n)
                res.append(node.val)
        res = []
        dfs(root)
        return res
        """