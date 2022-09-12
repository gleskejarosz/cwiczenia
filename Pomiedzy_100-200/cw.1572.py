def diagonalSum(mat: list) -> int:
    n = len(mat)
    sum_mat = 0
    start = 0
    end = n - 1

    for elem in mat:
        if start != end:
            sum_mat += elem[start]
            sum_mat += elem[end]
        if start == end:
            sum_mat += elem[start]
        start += 1
        end -= 1

    return sum_mat


if __name__ == '__main__':
    assert (diagonalSum([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])) == 25
    assert (diagonalSum([[1, 1, 1, 1],
                         [1, 1, 1, 1],
                         [1, 1, 1, 1],
                         [1, 1, 1, 1]])) == 8
    assert (diagonalSum([[5]])) == 5
