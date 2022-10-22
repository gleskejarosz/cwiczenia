def minimumOperations(nums: list) -> int:
    counter = 0
    nums_sum = sum(nums)

    if nums_sum == 0:
        return 0

    while nums_sum > 0:
        min_num = [x for x in sorted(nums) if x > 0][0]
        for idx, num in enumerate(nums):
            value = num - min_num
            if value < 0:
                nums[idx] = 0
            else:
                nums[idx] = value
        counter += 1
        nums_sum = sum(nums)

    return counter


if __name__ == '__main__':
    assert (minimumOperations([1, 5, 0, 3, 5])) == 3
    assert (minimumOperations([0])) == 0
