def findGCD(nums: list) -> int:
    min_num = min(nums)
    max_num = max(nums)
    max_divisor = 1
    divisors = [x for x in range(1, min_num + 1)]

    for divisor in divisors:
        if min_num % divisor == 0 and max_num % divisor == 0:
            max_divisor = divisor

    return max_divisor


if __name__ == '__main__':
    assert (findGCD([2, 5, 6, 9, 10])) == 2
    assert (findGCD([7, 5, 6, 8, 3])) == 1
    assert (findGCD([3, 3])) == 3
