class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max = 0
        # for i in range(len(prices)):
        #     print(f"i: {i}")
        #     for j in range(len(prices)-1-i):
        #         j = j+i+1
        #         if prices[j] > prices[i]:
        #             print(f"j: {j}")
        #             print(f"prices[j]: {prices[j]}")
        #             print(f"prices[i]: {prices[i]}")
        #             diff = prices[j] - prices[i]
        #             print(f"diff: {diff}")
        #             if max < diff:
        #                 max = diff
        # return max

        # using dynamic programming
        # we want to find the minimum prices to buy stock and then the maximum price to sell it, but this price should be after we bought it
        maxP = 0
        minBuy = prices[0]
        for price in prices:
            maxP = max(maxP, price-minBuy)
            minBuy = min(minBuy, price)
        return maxP
