def sortByBits(arr: list) -> list:
    counter = []
    arr.sort()

    for num in arr:
        elem = bin(num).count("1")
        counter.append(elem)

    max_ones = max(counter)
    arr_dict = {k: v for k, v in zip(arr, counter)}

    arr_list = [[] for _ in range(max_ones + 1)]

    for k in arr:
        arr_list[arr_dict[k]].append(k)

    result = []

    for elem in arr_list:
        result.extend(elem)

    return result


if __name__ == '__main__':
    assert (sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8])) == [0, 1, 2, 4, 8, 3, 5, 6, 7]
    assert (sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1])) == [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    assert (sortByBits([10000, 10000])) == [10000, 10000]
