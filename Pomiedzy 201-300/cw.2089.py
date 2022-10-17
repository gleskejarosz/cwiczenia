def targetIndices(nums: list, target: int) -> list:
    result = []
    nums_sorted = sorted(nums)

    for idx, num in enumerate(nums_sorted):
        if num == target:
            result.append(idx)

    return result


if __name__ == '__main__':
    assert (targetIndices(nums=[1, 2, 5, 2, 3], target=2)) == [1, 2]
    assert (targetIndices(nums=[1, 2, 5, 2, 3], target=3)) == [3]
    assert (targetIndices(nums=[1, 2, 5, 2, 3], target=5)) == [4]
