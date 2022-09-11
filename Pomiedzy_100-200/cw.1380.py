def luckyNumbers(matrix: list) -> list:
    rows = len(matrix)
    cols = len(matrix[0])
    min_row = []
    max_col = []
    temp_list = []
    result = []

    for elem in matrix:
        min_row.append(min(elem))

    for c in range(cols):
        for r in range(rows):
            temp_list.append(matrix[r][c])
        max_col.append(max(temp_list))
        temp_list = []

    test = []
    for num in min_row:
        if num in max_col:
            test.append(num)

    if len(test) == 0:
        return []

    for number in test:
        row = min_row.index(number)
        pos = matrix[row].index(number)
        if number == max_col[pos]:
            result.append(number)

    return result


if __name__ == '__main__':
    assert (luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]])) == [15]
    assert (luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]])) == [12]
    assert (luckyNumbers([[7, 8], [1, 2]])) == [7]
