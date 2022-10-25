def finalPrices(prices: list) -> list:
    result = []
    prices_len = len(prices)
    loop = 0

    for idx, price in enumerate(prices):
        loop += 1
        for j in range(idx + 1, prices_len):
            price_j = prices[j]
            if price >= price_j:
                result.append(price - price_j)
            if loop == len(result):
                break
        if loop > len(result):
            result.append(price)

    return result


if __name__ == '__main__':
    assert (finalPrices([8, 4, 6, 2, 3])) == [4, 2, 4, 2, 3]
    assert (finalPrices([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
    assert (finalPrices([10, 1, 1, 6])) == [9, 0, 1, 6]
