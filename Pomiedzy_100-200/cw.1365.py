def smallerNumbersThanCurrent(nums: list) -> list:
    result = []
    nums_list = list(nums)
    nums_sorted = sorted(nums)

    for num in nums_list:
        result.append(nums_sorted.index(num))

    return result


if __name__ == '__main__':
    assert (smallerNumbersThanCurrent([8, 1, 2, 2, 3])) == [4, 0, 1, 1, 3]
    assert (smallerNumbersThanCurrent([6, 5, 4, 8])) == [2, 1, 0, 3]
    assert (smallerNumbersThanCurrent([7, 7, 7, 7])) == [0, 0, 0, 0]
