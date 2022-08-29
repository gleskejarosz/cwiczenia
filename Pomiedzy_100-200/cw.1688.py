def numberOfMatches(n: int) -> int:
    matches = 0

    while n > 1:
        if n % 2 == 0:
            n = n / 2
            matches += n
        else:
            matches += (n - 1) / 2 + 1
            n = (n - 1) / 2

    return int(matches)


if __name__ == '__main__':
    assert(numberOfMatches(7)) == 6
    assert(numberOfMatches(14)) == 13
