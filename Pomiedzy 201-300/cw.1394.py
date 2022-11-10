def findLucky(arr: list) -> int:
    lucky_numbers = []
    arr_set = set(arr)

    for num in arr_set:
        if num == arr.count(num):
            lucky_numbers.append(num)

    if not lucky_numbers:
        return -1
    else:
        return max(lucky_numbers)


if __name__ == '__main__':
    assert (findLucky([2, 2, 3, 4])) == 2
    assert (findLucky([1, 2, 2, 3, 3, 3])) == 3
    assert (findLucky([2, 2, 2, 3, 3])) == -1
