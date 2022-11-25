from functools import reduce


def kWeakestRows(mat: list, k: int) -> list:
    ones = []
    for idx, row in enumerate(mat):
        row_sum = reduce(lambda x, total: total + x, row)
        ones.append(row_sum)

    sort_ones = sorted(ones)
    indexes = []

    for idx, one in enumerate(sort_ones):
        pos = ones.index(one)
        indexes.append(pos)
        ones[pos] = -1
        if idx == k - 1:
            break

    return indexes


if __name__ == '__main__':
    assert (kWeakestRows(mat=
                         [[1, 1, 0, 0, 0],
                          [1, 1, 1, 1, 0],
                          [1, 0, 0, 0, 0],
                          [1, 1, 0, 0, 0],
                          [1, 1, 1, 1, 1]],
                         k=3)) == [2, 0, 3]
    assert (kWeakestRows(mat=
                         [[1, 0, 0, 0],
                          [1, 1, 1, 1],
                          [1, 0, 0, 0],
                          [1, 0, 0, 0]],
                         k=2)) == [0, 2]
