def isSameAfterReversals(num: int) -> bool:

    if num == 0:
        return True

    if num % 10 == 0:
        return False
    return True


if __name__ == '__main__':
    assert(isSameAfterReversals(526)) is True
    assert(isSameAfterReversals(1800)) is False
    assert(isSameAfterReversals(0)) is True
