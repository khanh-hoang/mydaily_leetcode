#Time: O(log(n))
#Space:O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val 
        while root:
            closest = min(root.val, closest, key=lambda x: abs(x-target))
            root = root.left if target < root.val else root.right
        return closest
        
        
        """
        Time: O(n)
        Space:O(n)
        def dfs(node):
            if node:
                dfs(node.left)
                res.append(node.val)
                dfs(node.right)
        res = []
        dfs(root)
        return min(res, key= lambda x: abs(x-target))
        """
        