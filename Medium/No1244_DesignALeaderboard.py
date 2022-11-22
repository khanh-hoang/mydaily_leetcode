#Time: O(1)     for addScore and reset
#      O(nlogk) for top
#Space:O(n+k)   for n space of scoreboard and k space for heap
class Leaderboard:

    def __init__(self):
        self.scoreboard = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scoreboard:
            self.scoreboard[playerId] = 0
        self.scoreboard[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        for x in self.scoreboard.values():
            heapq.heappush(heap, x)
            if len(heap) > K:
                heapq.heappop(heap)
        res = 0
        while heap:
            res += heapq.heappop(heap)
        return res
    def reset(self, playerId: int) -> None:
        self.scoreboard[playerId] = 0
"""
class Leaderboard(object):

    def __init__(self):
        self.A = collections.Counter()

    def addScore(self, playerId, score):
        self.A[playerId] += score

    def top(self, K):
        return sum(v for i,v in self.A.most_common(K))

    def reset(self, playerId):
        self.A[playerId] = 0
"""

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)