def twoSum(nums: list, target: int) -> list:
    data = sorted(nums)

    i, j = 0, len(data) - 1
    while i < j:
        value = data[i] + data[j]
        if value > target:
            j -= 1
        if value < target:
            i += 1
        if value == target:
            break

    idx1 = nums.index(data[i])
    if data[i] == data[j]:
        idx2 = nums.index(data[j], idx1 + 1)
    else:
        idx2 = nums.index(data[j])

    return [idx1, idx2]


if __name__ == '__main__':
    assert (twoSum(nums=[3, 2, 3], target=6)) == [0, 2]
    assert (twoSum(nums=[2, 7, 11, 15], target=9)) == [0, 1]
    assert (twoSum(nums=[3, 2, 4], target=6)) == [1, 2]
    assert (twoSum(nums=[3, 3], target=6)) == [0, 1]
