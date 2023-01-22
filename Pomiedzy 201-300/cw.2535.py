from functools import reduce


def differenceOfSum(nums: list) -> int:
    sum_nums = reduce(lambda x, y: x + y, nums)
    digits_sum = 0

    for num in nums:
        num_str = str(num)
        for elem in num_str:
            digits_sum += int(elem)

    return abs(sum_nums - digits_sum)


if __name__ == '__main__':
    assert (differenceOfSum([1, 15, 6, 3])) == 9
    assert (differenceOfSum([1, 2, 3, 4])) == 0
