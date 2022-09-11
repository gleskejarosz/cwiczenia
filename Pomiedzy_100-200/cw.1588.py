def sumOddLengthSubarrays(arr: list) -> int:
    result = 0
    arrays = []
    arr_len = len(arr)

    odds = [x for x in range(3, arr_len + 1) if x % 2 == 1]

    for num in arr:
        result += num

    for elem in odds:
        max_idx = arr_len - elem
        for idx, num in enumerate(arr):
            if idx > max_idx:
                break
            temp_arr = arr[idx: idx + elem]
            arrays.append(temp_arr)

    for elem in arrays:
        for num in elem:
            result += num

    return result


if __name__ == '__main__':
    assert (sumOddLengthSubarrays([1, 4, 2, 5, 3])) == 58
    assert (sumOddLengthSubarrays([1, 2])) == 3
    assert (sumOddLengthSubarrays([10, 11, 12])) == 66
