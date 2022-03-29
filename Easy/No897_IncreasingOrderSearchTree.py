#Time: O(n)
#Space:O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if node:
                dfs(node.left)
                temp.append(node.val)
                dfs(node.right)
        temp = []
        dfs(root)
        
        dummy = cur = TreeNode()
        for i in temp:
            cur.right = TreeNode(i)
            cur = cur.right
        return dummy.right 
