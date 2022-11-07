def replaceElements(arr: list) -> list:
    result = []

    for idx, elem in enumerate(arr):
        right_arr = arr[idx + 1:]
        if right_arr:
            max_num = max(right_arr)
            result.append(max_num)
        else:
            result.append(-1)

    return result


if __name__ == '__main__':
    assert (replaceElements([17, 18, 5, 4, 6, 1])) == [18, 6, 6, 6, 1, -1]
    assert (replaceElements([400])) == [-1]
