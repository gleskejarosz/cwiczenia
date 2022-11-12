def maxCoins(piles: list) -> int:
    piles_len = len(piles)
    qty = piles_len // 3
    piles_sorted = sorted(piles, reverse=True)
    result = 0
    my_indexes = []

    for index in range((piles_len - qty + 1)):
        if index % 2 == 1:
            my_indexes.append(index)

    for idx in my_indexes:
        result += piles_sorted[idx]

    return result


if __name__ == '__main__':
    assert (maxCoins([2, 4, 1, 2, 7, 8])) == 9
    assert (maxCoins([2, 4, 5])) == 4
    assert (maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4])) == 18
