def diagonalSort(mat: list) -> list:
    rows = len(mat)
    cols = len(mat[0])
    if rows == 1:
        return mat
    if cols == 1:
        return mat

    result = [[0 for y in range(cols)] for x in range(rows)]

    result[rows - 1][0] = mat[rows - 1][0]
    result[0][cols - 1] = mat[0][cols - 1]

    i = 0
    row_s = 0
    col_s = 0
    elem = rows * cols - 2
    temp_list = []
    idx_list = []
    while elem > 0:
        row = row_s
        col = col_s
        for t in range(rows):
            if row >= rows or col >= cols:
                break
            num = mat[row][col]
            temp_list.append(num)
            idx_list.append([row, col])
            row += 1
            col += 1
            elem -= 1
        sorted_list = sorted(temp_list)
        for idx, n in enumerate(sorted_list):
            x = idx_list[idx][0]
            y = idx_list[idx][1]
            result[x][y] = n
        i += 1
        temp_list = []
        idx_list = []
        if i < cols - 1:
            col_s += 1
        else:
            row_s += 1
            col_s = 0

    return result


if __name__ == '__main__':
    assert (diagonalSort([[37, 98, 82, 45, 42]])) == [[37, 98, 82, 45, 42]]
    assert (diagonalSort([[3, 3, 1, 1],
                          [2, 2, 1, 2],
                          [1, 1, 1, 2]])) == [[1, 1, 1, 1],
                                              [1, 2, 2, 2],
                                              [1, 2, 3, 3]]
    assert (diagonalSort(
        [[11, 25, 66, 1, 69, 7],
         [23, 55, 17, 45, 15, 52],
         [75, 31, 36, 44, 58, 8],
         [22, 27, 33, 25, 68, 4],
         [84, 28, 14, 11, 5, 50]])) == [[5, 17, 4, 1, 52, 7],
                                        [11, 11, 25, 45, 8, 69],
                                        [14, 23, 25, 44, 58, 15],
                                        [22, 27, 31, 36, 50, 66],
                                        [84, 28, 75, 33, 55, 68]]
