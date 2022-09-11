def shuffle(nums: list, n: int) -> list:
    result = []

    for idx, num in enumerate(nums):
        result.append(num)
        result.append(nums[idx + n])
        if idx == n - 1:
            break

    return result


if __name__ == '__main__':
    assert (shuffle(nums=[2, 5, 1, 3, 4, 7], n=3)) == [2, 3, 5, 4, 1, 7]
    assert (shuffle(nums=[1, 2, 3, 4, 4, 3, 2, 1], n=4)) == [1, 4, 2, 3, 3, 2, 4, 1]
    assert (shuffle(nums=[1, 1, 2, 2], n=2)) == [1, 2, 1, 2]
