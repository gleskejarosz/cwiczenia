def buildArray(nums: list) -> list:
    result = [0 for x in range(len(nums))]

    for idx, num in enumerate(nums):
        result[idx] = nums[num]

    return result

if __name__ == '__main__':
    assert (buildArray([0, 2, 1, 5, 3, 4])) == [0, 1, 2, 4, 5, 3]
    assert (buildArray([5, 0, 1, 2, 3, 4])) == [4, 5, 0, 1, 2, 3]
