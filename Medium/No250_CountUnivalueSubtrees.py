#Time: O(n)
#Space:O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def count(root):
            if not root.left and not root.right:
                self.res += 1
                return True
            
            uni = True
            
            if root.left:
                uni = count(root.left) and uni and root.left.val == root.val
            
            if root.right:
                uni = count(root.right) and uni and root.right.val == root.val
            
            self.res += uni
            return uni
        
        self.res = 0
        if not root:
            return 0 
        count(root)
        return self.res