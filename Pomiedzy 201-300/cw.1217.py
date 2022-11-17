def minCostToMoveChips(position: list) -> int:
    counter = []
    temp_counter = 0
    test_positions = set(position)

    for test_pos in test_positions:
        for num in position:
            if abs(num - test_pos) % 2 == 1:
                temp_counter += 1
        counter.append(temp_counter)
        temp_counter = 0

    return min(counter)


if __name__ == '__main__':
    assert (minCostToMoveChips([1, 2, 3])) == 1
    assert (minCostToMoveChips([2, 2, 2, 3, 3])) == 2
    assert (minCostToMoveChips([1, 1000000000])) == 1
