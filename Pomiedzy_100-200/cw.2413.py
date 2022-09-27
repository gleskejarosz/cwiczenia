def smallestEvenMultiple(n: int) -> int:
    if n % 2 == 0:
        return n
    else:
        return 2 * n


if __name__ == '__main__':
    assert(smallestEvenMultiple(5)) == 10
    assert(smallestEvenMultiple(6)) == 6
