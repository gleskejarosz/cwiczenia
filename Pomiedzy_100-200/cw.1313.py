def decompressRLElist(nums: list) -> list:
    result = []

    for idx, num in enumerate(nums):
        if idx % 2 == 0:
            freq = num
        else:
            value = str(num)
            for _ in range(freq):
                result.append(int(value))

    return result


if __name__ == '__main__':
    assert (decompressRLElist([1, 2, 3, 4])) == [2, 4, 4, 4]
    assert (decompressRLElist([1, 1, 2, 3])) == [1, 3, 3]
    assert (decompressRLElist([42, 39])) == [39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39,
                                             39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39,
                                             39, 39, 39, 39]
