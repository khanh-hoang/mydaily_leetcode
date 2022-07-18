# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preIdx = 0
        self.inIdx = 0
        def build(stop):
            if self.inIdx < len(inorder) and inorder[self.inIdx] != stop:
                                            #inorder[0] != stop
                root = TreeNode(preorder[self.preIdx])
                self.preIdx += 1            #preorder.pop(0)
                root.left = build(root.val)
                self.inIdx += 1             #inorder.pop(0)
                root.right = build(stop)
                return root
            
        
        return build(None)
                
        """
        mymap = {}
        for i, val in enumerate(inorder):
            mymap[val] = i
        
        def build(low, high):
            if low > high:
                return
            x = TreeNode(preorder[self.preIdx])
            self.preIdx += 1
            mid = mymap[x.val]
            x.left = build(low, mid-1)
            x.right = build(mid+1, high)
            return x
        
        self.preIdx = 0
        return build(0, len(preorder) - 1)
        """