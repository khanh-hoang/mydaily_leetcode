#Time: O(n)
#Space:O(1)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pre_one = pre_two = 0
        
        for i in range(2, len(cost)+1):
            temp = pre_one
            pre_one = min(pre_one+cost[i-1], pre_two+cost[i-2])
            pre_two = temp
        return pre_one
        
        """
        Time: O(n)
        Space:O(n)
        minimumCost = [0] * (len(cost)+1)
        for i in range(2, len(cost)+1):
            onestep = minimumCost[i-1] + cost[i-1]
            twostep = minimumCost[i-2] + cost[i-2]
            minimumCost[i] = min(onestep, twostep)
        return minimumCost[-1]
        """
        