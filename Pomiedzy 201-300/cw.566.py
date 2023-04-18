def matrixReshape(mat: list, r: int, c: int) -> list:
    temp_list = []
    mat_len = 0
    for elem in mat:
        for num in elem:
            temp_list.append(num)
            mat_len += 1

    new_mat = []
    max_mat = r * c
    if max_mat != mat_len:
        return mat

    for row in range(r):
        new_mat.append(temp_list[row * c: row * c + c])

    return new_mat


if __name__ == '__main__':
    assert (matrixReshape(mat=[[1, 2]], r=1, c=1)) == [[1, 2]]
    assert (matrixReshape(mat=
                          [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18],
                           [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30]], r=22, c=15)) == [[1, 2, 3, 4, 5, 6],
                                                                                                 [7, 8, 9, 10, 11, 12],
                                                                                                 [13, 14, 15, 16, 17,
                                                                                                  18],
                                                                                                 [19, 20, 21, 22, 23,
                                                                                                  24],
                                                                                                 [25, 26, 27, 28, 29,
                                                                                                  30]]
    assert (matrixReshape(mat=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]], r=42,
                          c=5)) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
    assert (matrixReshape(mat=[[1, 2], [3, 4]], r=4, c=1)) == [[1], [2], [3], [4]]
    assert (matrixReshape(mat=[[1, 2], [3, 4]], r=1, c=4)) == [[1, 2, 3, 4]]
    assert (matrixReshape(mat=[[1, 2], [3, 4]], r=2, c=4)) == [[1, 2], [3, 4]]
