#Time: O(2^n * n)
#Space:O(2^n * n)
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        result = []
        def dfs(node, path):
            if node == target:
                result.append(path)
                return
            
            for n in graph[node]:
                dfs(n, path+[n])
        
        dfs(0, [0])
        return result