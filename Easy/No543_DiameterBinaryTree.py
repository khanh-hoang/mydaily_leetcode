#Time: O(n)
#Space:O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        total = 0
        def path_dfs(node):
            nonlocal total
            if not node:
                return 0
            left_path = path_dfs(node.left)
            right_path = path_dfs(node.right)
            
            total = max(total, left_path + right_path)
            
            return max(left_path, right_path) + 1
        path_dfs(root)
        return total