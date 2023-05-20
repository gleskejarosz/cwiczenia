def isBadVersion(bad: int) -> bool:
    if bad >= 4:
        return True
    else:
        return False


def firstBadVersion(n: int) -> int:
    left, right = 0, n - 1
    while left <= right:
        middle = left + (right - left) // 2
        if isBadVersion(middle) is False:
            left = middle + 1
        else:
            right = middle - 1
    return left


if __name__ == '__main__':
    assert (firstBadVersion(n=5)) == 4
    assert (firstBadVersion(n=1)) == 1
