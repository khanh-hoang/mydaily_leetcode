#Time: O(n)
#Space:O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 
        tempmin = prices[0]
        for price in prices:
            if price < tempmin:
                tempmin = price
            elif price-tempmin > res:
                res = price-tempmin 
        return res