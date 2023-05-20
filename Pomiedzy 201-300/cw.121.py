import sys


def maxProfit(prices):
    max_profit = 0
    for idx, buy_price in enumerate(prices):
        for sell_price in prices[idx + 1:]:
            temp_profit = sell_price - buy_price
            if temp_profit > max_profit:
                max_profit = temp_profit

    return max_profit


def maxProfit1(prices):
    max_profit = 0
    for idx, buy_price in enumerate(prices[:-1]):
        sell_price = max(prices[idx + 1:])
        temp_profit = sell_price - buy_price
        max_profit = max(max_profit, temp_profit)
    return max_profit


def maxProfit2(prices):
    max_num = sys.maxsize
    max_profit = 0

    for i in range(len(prices)):
        price = prices[i]
        if price < max_num:
            max_num = price
        cal_profit = price - max_num
        max_profit = max(max_profit, cal_profit)

    return max_profit


if __name__ == '__main__':
    assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert maxProfit([7, 6, 4, 3, 1]) == 0
    assert maxProfit1([7, 1, 5, 3, 6, 4]) == 5
    assert maxProfit1([7, 6, 4, 3, 1]) == 0
    assert maxProfit1([2, 4, 1]) == 2
    assert maxProfit1([1, 2]) == 1
