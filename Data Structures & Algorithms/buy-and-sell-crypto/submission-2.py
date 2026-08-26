class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_am = prices[0]
        profits = 0
        for i in prices:
            if profits < i - min_am:
                profits = i - min_am
            if i < min_am:
                min_am = i


        return profits
                
            



            