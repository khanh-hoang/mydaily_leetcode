#Time: O(n)
#Space:O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = []
        def dfs(node):
            if node:
                val.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return len(set(val)) == 1