'''
This can be solved using a sliding window.
Set pointers to keep track of the buy and sell prices
Check and keep track of the maximum profit
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxProfit = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]: #only sell if the price is higher than the buy price
                maxProfit = max(maxProfit, prices[sell] - prices[buy]) #keep track of the max profit
            else:
                buy = sell #if the sell price is lower, move the buy price up
            sell += 1 #move the sell price up                
        return maxProfit #return the max profit
        