def sumZero(n: int) -> list:
    middle = n // 2
    range_start = middle * -1
    range_end = middle
    n_list = [x for x in range(range_start, range_end + 1)]

    if n % 2 == 0:
        n_list.pop(middle)

    return n_list


if __name__ == '__main__':
    assert (sumZero(4)) == [-2, -1, 1, 2]
    assert (sumZero(5)) == [-2, -1, 0, 1, 2]
    assert (sumZero(3)) == [-1, 0, 1]
    assert (sumZero(1)) == [0]
