def minOperations(nums: list) -> int:
    counter = 0

    prev = nums[0]
    for num in nums[1:]:
        if prev >= num:
            sub = prev - num
            counter += sub + 1
            prev = num + sub + 1
        else:
            prev = num
    return counter


if __name__ == '__main__':
    assert (minOperations([1, 1, 1])) == 3
    assert (minOperations([1, 5, 2, 4, 1])) == 14
    assert (minOperations([8])) == 0
    assert (minOperations([7, 4, 2, 8, 1, 7, 7, 10])) == 38
