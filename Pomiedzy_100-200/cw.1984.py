def minimumDifference(nums: list, k: int) -> int:
    difference = []
    nums_len = len(nums)

    if nums_len == 1:
        return 0

    nums.sort()

    for idx, num in enumerate(nums):
        if idx + k - 1 < nums_len:
            difference.append(nums[idx + k - 1] - num)

    return min(difference)


if __name__ == '__main__':
    assert (minimumDifference(nums=[90], k=1)) == 0
    assert (minimumDifference(nums=[9, 4, 1, 7], k=2)) == 2
    assert (minimumDifference(nums=[87063, 61094, 44530, 21297, 95857, 93551, 9918], k=6)) == 74560
