#Time: O(n)
#Space:O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node):
            if not node:
                return -1
            level = max(dfs(node.left), dfs(node.right)) + 1
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            return level
        
        res = []
        dfs(root)
        return res