def projectionArea(grid: list) -> int:
    len_sum = 0
    max_grid = 0
    grid_elem = [0 for x in grid[0]]
    total_area = 0

    for elem in grid:
        max_grid += max(elem)
        for idx, num in enumerate(elem):
            if grid_elem[idx] < num:
                grid_elem[idx] = num
            if num > 0:
                len_sum += 1

    for num in grid_elem:
        total_area += num

    total_area += len_sum
    total_area += max_grid

    return total_area


if __name__ == '__main__':
    assert (projectionArea([[1, 2], [3, 4]])) == 17
    assert (projectionArea([[2]])) == 5
    assert (projectionArea([[1, 0], [0, 2]])) == 8
