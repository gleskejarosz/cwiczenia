def oddCells(m: int, n: int, indices: list) -> int:
    counter = 0
    matrix = [[0 for x in range(n)] for y in range(m)]

    for index in indices:
        row = index[0]
        for c in range(n):
            matrix[row][c] += 1
        col = index[1]
        for r in range(m):
            matrix[r][col] += 1

    for elem in matrix:
        for num in elem:
            if num % 2 == 1:
                counter += 1

    return counter


if __name__ == '__main__':
    assert (oddCells(m=2, n=3, indices=[[0, 1], [1, 1]])) == 6
    assert (oddCells(m=2, n=2, indices=[[1, 1], [0, 0]])) == 0
