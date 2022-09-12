def countNegatives(grid: list) -> int:
    counter = 0

    for elem in grid:
        for num in elem:
            if num < 0:
                counter += 1

    return counter


def countNegatives2(grid: list) -> int:
    grid_list = []

    for elem in grid:
        grid_list.extend(elem)

    negative = list(filter(lambda x: x < 0, grid_list))

    return len(negative)


if __name__ == '__main__':
    assert (countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]])) == 8
    assert (countNegatives([[3, 2], [1, 0]])) == 0
    assert (countNegatives2([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]])) == 8
    assert (countNegatives2([[3, 2], [1, 0]])) == 0
