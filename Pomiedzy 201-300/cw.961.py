def repeatedNTimes(nums: list) -> int:
    n = len(nums) // 2

    for num in nums:
        if nums.count(num) == n:
            return num


if __name__ == '__main__':
    assert (repeatedNTimes([1, 2, 3, 3])) == 3
    assert (repeatedNTimes([2, 1, 2, 5, 3, 2])) == 2
    assert (repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4])) == 5
