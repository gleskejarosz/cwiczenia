def largestLocal(grid: list) -> list:
    n = len(grid) - 2
    temp_matrix = []
    result = [[0 for x in range(n)] for x in range(n)]
    col = 0
    row = 0
    iterations = n ** 2
    max_elem = 0
    loop = n - 1

    for i in range(iterations):
        temp_matrix.append(grid[row][col: col + 3])
        temp_matrix.append(grid[row + 1][col: col + 3])
        temp_matrix.append(grid[row + 2][col: col + 3])
        for elem in temp_matrix:
            new_max_elem = max(elem)
            if new_max_elem > max_elem:
                max_elem = new_max_elem
        result[row][col] = max_elem
        if loop > 0:
            col += 1
            loop -= 1
        else:
            row += 1
            col = 0
            loop = n - 1
        temp_matrix = []
        max_elem = 0

    return result


if __name__ == '__main__':
    assert (largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]])) == [[9, 9], [8, 6]]
    assert (largestLocal([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])) == [
         [2, 2, 2], [2, 2, 2], [2, 2, 2]]
    assert(largestLocal([[20, 8, 20, 6, 16, 16, 7, 16, 8, 10], [12, 15, 13, 10, 20, 9, 6, 18, 17, 6],
           [12, 4, 10, 13, 20, 11, 15, 5, 17, 1], [7, 10, 14, 14, 16, 5, 1, 7, 3, 11],
           [16, 2, 9, 15, 9, 8, 6, 1, 7, 15], [18, 15, 18, 8, 12, 17, 19, 7, 7, 8], [19, 11, 15, 16, 1, 3, 7, 4, 7, 11],
           [11, 6, 5, 14, 12, 18, 3, 20, 14, 6], [4, 4, 19, 6, 17, 12, 8, 8, 18, 8],
           [19, 15, 14, 11, 11, 13, 12, 6, 16, 19]])) == [[20, 20, 20, 20, 20, 18, 18, 18],
            [15, 15, 20, 20, 20, 18, 18, 18], [16, 15, 20, 20, 20, 15, 17, 17], [18, 18, 18, 17, 19, 19, 19, 15],
            [19, 18, 18, 17, 19, 19, 19, 15], [19, 18, 18, 18, 19, 20, 20, 20], [19, 19, 19, 18, 18, 20, 20, 20],
                                                          [19, 19, 19, 18, 18, 20, 20, 20]]
