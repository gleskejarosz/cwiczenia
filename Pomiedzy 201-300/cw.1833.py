def maxIceCream(costs: list, coins: int) -> int:
    sorted_costs = sorted(costs)
    counter = 0

    for cost in sorted_costs:
        coins -= cost
        counter += 1
        if coins == 0:
            return counter
        if coins < 0:
            return counter - 1
    return counter


if __name__ == '__main__':
    assert (maxIceCream(costs=[1, 3, 2, 4, 1], coins=7)) == 4
    assert (maxIceCream(costs=[10, 6, 8, 7, 7, 8], coins=5)) == 0
    assert (maxIceCream(costs=[1, 6, 3, 1, 2, 5], coins=20)) == 6
