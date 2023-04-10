def arraySign(nums: list) -> int:
    result = 1

    for num in nums:
        result *= num

    if result > 0:
        return 1
    elif result < 0:
        return -1
    else:
        return 0


if __name__ == '__main__':
    assert (arraySign(nums=[-1, -2, -3, -4, 3, 2, 1])) == 1
    assert (arraySign(nums=[1, 5, 0, 2, -3])) == 0
    assert (arraySign(nums=[-1, 1, -1, 1, -1])) == -1
