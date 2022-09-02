def arithmeticTriplets(nums: list, diff: int) -> int:
    result = []

    for elem in nums[:-2]:
        mid_num = elem + diff
        max_num = mid_num + diff
        if mid_num in nums and max_num in nums:
            result.append((elem, mid_num, max_num))

    return len(result)


if __name__ == '__main__':
    assert (arithmeticTriplets(nums=[0, 1, 4, 6, 7, 10], diff=3)) == 2
    assert (arithmeticTriplets(nums=[4, 5, 6, 7, 8, 9], diff=2)) == 2
