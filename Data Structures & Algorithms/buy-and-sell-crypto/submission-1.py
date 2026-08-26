class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_am = prices[0]
        profits = 0
        for i in range(0,len(prices)):
            if profits < prices[i] - min_am:
                profits = prices[i] - min_am
            if prices[i] < min_am:
                min_am = prices[i]


        return profits
                
            



            