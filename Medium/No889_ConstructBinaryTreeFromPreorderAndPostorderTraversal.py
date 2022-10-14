#Time: O(n)
#Space:O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        stack = [TreeNode(preorder[0])]
        j = 0
        for n in preorder[1:]:
            node = TreeNode(n)
            while stack[-1].val == postorder[j]:
                stack.pop()
                j+=1
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
        """
        Time: O(n)
        Space:O(h)
        preIdx, postIdx = 0, 0
        def constructFromPrePost(self, preorder: List[int], postorder: List[int]) ->        Optional[TreeNode]:
            root = TreeNode(preorder[self.preIdx])
            self.preIdx += 1
            if root.val != postorder[self.postIdx]:
                root.left = self.constructFromPrePost(preorder, postorder)
            if root.val != postorder[self.postIdx]:
                root.right = self.constructFromPrePost(preorder, postorder)
            self.postIdx +=1
            return root

        """
            
            