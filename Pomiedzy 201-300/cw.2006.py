def countKDifference(nums: list, k: int) -> int:
    counter = 0
    nums_len = len(nums)

    for idx, num in enumerate(nums):
        if idx + 1 > nums_len:
            break
        for n in nums[idx + 1:]:
            if abs(num - n) == k:
                counter += 1

    return counter


if __name__ == '__main__':
    assert (countKDifference(nums=[1, 2, 2, 1], k=1)) == 4
    assert (countKDifference(nums=[1, 3], k=3)) == 0
    assert (countKDifference(nums=[3, 2, 1, 5, 4], k=2)) == 3
