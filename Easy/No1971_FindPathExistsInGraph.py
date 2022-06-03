#Time: O(n+m) n:edges, m:range of value
#Space:O(n+m)
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        neighbor = defaultdict(list)
        
        for n1, n2 in edges:
            neighbor[n1].append(n2)
            neighbor[n2].append(n1)
        
        queue = deque([start])
        seen = set([start])
        
        while queue:
            node = queue.popleft()
            if node == end:
                return True
            for n in neighbor[node]:
                if n not in seen:
                    seen.add(n)
                    queue.append(n)
        return False
            