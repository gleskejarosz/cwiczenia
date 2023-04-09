def largestPerimeter(nums: list) -> int:
    sorted_nums = sorted(nums, reverse=True)

    for i in range(len(sorted_nums) - 2):
        c = sorted_nums[i]
        b = sorted_nums[i + 1]
        a = sorted_nums[i + 2]
        if a + b > c:
            return a + b + c
    return 0


if __name__ == '__main__':
    assert (largestPerimeter([2, 1, 2])) == 5
    assert (largestPerimeter([1, 2, 1, 10])) == 0
