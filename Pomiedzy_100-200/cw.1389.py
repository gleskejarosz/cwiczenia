def createTargetArray(nums: list, index: list) -> list:
    target = []

    for idx, num in enumerate(nums):
        pos = index[idx]
        target.insert(pos, num)

    return target


if __name__ == '__main__':
    assert (createTargetArray(nums=[0, 1, 2, 3, 4], index=[0, 1, 2, 2, 1])) == [0, 4, 1, 3, 2]
    assert (createTargetArray(nums=[1, 2, 3, 4, 0], index=[0, 1, 2, 3, 0])) == [0, 1, 2, 3, 4]
    assert (createTargetArray(nums=[1], index=[0])) == [1]
