def findFinalValue(nums: list, original: int) -> int:

    if original not in nums:
        return original

    original_value = 2 * original
    while original_value in nums:
        original_value *= 2

    return original_value


if __name__ == '__main__':
    assert (findFinalValue(nums=[5, 3, 6, 1, 12], original=3)) == 24
    assert (findFinalValue(nums=[2, 7, 9], original=4)) == 4
