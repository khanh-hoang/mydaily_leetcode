#Time: O(n)
#Space:O(n)
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        queue = deque([kill])
        mymap = defaultdict(list)
        for i in range(len(pid)):
            mymap[ppid[i]].append(pid[i])
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for i in mymap[node]:
                queue.append(i)
        return res