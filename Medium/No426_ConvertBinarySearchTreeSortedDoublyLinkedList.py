"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(node):
            
            nonlocal first, last
            if node:
                dfs(node.left)
                
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node
                last = node
                
                dfs(node.right)
                
        if not root:
            return root
        
        first, last = None, None
        dfs(root)
        
        first.left = last
        last.right = first
        
        return first 