"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # def __init__(self):
    #     self.visited = {}
    # def cloneGraph(self, node: 'Node') -> 'Node':
    #     if not node:
    #         return node 
        
    #     if node in self.visited:
    #         return self.visited[node]

    #     clone = Node(node.val, [])
    #     self.visited[node] = clone
        
    #     if node.neighbors:
    #         clone.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
    #     return clone 
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        visited = {}

        queue = deque([node])
        visited[node] = Node(node.val, [])
        while queue:
            n = queue.popleft()
            for nei in n.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val, [])
                    queue.append(nei)
                visited[n].neighbors.append(visited[nei])
        return visited[node]


        