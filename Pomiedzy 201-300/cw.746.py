def minCostClimbingStairs(cost: list) -> int:
    pre_previous = previous = 0

    for i in range(0, len(cost) - 1):
        current = min(previous + cost[i + 1], pre_previous + cost[i])
        pre_previous = previous
        previous = current
    return previous


if __name__ == '__main__':
    assert (minCostClimbingStairs([0, 1, 2, 2])) == 2
    assert (minCostClimbingStairs([10, 15, 20])) == 15
    assert (minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])) == 6
    assert (minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1, 2])) == 6
