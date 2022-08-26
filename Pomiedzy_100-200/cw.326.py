def isPowerOfThree(n: int) -> bool:
    if n < 1:
        return False
    while n % 3 == 0:
        n /= 3
    return n == 1


if __name__ == '__main__':
    assert(isPowerOfThree(27)) is True
    assert(isPowerOfThree(0)) is False
    assert(isPowerOfThree(9)) is True
    assert (isPowerOfThree(-27)) is False
    assert(isPowerOfThree(45)) is False
