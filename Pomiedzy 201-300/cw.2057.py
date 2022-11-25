def smallestEqual(nums: list) -> int:
    for idx, num in enumerate(nums):
        if idx % 10 == num:
            return idx

    return -1


if __name__ == '__main__':
    assert (smallestEqual([7, 8, 3, 5, 2, 6, 3, 1, 1, 4, 5, 4, 8, 7, 2, 0, 9, 9, 0, 5, 7, 1, 6])) == 21
    assert (smallestEqual([0, 1, 2])) == 0
    assert (smallestEqual([4, 3, 2, 1])) == 2
    assert (smallestEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) == -1
