def lastStoneWeight(stones: list) -> int:
    sorted_stones = sorted(stones, reverse=True)

    while len(sorted_stones) >= 2:
        y = sorted_stones[0]
        x = sorted_stones[1]
        if x == y:
            sorted_stones = sorted_stones[2:]
        else:
            sorted_stones.pop(1)
            sorted_stones[0] = y - x
        sorted_stones = sorted(sorted_stones, reverse=True)

    if len(sorted_stones) == 0:
        return 0
    else:
        return sorted_stones[0]


if __name__ == '__main__':
    assert (lastStoneWeight([2, 7, 4, 1, 8, 1])) == 1
    assert (lastStoneWeight([1])) == 1
