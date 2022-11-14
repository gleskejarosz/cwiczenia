def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> list:
    elem = [rStart, cStart]
    result = [[rStart, cStart]]
    counter = rows * cols
    max_distance = 0
    row = rStart
    col = cStart

    while counter > 1:
        max_distance += 1
        for distance in range(1, max_distance + 1):
            col += 1
            elem = [row, col]
            if 0 <= col < cols and 0 <= row < rows:
                result.append(elem)
                counter -= 1
        for distance in range(1, max_distance + 1):
            row += 1
            elem = [row, col]
            if 0 <= col < cols and 0 <= row < rows:
                result.append(elem)
                counter -= 1
        max_distance += 1
        for distance in range(1, max_distance + 1):
            col -= 1
            elem = [row, col]
            if 0 <= col < cols and 0 <= row < rows:
                result.append(elem)
                counter -= 1
        for distance in range(1, max_distance + 1):
            row -= 1
            elem = [row, col]
            if 0 <= col < cols and 0 <= row < rows:
                result.append(elem)
                counter -= 1

    return result


if __name__ == '__main__':
    assert (spiralMatrixIII(rows=1, cols=4, rStart=0, cStart=0)) == [[0, 0], [0, 1], [0, 2], [0, 3]]
    assert (spiralMatrixIII(rows=5, cols=6, rStart=1, cStart=4)) == [[1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3],
                                                                     [0, 3], [0, 4], [0, 5], [3, 5], [3, 4], [3, 3],
                                                                     [3, 2], [2, 2], [1, 2], [0, 2], [4, 5], [4, 4],
                                                                     [4, 3], [4, 2], [4, 1], [3, 1], [2, 1], [1, 1],
                                                                     [0, 1], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]
    