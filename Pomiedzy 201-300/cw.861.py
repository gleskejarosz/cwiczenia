def matrixScore(grid: list):
    rows, cols = len(grid), len(grid[0])
    result = (1 << cols - 1) * rows
    for j in range(1, cols):
        current = 0
        for i in range(rows):
            if grid[i][j] == grid[i][0]:
                current += 1
        result += max(current, rows - current) * (1 << cols - 1 - j)
    return result


if __name__ == '__main__':
    assert (matrixScore([[1, 1], [1, 1], [0, 1]])) == 8
    assert (matrixScore([[0, 1], [0, 0]])) == 5
    assert (matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]])) == 39
    assert (matrixScore([[0]]))
