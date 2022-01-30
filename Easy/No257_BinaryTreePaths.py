#Time: O(n)
#Space:O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        paths = []
        queue = deque([(root, str(root.val))])
        
        while queue:
            node, path = queue.popleft()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                queue.append((node.left, path+"->"+str(node.left.val)))
            if node.right:
                queue.append((node.right, path+"->"+str(node.right.val)))
        return paths
    
        """
        DFS recursion
        Time: O(n)
        Space:O(n)
        def dfs(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += "->"
                    dfs(root.left, path)
                    dfs(root.right, path)
        
        paths = []
        dfs(root, "")
        return paths
        """
        
                