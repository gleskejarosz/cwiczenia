from functools import reduce


def sumOfUnique(nums: list) -> int:
    unique_nums = []

    for num in nums:
        if nums.count(num) == 1:
            unique_nums.append(num)

    if len(unique_nums) == 0:
        return 0

    sum_unique_nums = reduce(lambda n, total: total + n, unique_nums)

    return sum_unique_nums


if __name__ == '__main__':
    assert (sumOfUnique([1, 2, 3, 2])) == 4
    assert (sumOfUnique([1, 1, 1, 1, 1])) == 0
    assert (sumOfUnique([1, 2, 3, 4, 5]) == 15)
