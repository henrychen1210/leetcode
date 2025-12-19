class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        priceSum = [0] * (n + 1)
        profitSum = [0] * (n + 1)

        for i in range(n):
            priceSum[i + 1] = priceSum[i] + prices[i]
            profitSum[i + 1] = profitSum[i] + prices[i] * strategy[i]
        
        res = profitSum[n]
        
        for i in range(k - 1, n):
            left = profitSum[i - k + 1]
            right = profitSum[n] - profitSum[i + 1]
            change = priceSum[i + 1] - priceSum[i - k // 2 + 1]
            res = max(res, left + right + change)
        return res 