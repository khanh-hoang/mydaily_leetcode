class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def myflatten(node):
            if not node:
                return None
            if not node.left and not node.right:
                return node
            
            leftTail  = myflatten(node.left)
            rightTail = myflatten(node.right)
            
            if leftTail:
                leftTail.right = node.right
                node.right = node.left
                node.left = None
            
            return rightTail if rightTail else leftTail
        myflatten(root)