# leetcode 121. Best Time to Buy and Sell Stock

def maxProfit(prices):
    # 주식의 변화(prices)가 주어졌을 때
    # 사고 팔 때 얻을 수 있는 최대 이익
    # 싸게 사고, 비싸게 팔아
    buy = 0         # 살 때
    sell = buy + 1  # 팔 때
    maxprofit = 0   # 최대 이익

    while sell < len(prices):
        print(buy, sell, maxprofit, prices[sell] - prices[buy])
        if prices[sell] > prices[buy]:      # 살 때 보다 팔 때가 비싼 경우
            maxprofit = max(maxprofit, prices[sell] - prices[buy])

        if prices[buy] > prices[sell]:      # 더 싸게 살 수 있는 경우 
            buy = sell

        sell += 1

    return maxprofit

print(maxProfit([7,1,5,3,6,4]))  # 5
print(maxProfit([7, 6, 4, 3, 2, 1]))  # 0