from functools import reduce


def maxIncreaseKeepingSkyline(grid: list) -> int:
    n = len(grid)
    horizontal = []
    vertical = [0 for x in range(n)]

    for elem in grid:
        max_horizontal = max(elem)
        horizontal.append(max_horizontal)
        for idx, num in enumerate(elem):
            if vertical[idx] < elem[idx]:
                vertical[idx] = elem[idx]

    new_grid = []
    grid_elem = []
    for elem in horizontal:
        for e in vertical:
            if e > elem:
                grid_elem.append(elem)
            else:
                grid_elem.append(e)
        new_grid.append(grid_elem)
        grid_elem = []

    grid_sum = 0
    for elem in grid:
        grid_elem_sum = reduce(lambda x, total: x + total, elem)
        grid_sum += grid_elem_sum

    new_grid_sum = 0
    for elem in new_grid:
        new_grid_elem_sum = reduce(lambda x, total: x + total, elem)
        new_grid_sum += new_grid_elem_sum

    result = new_grid_sum - grid_sum

    return result


if __name__ == '__main__':
    assert (maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]])) == 35
    assert (maxIncreaseKeepingSkyline([[0, 0, 0], [0, 0, 0], [0, 0, 0]])) == 0
