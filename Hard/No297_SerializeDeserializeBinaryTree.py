#Time: O(n)
#Space:O(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        ans = ""
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                ans += str(node.val) + ","
                queue.append(node.left)
                queue.append(node.right)
            else:
                ans += "None,"
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        mylist = data.split(',')
        root = TreeNode(mylist[0])
        queue = deque([root])
        i = 1
        while queue and i < len(mylist):
            node = queue.popleft()
            if mylist[i] != 'None':
                node.left = TreeNode(mylist[i])
                queue.append(node.left)
            i += 1
            
            if mylist[i] != 'None':
                node.right = TreeNode(mylist[i])
                queue.append(node.right)
            i += 1
        return root
            
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))