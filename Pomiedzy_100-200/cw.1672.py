from functools import reduce


def maximumWealth(accounts: list) -> int:
    wealth = []

    for account in accounts:
        temp_sum = reduce(lambda money, total: total + money, account)
        wealth.append(temp_sum)

    return max(wealth)


if __name__ == '__main__':
    assert (maximumWealth([[1, 2, 3], [3, 2, 1]])) == 6
    assert (maximumWealth([[1, 5], [7, 3], [3, 5]])) == 10
    assert (maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]])) == 17
